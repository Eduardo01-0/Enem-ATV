import sqlite3 

CAMINHOBANCO=""

def config(banco):
    global CAMINHOBANCO
    CAMINHOBANCO=banco
    
def Open():
    #Abre a conexao com o banco
    #Cria o arquivo do banco de dados 
    conexao = sqlite3.connect(CAMINHOBANCO) 

    #O codigo abaixo permite ler as colunas do banco
    #pelo nome!
    conexao.row_factory = sqlite3.Row
    return conexao

#Funcao para executar (UPDATE,DELETE,INSERT,ETCC..)
#TUDO MENOS SELECT !
def execute_non_query(sql):
    con = Open()
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()

#Funcao para executar query (consulta comando SELECT)
def execute_query(sql):
    con = Open()
    cursor = con.cursor()
    cursor.execute(sql)
    return cursor.fetchall()
    
