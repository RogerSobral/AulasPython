# -*- coding:utf-8 -*-

import sqlite3 as sq

def conector():
    conn= sq.connect("appfinanceiro.db")
    cursor=conn.cursor()

    return conn, cursor

def criarTabelaUsuario():
    conn, cursor=conector()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuario(
    id INTEGER  PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    senha TEXT NOT NULL,
    telefone TEXT NOT NULL
    );
    """)
    conn.commit()
    cursor.close()
    conn.close()


def addUsuario(nome,senha,telefone):
    criarTabelaUsuario()
    conn, cursor = conector()
    cursor.execute("""
    INSERT INTO usuario (nome,senha, telefone) 
    VALUES(?,?,?);
    """,(nome,senha,telefone))
    conn.commit()
    cursor.close()
    conn.close()
    print("Add usuario com sucesso!")





addUsuario("MARIA","123","(11)93445-4545")