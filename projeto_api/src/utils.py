import requests #type: ignore

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
        request = requests.get(url)
        request_json = request.json()

        return request_json
    
    except requests.exceptions.JSONDecodeError:
        print('Erro ao decodificar o JSON.')
    except requests.exceptions.ConnectionError:
        print('Erro de conexão. Verifique sua internet.')
    except requests.exceptions.Timeout:
        print('A requisição demorou muito para responder. Timeout.')
    except requests.exceptions.RequestException as e:
        print(f'Erro ao fazer a requisição: {e}')
    return None

def criar_arquivo_txt(processed_path: str) -> None:
    """
    Cria um arquivo de texto e insere o cabeçalho com as colunas 'Preco_Bitcoin' e 'Data_Consulta'.

    Args:
        processed_path (str): Caminho completo do arquivo de texto a ser criado.
    
    Returns:
        None
    """
    with open(processed_path, 'w', encoding = 'utf-8') as file:
        file.write('Preco_Bitcoin\tData_Consulta\n')

def extrair_preco_bitcoin(json_file: dict) -> float:
    """
    Extrai o preço atual do Bitcoin em dólares americanos a partir do JSON fornecido pela API.

    Args:
        json_file (dict): O dicionário JSON retornado pela API.

    Returns:
        float: O preço do Bitcoin em dólares americanos.
    """
    price_dict: dict = json_file.get('bpi',{})
    usd_price_dict: dict = price_dict.get('USD',{})
    price_bitcoin = usd_price_dict.get('rate_float',0.0)

    return price_bitcoin

def extrair_data_consulta(json_file: dict) -> str:
    """
    Extrai a data e hora da consulta a partir do JSON fornecido pela API.

    Args:
        json_file (dict): O dicionário JSON retornado pela API.

    Returns:
        str: A data e hora da consulta em formato de string.
    """
    time_dict: dict = json_file.get('time',{})
    date_time_consulted: str = time_dict.get('updated','Data não encontrada')

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
    with open(processed_path, 'a', encoding = 'utf-8') as file:
        file.write(f'{bitcoin_price}\t{consulted_date}\n')
