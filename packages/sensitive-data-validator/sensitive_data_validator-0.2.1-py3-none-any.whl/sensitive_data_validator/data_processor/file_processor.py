import json
import pandas as pd

class FileProcessor:
    """
    Classe para processar arquivos de diferentes formatos e convertê-los em estruturas de dados pandas.
    """
    
    @staticmethod
    def read_json(file_path):
        """
        Lê um arquivo JSON e o converte em um DataFrame pandas.

        :param file_path: Caminho do arquivo JSON.
        :return: DataFrame pandas contendo os dados do arquivo JSON.
        """
        with open(file_path, 'r') as file:
            data = json.load(file)
        return pd.json_normalize(data)

    @staticmethod
    def read_csv(file_path, delimiter=','):
        """
        Lê um arquivo CSV e o converte em um DataFrame pandas.

        :param file_path: Caminho do arquivo CSV.
        :param delimiter: Delimitador usado no arquivo CSV (padrão é ',').
        :return: DataFrame pandas contendo os dados do arquivo CSV.
        """
        return pd.read_csv(file_path, delimiter=delimiter)

    @staticmethod
    def read_parquet(file_path):
        """
        Lê um arquivo Parquet e o converte em um DataFrame pandas.

        :param file_path: Caminho do arquivo Parquet.
        :return: DataFrame pandas contendo os dados do arquivo Parquet.
        """
        return pd.read_parquet(file_path)

    @staticmethod
    def read_txt(file_path):
        """
        Lê um arquivo TXT e retorna seu conteúdo como uma string.

        :param file_path: Caminho do arquivo TXT.
        :return: String contendo o conteúdo do arquivo TXT.
        """
        with open(file_path, 'r') as file:
            content = file.read()
        return content
