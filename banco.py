import sqlite3

class Banco():
 
    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')  #conecta com o banco
        self.createTable()                          #cria a tabela do banco

    def createTable(self):
        c = self.conexao.cursor()

        #codigo da tabela
        c.execute("""create table if not exists usuarios (
                     idusuario integer primary key autoincrement ,
                     nome text,
                     telefone text,
                     email text,
                     usuario text,
                     senha text)""")
        self.conexao.commit()   #ativa os comandos escritos
        c.close()               #fecha a conexao com o banco
