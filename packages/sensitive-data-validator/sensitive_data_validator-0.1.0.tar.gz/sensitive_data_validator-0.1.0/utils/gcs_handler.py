from google.cloud import storage
from google.oauth2 import service_account
from google.cloud import logging
import datetime

class GCSHandler:
    """
    Classe para manipular operações no Google Cloud Storage (GCS) e buscar informações de arquivos usando o Google Cloud Logging.
    """
    def __init__(self, project_id, bucket_name, credentials_path=None):
        """
        Inicializa o GCSHandler com o ID do projeto, nome do bucket e caminho para as credenciais.

        :param project_id: ID do projeto no Google Cloud.
        :param bucket_name: Nome do bucket no GCS.
        :param credentials_path: Caminho para o arquivo de credenciais do Google Cloud (opcional).
        """
        if credentials_path:
            # Carrega as credenciais a partir do arquivo especificado
            credentials = service_account.Credentials.from_service_account_file(credentials_path)
            self.client = storage.Client(project=project_id, credentials=credentials)
            self.logging_client = logging.Client(project=project_id, credentials=credentials)
        else:
            # Inicializa os clientes de armazenamento e logging sem credenciais específicas
            self.client = storage.Client(project=project_id)
            self.logging_client = logging.Client(project=project_id)
        
        # Referencia o bucket especificado
        self.bucket = self.client.bucket(bucket_name)

    def get_file_info(self, blob_name):
        """
        Obtém informações sobre um arquivo específico no bucket do GCS.

        :param blob_name: Nome do blob (arquivo) no bucket.
        :return: Dicionário com o e-mail do usuário que fez o upload, nome do bucket e ID do projeto.
        """
        # Carrega o blob (arquivo) especificado
        blob = self.bucket.blob(blob_name)
        blob.reload()
        
        # Obtém o e-mail do usuário que fez o upload
        uploader_email = self.get_uploader_email(blob_name)
        
        return {
            'email': uploader_email,
            'bucket': blob.bucket.name,
            'project': self.client.project
        }
    
    def get_uploader_email(self, blob_name):
        """
        Busca o e-mail do usuário que fez o upload do arquivo nos logs de auditoria do Google Cloud.

        :param blob_name: Nome do blob (arquivo) no bucket.
        :return: E-mail do usuário que fez o upload, se encontrado; caso contrário, None.
        """
        end_time = datetime.datetime.utcnow()
        start_time = end_time - datetime.timedelta(minutes=10)  # Ajusta o intervalo de tempo conforme necessário
        
        # Filtro para buscar logs específicos de criação de objetos no bucket do GCS
        filter_str = (
            f'protoPayload.methodName="storage.objects.create" '
            f'AND resource.labels.bucket_name="{self.bucket.name}" '
            f'AND protoPayload.resourceName="projects/_/buckets/{self.bucket.name}/objects/{blob_name}" '
        )

        # Busca entradas de log com o filtro especificado
        entries = self.logging_client.list_entries(filter_=filter_str, order_by=logging.DESCENDING, page_size=1)
        
        for entry in entries:
            if 'protoPayload' in entry:
                # Retorna o e-mail do usuário que fez o upload, se encontrado nos logs
                return entry['protoPayload'].get('authenticationInfo', {}).get('principalEmail', None)
        
        # Retorna None se o e-mail não for encontrado nos logs
        return None
