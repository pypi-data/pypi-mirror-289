import json
import re
from datetime import datetime
from validate_docbr import CPF, CNPJ, CNH, TituloEleitoral, PIS
from validators import PhoneValidator, RegexValidator, remove_non_numeric
from utils import ResultHandler, GCSHandler
from data_processor import FileProcessor

class SensitiveAPI:
    """
    API para verificar a presença de dados sensíveis em arquivos e strings.
    Suporta integração com Google Cloud Storage para obter informações adicionais sobre os arquivos.
    """
    
    def __init__(self, file_path=None, fields_to_check=None, gcs_config=None):
        """
        Inicializa a API com opções para verificar arquivos e strings em busca de dados sensíveis.

        :param file_path: Caminho do arquivo a ser verificado (opcional).
        :param fields_to_check: Lista de campos a serem verificados (opcional).
        :param gcs_config: Configurações para integração com Google Cloud Storage (opcional).
        """
        self.file_path = file_path
        self.fields_to_check = fields_to_check
        self.gcs_handler = None

        if gcs_config:
            self.gcs_handler = GCSHandler(
                project_id=gcs_config['project_id'],
                bucket_name=gcs_config['bucket_name'],
                credentials_path=gcs_config.get('credentials')
            )

        # Inicializa validadores para diferentes tipos de dados sensíveis
        self.validators = {
            'BRAZIL_PERSONAL_ID': CPF(),
            'BRAZIL_COMPANY_ID': CNPJ(),
            'BRAZIL_DRIVER_ID': CNH(),
            'BRAZIL_VOTER_ID': TituloEleitoral(),
            'BRAZIL_EMPLOYEE_ID': PIS(),
            'PHONE_NUMBER': PhoneValidator()
        }
        # Padrões regex para validar diferentes tipos de dados sensíveis
        self.regex_validators = RegexValidator.patterns

    def check_sensitive_data(self, value):
        """
        Verifica se o valor fornecido contém dados sensíveis.

        :param value: String a ser verificada.
        :return: Dicionário com o resultado da verificação para cada tipo de dado.
        """
        results = {}
        fields = self.fields_to_check if self.fields_to_check else list(self.validators.keys()) + list(self.regex_validators.keys())

        for doc_type in fields:
            if doc_type in self.validators:
                if doc_type in ['BRAZIL_PERSONAL_ID', 'PHONE_NUMBER']:
                    numeric_value = remove_non_numeric(value)
                    if self.validators[doc_type].validate(numeric_value):
                        results[doc_type] = True
                else:
                    if self.validators[doc_type].validate(value):
                        results[doc_type] = True
            elif doc_type in self.regex_validators and RegexValidator.validate(doc_type, value):
                results[doc_type] = True
            else:
                results[doc_type] = False

        return results

    def check_string(self, string):
        """
        Verifica cada linha da string fornecida em busca de dados sensíveis.

        :param string: String a ser verificada.
        :return: Dicionário com os resultados da verificação.
        """
        fields = self.fields_to_check if self.fields_to_check else list(self.validators.keys()) + list(self.regex_validators.keys())
        found_details = ResultHandler.initialize_results(fields)
        
        for line in string.splitlines():
            value = line.strip()
            results = self.check_sensitive_data(value)
            for doc_type, found in results.items():
                if found:
                    ResultHandler.update_results(found_details, doc_type)

        return found_details

    def file_check(self, file_path, filetype, delimiter=None):
        """
        Verifica o arquivo especificado em busca de dados sensíveis.

        :param file_path: Caminho do arquivo a ser verificado.
        :param filetype: Tipo do arquivo (json, csv, parquet, txt).
        :param delimiter: Delimitador para arquivos CSV (opcional).
        :return: Resultados da verificação em formato JSON.
        """
        fields = self.fields_to_check if self.fields_to_check else list(self.validators.keys()) + list(self.regex_validators.keys())
        results = {
            "filename": file_path,
            "data_e_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            **ResultHandler.initialize_results(fields)
        }

        try:
            if filetype == 'json':
                data = FileProcessor.read_json(file_path)
            elif filetype == 'csv':
                data = FileProcessor.read_csv(file_path, delimiter=delimiter if delimiter else ',')
            elif filetype == 'parquet':
                data = FileProcessor.read_parquet(file_path)
            elif filetype == 'txt':
                content = FileProcessor.read_txt(file_path)
                return self.check_txt(content, results)
            else:
                raise ValueError(f"Unsupported filetype: {filetype}")

            for column in data.columns:
                for index, value in data[column].dropna().items():
                    check_results = self.check_sensitive_data(str(value))
                    for doc_type, found in check_results.items():
                        if found:
                            ResultHandler.update_results(results, doc_type)

            if self.gcs_handler:
                gcs_info = self.gcs_handler.get_file_info(file_path)
                results['uploader_email'] = gcs_info['email']
                results['bucket'] = gcs_info['bucket']
                results['project'] = gcs_info['project']

        except Exception as e:
            ResultHandler.handle_error(results, str(e))

        return json.dumps(results, indent=4, ensure_ascii=False)

    def check_txt(self, content, results):
        """
        Verifica o conteúdo de um arquivo TXT em busca de dados sensíveis.

        :param content: Conteúdo do arquivo TXT.
        :param results: Dicionário para armazenar os resultados da verificação.
        :return: Resultados da verificação em formato JSON.
        """
        for line in content.splitlines():
            value = line.strip()
            check_results = self.check_sensitive_data(value)
            for doc_type, found in check_results.items():
                if found:
                    ResultHandler.update_results(results, doc_type)
        return json.dumps(results, indent=4, ensure_ascii=False)
