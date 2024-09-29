from gerar_vendas_xlsx import gerar_vendas_xlsx
from utils import ler_arquivo_xlsx, calcular_total_vendas_produtos, gerar_arquivo_csv

def main():
    #gerar_vendas_xlsx()

    path_raw: str = './data/raw/vendas_raw.xlsx'
    path_processed: str = './data/processed/total_vendas_por_produto.csv'

    excel_file = ler_arquivo_xlsx(path_raw)
    excel_file_grouped = calcular_total_vendas_produtos(excel_file)

    gerar_arquivo_csv(excel_file_grouped,path_processed)

if __name__ == '__main__':
    main()