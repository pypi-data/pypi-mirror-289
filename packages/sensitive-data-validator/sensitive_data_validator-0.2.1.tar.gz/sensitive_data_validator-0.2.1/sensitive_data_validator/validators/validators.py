#Esse script utiliza a biblioteca validate_docbr que contém os algoritmos de validação de documentos brasileiros.
#Para mais informações, consultar: https://pypi.org/project/validate-docbr/


import re
from validate_docbr import CPF, CNPJ, CNH, TituloEleitoral, PIS

# Função para remover todos os caracteres não numéricos de uma string
def remove_non_numeric(value):
    """
    Remove todos os caracteres não numéricos da string fornecida.

    :param value: String de entrada.
    :return: String contendo apenas caracteres numéricos.
    """
    return re.sub(r'\D', '', value)

# Classe para validar números de telefone brasileiros
class PhoneValidator:
    """
    Validador de números de telefone brasileiros.
    """
    def __init__(self):
        # Padrão regex para validar números de telefone no formato brasileiro (com ou sem DDD)
        self.pattern = re.compile(r'^(?:\d{2})?(?:9?\d{4})\d{4}$')

    def validate(self, phone_number):
        """
        Valida o número de telefone fornecido.

        :param phone_number: String contendo o número de telefone.
        :return: True se o número for válido, False caso contrário.
        """
        # Remove todos os caracteres não numéricos do número de telefone
        cleaned_number = re.sub(r'\D', '', phone_number)
        # Verifica se o número limpo corresponde ao padrão regex
        return bool(self.pattern.fullmatch(cleaned_number))

# Classe para validar números de cartão de crédito usando o algoritmo de Luhn
class CreditCardValidator:
    """
    Validador de números de cartão de crédito usando o algoritmo de Luhn.
    """
    @staticmethod
    def validate(card_number):
        """
        Valida o número de cartão de crédito fornecido.

        :param card_number: String contendo o número do cartão de crédito.
        :return: True se o número for válido, False caso contrário.
        """
        # Remove todos os caracteres não numéricos do número do cartão
        card_number = re.sub(r'\D', '', card_number)
        
        # Converte cada dígito em um inteiro
        card_number = [int(num) for num in card_number]

        # Remove o último dígito (dígito verificador)
        checkDigit = card_number.pop(-1)

        # Inverte os dígitos restantes
        card_number.reverse()

        # Dobra os dígitos em posições pares
        card_number = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_number)]

        # Subtrai 9 dos dígitos que resultaram em um valor maior que 9
        card_number = [num - 9 if idx % 2 == 0 and num > 9 else num for idx, num in enumerate(card_number)]

        # Adiciona o dígito verificador de volta à lista
        card_number.append(checkDigit)

        # Soma todos os dígitos
        checkSum = sum(card_number)

        # Verifica se a soma é divisível por 10
        return checkSum % 10 == 0

# Classe para validar diversos tipos de dados usando expressões regulares
class RegexValidator:
    """
    Validador genérico usando expressões regulares para diversos tipos de dados.
    """
    # Padrões regex para validar diferentes tipos de dados
    patterns = {
        'EMAIL': re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$'),  # Padrão para validar endereços de e-mail
        'GENERIC_PASSWORD': re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$'),  # Padrão para validar senhas complexas
        'GOOGLE_API_KEY': re.compile(r'AIza[0-9A-Za-z-_]{35}'),  # Padrão para validar chaves de API do Google
        'GOOGLE_OAUTH_TOKEN': re.compile(r'ya29\.[0-9A-Za-z\-_]+'),  # Padrão para validar tokens OAuth do Google
        'GOOGLE_SERVICE_ACCOUNT_KEY': re.compile(r'-----BEGIN PRIVATE KEY-----[\s\S]+-----END PRIVATE KEY-----'),  # Padrão para validar chaves de contas de serviço do Google
        'AUTH_BASIC': re.compile(r'basic [a-zA-Z0-9=:_\+\/-]{5,100}'),  # Padrão para validar cabeçalhos de autenticação básica
        'AUTH_BEARER': re.compile(r'bearer [a-zA-Z0-9_\-\.=:_\+\/]{5,100}'),  # Padrão para validar tokens de autenticação Bearer
        'AUTH_API': re.compile(r'api[key|_key|\s+]+[a-zA-Z0-9_\-]{5,100}'),  # Padrão para validar chaves de API genéricas
        'RSA_PRIVATE_KEY': re.compile(r'-----BEGIN RSA PRIVATE KEY-----'),  # Padrão para validar chaves privadas RSA
        'SSH_DSA_PRIVATE_KEY': re.compile(r'-----BEGIN DSA PRIVATE KEY-----'),  # Padrão para validar chaves privadas DSA
        'SSH_DC_PRIVATE_KEY': re.compile(r'-----BEGIN EC PRIVATE KEY-----'),  # Padrão para validar chaves privadas EC (Elliptic Curve)
        'PGP_PRIVATE_BLOCK': re.compile(r'-----BEGIN PGP PRIVATE KEY BLOCK-----'),  # Padrão para validar blocos de chaves privadas PGP
        'JWT_TOKEN': re.compile(r'ey[A-Za-z0-9-_=]+\.[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*$'),  # Padrão para validar tokens JWT (JSON Web Token)
    }

    @classmethod
    def validate(cls, doc_type, value):
        """
        Valida o valor fornecido de acordo com o tipo de documento especificado.

        :param doc_type: Tipo de documento (chave do dicionário 'patterns').
        :param value: String contendo o valor a ser validado.
        :return: True se o valor for válido, False caso contrário.
        """
        # Verifica se o tipo de documento está nos padrões definidos
        if doc_type in cls.patterns:
            # Verifica se o valor corresponde ao padrão regex
            return bool(cls.patterns[doc_type].search(value))
        return False
