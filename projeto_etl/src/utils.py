import csv

def importar_csv(caminho_csv_raw: str) -> dict:
    """
    Lê um arquivo CSV e retorna uma lista de dicionários
    onde cada dicionário representa uma linha do CSV.

    :param caminho_csv: Caminho para o arquivo CSV.
    :return: Lista de dicionários contendo os dados do CSV.
    """
    try:
        with open(file = caminho_csv_raw, mode = "r", encoding = "utf-8") as file:
            arquivo = list(csv.DictReader(file))
            print("Arquivo 'csv' importado com sucesso!")
            return arquivo
        
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_csv_raw} não foi encontado.")
        return []
    
    except Exception as e:
        print(f"Erro: {e}. Tente novamente.")
        return []
    
def filtrar_emails(arquivo_csv: list) -> list:
    """
    Função que recebe um arquivo csv no formato de uma lista de dicionários
    e filtra os dados pelo campo "E-mail" quando os usuários tiverem emails
    que terminam com "@empresa.com".

    :params arquivo_csv: Arquivo csv no formato de uma lista de dicionários.
    :return: Lista de dicionários com dados filtrados.
    """
    list_dados: list = []

    try:
        for dict_dados in arquivo_csv:
            list_email: list = []
            email: str = dict_dados.get("E-mail","")

            if isinstance(email, str):
                list_email: list = email.split("@")
                if "empresa.com" in list_email:
                    list_dados.append(dict_dados)

        print("E-mails filtrados com sucesso!")
        return list_dados
    
    except Exception as e:
        print(f"Erro: {e}. Tente novamente.")
        return []

def salvar_como_csv(caminho_csv_processed: str, arquivo_csv: list) -> None:
    """
    Salva uma lista de dicionários em um arquivo CSV.

    :param caminho_csv_processed: Caminho para o arquivo CSV de saída.
    :param arquivo_csv: Lista de dicionários contendo os dados a serem salvos.
    """
    cabecalho: list= ["ID", "Nome", "E-mail"]

    try:
        with open(caminho_csv_processed, mode = "w", newline = "", encoding = "utf-8") as file:
            writer = csv.DictWriter(file, fieldnames = cabecalho)
            writer.writeheader()
            for dict_dados in arquivo_csv:
                if all(key in dict_dados for key in cabecalho):
                    writer.writerow(dict_dados)
                else:
                    print(f"Dado com ID {dict_dados.get('ID')} está faltando campos.")

        print("Arquivo 'csv' salvo com sucesso!")

    except Exception as e:
        print(f"Erro ao salvar o arquivo CSV: {e}")

               
