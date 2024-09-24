import pandas as pd # type: ignore
import random # type: ignore
from faker import Faker # type: ignore

def gerar_dados_usuarios(num_linhas: int):
    fake = Faker("pt-BR")
    df = pd.DataFrame()

    lista_dominios: list = ["example.com", "empresa.com", "yahoo.com.br", 
                            "gmail.com", "uol.com.br", "hotmail.com"]
    lista_emails: list = []

    df["ID"] = [_ for _ in range(num_linhas)]
    df["Nome"] = [fake.name() for _ in range(num_linhas)]

    for _ in range(num_linhas):
        email_selecionado = random.choice(lista_dominios)
        lista_emails.append(fake.email(domain = email_selecionado))

    df["E-mail"] = lista_emails

    return print(df.head(num_linhas))

def main():
    gerar_dados_usuarios(20)

if __name__ == "__main__":
    main()