import requests #type: ignore
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setFormatter(formatter)

# console_handler = logging.StreamHandler()
# console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
# logger.addHandler(console_handler)

logger.info('-' * 50)
logger.info('Início de uma nova execução')

def requisicao_api(url: str) -> dict:
    """
    Faz uma requisição GET para a URL fornecida e retorna o conteúdo JSON.

    Args:
        url (str): A URL da API para fazer a requisição.

    Returns:
        dict: Um dicionário contendo a resposta em formato JSON se a requisição for bem-sucedida.
        None: Retorna None se houver erro na requisição ou na decodificação do JSON.
    """
    try:
        logger.info(f"Fazendo requisição para a URL: {url}")
        request = requests.get(url)
        request_json = request.json()

        logger.info("Requisição bem-sucedida.")
        return request_json
    
    except requests.exceptions.JSONDecodeError:
        logger.error('Erro ao decodificar o JSON.')
    except requests.exceptions.ConnectionError:
        logger.error('Erro de conexão. Verifique sua internet.')
    except requests.exceptions.Timeout:
        logger.error('A requisição demorou muito para responder. Timeout.')
    except requests.exceptions.RequestException as e:
        logger.critical(f'Erro ao fazer a requisição: {e}')
    return None

def criar_arquivo_txt(processed_path: str) -> None:
    """
    Cria um arquivo de texto e insere o cabeçalho com as colunas 'Preco_Bitcoin' e 'Data_Consulta'.

    Args:
        processed_path (str): Caminho completo do arquivo de texto a ser criado.
    
    Returns:
        None
    """
    logger.info(f"Criando arquivo de texto em: {processed_path}")
    try:
        with open(processed_path, 'w', encoding = 'utf-8') as file:
            file.write('Preco_Bitcoin\tData_Consulta\n')
            logger.info("Arquivo criado com sucesso.")
    except IOError as e:
        logger.error(f"Erro ao criar o arquivo: {e}")

def extrair_preco_bitcoin(json_file: dict) -> float:
    """
    Extrai o preço atual do Bitcoin em dólares americanos a partir do JSON fornecido pela API.

    Args:
        json_file (dict): O dicionário JSON retornado pela API.

    Returns:
        float: O preço do Bitcoin em dólares americanos.
    """
    logger.info("Extraindo preço do Bitcoin do JSON.")

    price_dict: dict = json_file.get('bpi',{})
    usd_price_dict: dict = price_dict.get('USD',{})
    price_bitcoin = usd_price_dict.get('rate_float',0.0)

    logger.info(f"Preço do Bitcoin do JSON extraído com sucesso: {price_bitcoin}.")

    return price_bitcoin

def extrair_data_consulta(json_file: dict) -> str:
    """
    Extrai a data e hora da consulta a partir do JSON fornecido pela API.

    Args:
        json_file (dict): O dicionário JSON retornado pela API.

    Returns:
        str: A data e hora da consulta em formato de string.
    """
    logger.info("Extraindo data de consulta do preço do Bitcoin do JSON.")
    
    time_dict: dict = json_file.get('time',{})
    date_time_consulted: str = time_dict.get('updated','Data não encontrada')

    logger.info(f"Data de consulta do preço do Bitcoin do JSON extraída com sucesso: {date_time_consulted}.")

    return date_time_consulted

def escrever_preco_data_txt(processed_path: str, bitcoin_price: float, consulted_date: str) -> None:
    """
    Escreve o preço do Bitcoin e a data/hora da consulta no arquivo de texto.

    Args:
        processed_path (str): Caminho completo do arquivo de texto onde os dados serão escritos.
        bitcoin_price (float): O preço do Bitcoin em dólares americanos.
        consulted_date (str): A data e hora da consulta.
    
    Returns:
        None
    """
    logger.info(f"Escrevendo dados no arquivo: {processed_path}")
    try:
        with open(processed_path, 'a', encoding='utf-8') as file:
            file.write(f'{bitcoin_price}\t{consulted_date}\n')
        logger.info("Dados escritos com sucesso.")
    except IOError as e:
        logger.error(f"Erro ao escrever no arquivo: {e}")