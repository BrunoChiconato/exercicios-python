from transformacoes import abrir_arquivo_txt, normalizar_nomes, salvar_nomes_normalizados

def main():
    caminho_raw: str = './data/raw/nomes_raw.txt'
    caminho_processed: str = './data/processed/nomes_normalizados.txt'

    arquivo_txt_raw = abrir_arquivo_txt(caminho_raw)
    arquivo_txt_normalizado = normalizar_nomes(arquivo_txt_raw)
    salvar_nomes_normalizados(arquivo_txt_normalizado, caminho_processed)

if __name__ == '__main__':
    main()