import pandas as pd # type: ignore
from faker import Faker # type: ignore

fake = Faker('pt_BR')

def gerar_nome_raw_txt():
    """
    Gera um arquivo 'nomes_raw.txt' contendo 100 nomes aleatórios.

    A função utiliza a biblioteca `faker` para gerar uma lista de 100 nomes fictícios e os 
    armazena em um arquivo CSV com separador de tabulação (tab). 
    O arquivo gerado contém uma única coluna chamada 'Nome', e é salvo no diretório './data/raw/'.

    :return: None
    """
    num_linhas: int = 100
    df = pd.DataFrame()

    df['Nome'] = [fake.name() for _ in range(num_linhas)]

    df.to_csv(path_or_buf = './data/raw/nomes_raw.txt', sep = '\t', index = False)
