from banco import *

class Usuarios(object):
  def __init__(self, idusuario = 0, nome = "", telefone = "", 
  email = "", usuario = "", senha = ""):
    #inicializando variaveis
    self.info = {}
    self.idusuario = idusuario
    self.nome = nome
    self.telefone = telefone
    self.email = email
    self.usuario = usuario
    self.senha = senha
   
  def insertUser(self):
    banco = Banco() #criando uma variavel para utilizar o metodo do Banco
    try:
   
        c = banco.conexao.cursor() #inicia a conexao do banco
   
        c.execute("insert into usuarios (nome, telefone, email, usuario, senha) values ('" + self.nome + "', '" + 
        self.telefone + "', '" + self.email + "', '" + 
        self.usuario + "', '" + self.senha + "' )")
   
        banco.conexao.commit() #faz os comandos digitados acima
        c.close() #fecha a conexao com o banco
   
        return "Usuário cadastrado com sucesso!"
    except:
        return "Ocorreu um erro na inserção do usuário"

  def updateUser(self):
    banco = Banco() #criando uma variavel para utilizar o metodo do Banco
    try:
   
        c = banco.conexao.cursor() #inicia a conexao do banco
   
        c.execute("update usuarios set nome = '" + self.nome + "', telefone = '" + self.telefone + "', email = '" + self.email
                  + "', usuario = '" + self.usuario + "', senha = '" + self.senha
                  + "' where idusuario = " + self.idusuario + " ")
   
        banco.conexao.commit() #faz os comandos digitados acima
        c.close() #fecha a conexao com o banco
   
        return "Usuário atualizado com sucesso!"
    except:
        return "Ocorreu um erro na alteração do usuário"
   
  def deleteUser(self):
    banco = Banco() #criando uma variavel para utilizar o metodo do Banco
    try:
   
        c = banco.conexao.cursor() #inicia a conexao do banco
   
        c.execute("delete from usuarios where idusuario = " + self.idusuario + " ")
   
        banco.conexao.commit() #faz os comandos digitados acima
        c.close() #fecha a conexao com o banco
   
        return "Usuário excluído com sucesso!"
    except:
        return "Ocorreu um erro na exclusão do usuário"
   
  def selectUser(self, idusuario):
    banco = Banco() #criando uma variavel para utilizar o metodo do Banco
    try:
   
        c = banco.conexao.cursor() #inicia a conexao do banco
   
        c.execute("select * from usuarios where idusuario = " + idusuario + "  ")
   
        for linha in c:
            self.idusuario = linha[0]
            self.nome = linha[1]
            self.telefone = linha[2]
            self.email = linha[3]
            self.usuario = linha[4]
            self.senha = linha[5]
   
        c.close() #fecha a conexao com o banco
   
        return "Busca feita com sucesso!"
    except:
        return "Ocorreu um erro na busca do usuário"
