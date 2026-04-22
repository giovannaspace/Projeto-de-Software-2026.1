import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conexao = psycopg2.connect(os.getenv("DATABASE_URL"))


cursor = conexao.cursor() # cursor é responsavel por ler os comandos e executar no bd

def cadastro_bd(usuario):
    cursor.execute("""CREATE TABLE IF NOT EXISTS perfis_usuarios (
               id SERIAL NOT NULL PRIMARY KEY,
               nome_usuario TEXT NOT NULL,
               email_usuario TEXT NOT NULL UNIQUE,
               senha_usuario TEXT NOT NULL,
                ultimo_acesso TEXT
               )""")
    cursor.execute("""INSERT INTO perfis_usuarios
               (nome_usuario,email_usuario,senha_usuario,ultimo_acesso) VALUES
               (%s,%s,%s,%s)""",(usuario.nome,usuario.email,usuario.senha,None))


    conexao.commit()


def login_bd(string_email):
    # buscar email na tabela para verificação da senha no backend
    # FILTRA pelo email e ARMAZENA senha ligada a ele
    cursor.execute("""SELECT senha_usuario FROM perfis_usuarios WHERE email_usuario = (%s)""",(string_email,))
    busca = cursor.fetchone() # serve como ponteiro,cursor nas linhas da tabela
    if not busca: #se a busca pelo email falhar (query falhar) fetchone retorna a linha (tupla com infos) como None
        return False
    else: # retorna a senha cadastrada pra comparar com a senha dada pelo usuário
        return busca[0] # indice da TUPLA retornada por fetchone(), tupla que contem apenas um elemento (senha)

def ultimo_acesso_bd(usuario):
    #atualiza coluna do ultimo acesso
    cursor.execute("""UPDATE perfis_usuarios SET ultimo_acesso = %s WHERE email_usuario = %s""", (usuario.ultimo_acesso,usuario.email))
    conexao.commit()
    return usuario.ultimo_acesso

# antes de sobrescrever, compara o ultimo acesso armazenado
def comparar_ultimo_acesso_bd(string_email):
    cursor.execute("""SELECT ultimo_acesso FROM perfis_usuarios WHERE email_usuario = %s"""), (string_email)
    resultado = cursor.fetchone()
    # se o email existe (nao for None) e o ultimo acesso existir (ultimo acesso é o elemento da tupla (de um elemento) retornada por fetchone)
    if resultado and resultado[0]:
        return resultado[0] # data salva 
    return None

