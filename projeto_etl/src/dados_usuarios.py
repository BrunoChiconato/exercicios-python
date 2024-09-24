import pandas as pd # type: ignore
import random # type: ignore
from faker import Faker # type: ignore

def gerar_dados_usuarios(num_linhas: int, caminho: str) -> None:
    """
    Função que gera dados aleatórios de Nome e E-mail utilizando a biblioteca Faker e
    salva como um arquivo csv utilizando a biblioteca Pandas.

    :params num_linhas: Número de linhas totais que o usuário deseja que a base tenha.
    :params caminho: Caminho onde a base será salva. 
    """
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

    df.to_csv(path_or_buf = caminho, index = False, sep = ",", encoding = "utf-8")