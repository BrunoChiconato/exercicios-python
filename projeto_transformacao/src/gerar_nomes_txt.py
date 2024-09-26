import pandas as pd # type: ignore
from faker import Faker # type: ignore

fake = Faker('pt_BR')

def gerar_nome_raw_txt():
    num_linhas: int = 100
    df = pd.DataFrame()

    df['Nome'] = [fake.name() for _ in range(num_linhas)]

    df.to_csv(path_or_buf = './data/raw/nomes_raw.txt', sep = '\t', index = False)
