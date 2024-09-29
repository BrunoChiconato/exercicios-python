import pandas as pd  # type: ignore

def ler_arquivo_xlsx(path: str) -> pd.DataFrame:
    """
    Lê um arquivo Excel e retorna seu conteúdo como um DataFrame.

    Args:
        path (str): O caminho do arquivo Excel a ser lido.

    Returns:
        pd.DataFrame: DataFrame com o conteúdo do arquivo Excel.
    """
    sales = pd.read_excel(path)
    return sales


def calcular_total_vendas_produtos(arquivo: pd.DataFrame) -> pd.DataFrame:
    """
    Agrupa as vendas por produto e calcula o total de vendas para cada produto.

    Args:
        arquivo (pd.DataFrame): DataFrame contendo os dados de vendas, com colunas 'Produto' e 'Valor_Venda'.

    Returns:
        pd.DataFrame: DataFrame com o total de vendas para cada produto.
    """
    arquivo_agrupado = arquivo.groupby(['Produto']).sum().round()
    return arquivo_agrupado


def gerar_arquivo_csv(arquivo: pd.DataFrame, path: str):
    """
    Gera um arquivo CSV com os dados fornecidos em um DataFrame.

    Args:
        arquivo (pd.DataFrame): DataFrame contendo os dados a serem salvos no CSV.
        path (str): O caminho onde o arquivo CSV será salvo.

    Returns:
        None
    """
    arquivo.to_csv(path)
