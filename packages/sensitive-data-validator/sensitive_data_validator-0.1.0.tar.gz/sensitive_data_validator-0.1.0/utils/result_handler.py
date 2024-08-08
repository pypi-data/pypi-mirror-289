class ResultHandler:
    """
    Classe para manipular e atualizar os resultados da verificação de dados sensíveis.
    """
    
    @staticmethod
    def initialize_results(fields):
        """
        Inicializa a estrutura de resultados para armazenar os resultados da verificação de dados sensíveis.

        :param fields: Lista de campos a serem verificados.
        :return: Dicionário com a estrutura inicializada para armazenar os resultados.
        """
        return {
            "found": False,  # Indica se algum dado sensível foi encontrado
            "total_sensitive_data_count": 0,  # Contagem total de dados sensíveis encontrados
            "details": {key: {"found": False, "count": 0} for key in fields}  # Detalhes para cada campo
        }

    @staticmethod
    def update_results(results, doc_type):
        """
        Atualiza a estrutura de resultados quando um dado sensível é encontrado.

        :param results: Dicionário contendo os resultados atuais.
        :param doc_type: Tipo de documento/dado sensível encontrado.
        """
        results["found"] = True  # Marca que algum dado sensível foi encontrado
        results["details"][doc_type]["found"] = True  # Marca que o tipo de dado específico foi encontrado
        results["details"][doc_type]["count"] += 1  # Incrementa a contagem do tipo de dado específico
        results["total_sensitive_data_count"] += 1  # Incrementa a contagem total de dados sensíveis encontrados

    @staticmethod
    def handle_error(results, error_message):
        """
        Atualiza a estrutura de resultados para incluir uma mensagem de erro quando ocorre um problema.

        :param results: Dicionário contendo os resultados atuais.
        :param error_message: Mensagem de erro a ser incluída nos resultados.
        """
        results["found"] = False  # Marca que nenhum dado sensível foi encontrado devido ao erro
        results["total_sensitive_data_count"] = 0  # Reseta a contagem total de dados sensíveis encontrados
        results["details"] = {"error": error_message}  # Inclui a mensagem de erro nos detalhes
