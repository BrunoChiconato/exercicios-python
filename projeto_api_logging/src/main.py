#from utils import requisicao_api, extrair_data_consulta, extrair_preco_bitcoin, criar_arquivo_txt, escrever_preco_data_txt
from utils_using_loguru import requisicao_api, extrair_data_consulta, extrair_preco_bitcoin, criar_arquivo_txt, escrever_preco_data_txt

def main():
    url: str = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    processed_path: str = './data/processed/preco_bitcoin.txt'

    criar_arquivo_txt(processed_path)

    json_file = requisicao_api(url)

    if json_file:
        bitcoin_price_usd: float = extrair_preco_bitcoin(json_file)
        consulted_date: str = extrair_data_consulta(json_file)

        escrever_preco_data_txt(processed_path, bitcoin_price_usd, consulted_date)

if __name__ == '__main__':
    main()
