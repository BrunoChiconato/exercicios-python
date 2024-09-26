import pandas as pd  # type: ignore

def abrir_arquivo_txt(caminho_raw: str) -> dict:
    """
    Lê o arquivo de texto especificado e retorna seu conteúdo como um dicionário, 
    onde a chave é a primeira linha (cabeçalho) e os valores são as demais linhas (nomes).

    :param caminho_raw: Caminho para o arquivo de texto contendo os nomes.
    :type caminho_raw: str

    :return: Um dicionário onde a chave é o cabeçalho e os valores são as linhas (nomes) do arquivo.
    :rtype: dict
    """
    dict_txt: dict = {}

    with open(file = caminho_raw, mode = 'r', encoding = 'utf-8') as txt:
        chave = txt.readline()
        chave_tratada = chave.replace('\n', '')

        valores = txt.readlines()
        valores_tratados = [valor.replace('\n', '') for valor in valores]

        dict_txt[chave_tratada] = valores_tratados

        return dict_txt
  
def normalizar_nomes(arquivo_txt_raw: dict) -> dict:
    """
    Recebe um dicionário contendo um cabeçalho e uma lista de nomes, e retorna um novo dicionário 
    com os nomes normalizados (convertidos para letras minúsculas e sem espaços).

    :param arquivo_txt_raw: Dicionário com o cabeçalho e os nomes a serem normalizados.
    :type arquivo_txt_raw: dict
    
    :return: Um dicionário onde os nomes foram normalizados (em minúsculas e sem espaços).
    :rtype: dict
    """
    aux_names_list: list = []
    aux_dict: dict = {}

    for names in arquivo_txt_raw.values():
        for name in names:
            aux_names_list.append(name.lower().replace(' ', ''))

    aux_dict['Nome'] = aux_names_list

    return aux_dict

def salvar_nomes_normalizados(arquivo_txt_normalizado: dict, caminho_processed: str) -> None:
    """
    Salva os nomes normalizados em um arquivo CSV com separador de tabulação.

    :param arquivo_txt_normalizado: Dicionário contendo os nomes normalizados para serem salvos.
    :type arquivo_txt_normalizado: dict

    :param caminho_processed: Caminho para o arquivo onde os nomes normalizados serão salvos.
    :type caminho_processed: str
    
    :return: None
    """
    df = pd.DataFrame(arquivo_txt_normalizado)

    df.to_csv(path_or_buf = caminho_processed, sep = '\t', encoding = 'utf-8', index = False)

