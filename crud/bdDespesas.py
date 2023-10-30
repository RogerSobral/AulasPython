import sqlite3 as sq

def connect_despesa():
    conn= sq.connect("despesa.db")
    cursor= conn.cursor()
    return conn, cursor

def creat_table_despesa():
    conn, cursor=connect_despesa()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS DESPESAS(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    DESCRICAO TEXT NOT NULL,
    VALOR REAL NOT NULL,
    DATA_LANCAMENTO TEXT
    );
    """)

    conn.commit()
    cursor.close()
    conn.close()

def addDespesa(descricao,valor,data):
    creat_table_despesa()
    conn, cursor = connect_despesa()

    cursor.execute(""" INSERT INTO DESPESAS (DESCRICAO,VALOR,DATA_LANCAMENTO)
    VALUES(?,?,?)
    """,(descricao,valor,data))
    conn.commit()
    cursor.close()
    conn.close()

def listarDespesas():
    creat_table_despesa()
    conn, cursor = connect_despesa()
    cursor.execute("""SELECT * FROM DESPESAS; 
    """)
    conn.commit()
    lista=cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

def atualizar(descricao,data,valor, id):
    creat_table_despesa()
    conn, cursor = connect_despesa()
    cursor.execute(""" UPDATE DESPESAS SET DESCRICAO = ?, DATA_LANCAMENTO=?, VALOR = ? WHERE ID = ?""",
                   (descricao,data,valor,id))
    conn.commit()
    cursor.close()
    conn.close()



def deletarDespesa(id):
    creat_table_despesa()
    conn, cursor = connect_despesa()
    cursor.execute("""DELETE FROM DESPESAS WHERE ID=?""",(id,))
    conn.commit()
    cursor.close()
    conn.close()

def buscar(palavra):
    creat_table_despesa()
    conn, cursor = connect_despesa()
    cursor.execute(f"""SELECT * FROM DESPESAS 
        where descricao like '%{palavra}%' or DATA_LANCAMENTO like '%{palavra}%' """)
    conn.commit()
    lista = cursor.fetchall()
    cursor.close()
    conn.close()
    return lista

