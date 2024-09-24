from dados_usuarios import gerar_dados_usuarios
from utils import importar_csv, filtrar_emails, salvar_como_csv

def main():
    num_linhas: int = 100
    caminho_raw: str = "./data/raw/dados_usuarios_raw.csv"
    caminho_processed: str = "./data/processed/dados_usuarios_processed.csv"

    gerar_dados_usuarios(num_linhas, caminho_raw)

    arquivo_csv = importar_csv(caminho_raw)
    arquivo_csv_filtrado = filtrar_emails(arquivo_csv)
    
    salvar_como_csv(caminho_processed, arquivo_csv_filtrado)

if __name__ == "__main__":
    main()