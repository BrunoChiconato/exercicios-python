from db_operations import connect_postgres, db_create_table, db_insert_data, db_retrieve_data

def main():
    conexao = connect_postgres()

    #db_create_table(conexao)
    #db_insert_data(conexao)

    resultado = db_retrieve_data(conexao)

    print("Os funcionários do departamento de 'Vendas' são:")
    [print(f"- {tupla[0]}") for tupla in resultado]

if __name__ == '__main__':
    main()