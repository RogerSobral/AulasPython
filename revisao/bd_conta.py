import sqlite3 as sq

# Cria o banco e conecta com ele
def conectar():
    conn=sq.connect("banco.db")
    cursor=conn.cursor()
    return conn, cursor

# cria a tabela Cliente
def criarTabelaCliente():
    conn, cursor=conectar()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    data_nasc TEXT NOT NULL
    )
    """)
    conn.commit()
    cursor.close()
    conn.close()


#Add clientes a tabela Cliente
def addCliente(nome, data):


    criarTabelaCliente()
    conn, cursor = conectar()
    try:
        cursor.execute("""
        INSERT INTO cliente (nome, data_nasc)
        values(?,?)
        """,(nome,data))
        conn.commit()

        print("Cadastrado com sucesso!")
    except Exception as e:
        print("Erro ", e)
    finally:
        cursor.close()
        conn.close()


#vai listar os clientes que estão salvos no banco de dados
def listarCliente():
    conn, cursor = conectar()
    cursor.execute("""
    SELECT * FROM cliente;
    """)
    listaClientes=cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return listaClientes




