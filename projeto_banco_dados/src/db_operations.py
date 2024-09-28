import psycopg2 # type: ignore

def connect_postgres():
    """
    Estabelece uma conexão com o banco de dados PostgreSQL.

    Tenta conectar ao banco de dados PostgreSQL com as credenciais e configurações fornecidas.
    Se a conexão for bem-sucedida, retorna o objeto de conexão. Caso contrário, retorna None.

    :return: Objeto de conexão ao banco de dados PostgreSQL se a conexão for bem-sucedida,
    ou None em caso de falha.
    """
    try:
        conexao = psycopg2.connect(
            host="localhost",
            port="5432",
            database="postgres",
            user="postgres",
            password="postgres"
        )
        print("Conexão com o banco de dados foi bem-sucedida!")
        return conexao

    except Exception as erro:
        print(f"Erro ao conectar ao banco de dados: {erro}")
        return None

def db_create_table(conexao):
    """
    Cria a tabela 'funcionarios' no banco de dados, se ela não existir.

    Executa um comando SQL para criar uma tabela chamada 'funcionarios' com colunas de ID, nome e departamento.
    A função faz o commit da transação ao banco de dados e fecha a conexão ao final.

    :params: Objeto de conexão ao banco de dados PostgreSQL.

    :return: None
    """
    if conexao is None:
        print("Conexão inválida.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS funcionarios(
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                departamento VARCHAR(100) NOT NULL
            );
        """)

        conexao.commit()

        print("Tabela criada com sucesso!")

    except Exception as erro:
        print(f"Erro ao criar a tabela: {erro}")

def db_insert_data(conexao):
    """
    Insere dados na tabela 'funcionarios'.

    Insere cinco registros de funcionários com os nomes e departamentos especificados na tabela 'funcionarios'.
    Faz o commit da transação e fecha a conexão ao banco de dados.

    :params: Objeto de conexão ao banco de dados PostgreSQL.

    :return: None
    """
    if conexao is None:
        print("Conexão inválida.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO funcionarios (nome, departamento) VALUES 
            ('Bruno', 'Vendas'),
            ('Gabriel', 'Compras'),
            ('Gustavo', 'Compras'),
            ('Fabrício', 'Peças'),
            ('Pablo', 'Vendas');
        """)

        conexao.commit()

        print("Dados inseridos com sucesso!")

    except Exception as erro:
        print(f"Erro ao tentar inserir dados na tabela: {erro}")

def db_retrieve_data(conexao):
    """
    Recupera dados da tabela 'funcionarios' onde o departamento é 'Vendas'.

    Executa uma consulta SQL para buscar os nomes dos funcionários que pertencem ao departamento 'Vendas'.
    Retorna os resultados da consulta.

    :params: Objeto de conexão ao banco de dados PostgreSQL.

    :params: Lista de tuplas com os nomes dos funcionários que pertencem ao departamento 'Vendas'.
    """
    if conexao is None:
        print("Conexão inválida.")
        return

    try:
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT nome FROM funcionarios
            WHERE departamento = 'Vendas';
        """)

        resultado = cursor.fetchall()

        print("Consulta realizada com sucesso!")

    except Exception as erro:
        print(f"Erro ao tentar consultar a tabela: {erro}")
    
    finally:
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")

        return resultado