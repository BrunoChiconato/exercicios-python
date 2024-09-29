import pandas as pd  # type: ignore
import numpy as np #type: ignore

def gerar_vendas_xlsx():
    """
    Gera um arquivo Excel com dados de vendas fictícias.

    A função cria um DataFrame com 1000 linhas, preenchendo as colunas
    com um produto aleatório e um valor de venda aleatório. O resultado
    é salvo como um arquivo Excel em './data/raw/vendas_raw.xlsx'.
    
    Returns:
        None
    """
    sales = pd.DataFrame()
    rows_num: int = 1000
    products_list: list = ['Celular','Notebook','Desktop','Pendrive','Mouse','Teclado']

    sales['Produto'] = np.random.choice(products_list,rows_num)
    sales['Valor_Venda'] = np.random.uniform(0.0,1000.0,rows_num)

    sales.to_excel('./data/raw/vendas_raw.xlsx', index = False)