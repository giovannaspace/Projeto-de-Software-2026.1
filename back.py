
from script import enviar_email

from abc import ABC,abstractmethod

# CRIAÇÃO DE VENV PRA UTILIZAR BIBLIOTECA DE PROTEÇÃO DE SENHAS
from argon2 import PasswordHasher

# BIBLIOTECA PARA MANIPULAÇÃO DE DATAS
from datetime import datetime,timedelta


class Livro:
    def __init__(self,numero,titulo,autor,sinopse):
        self.numero = numero
        self.titulo = titulo
        self.autor = autor
        self.sinopse = sinopse
        #self.capa = capa

    def __str__(self):
        return f'TÍTULO:{self.titulo}, AUTOR/A: {self.autor}'
    


# CLASSE ABSTRATA
class Leitura(ABC):
    def __init__(self,livro,inicio_leitura = None,final_leitura = None,etiqueta=None,nota=None,resenha=None):  #parametro livro pra extrair nome e autor (infos primarias) 

        self.etiqueta = etiqueta
        self.nota = nota
        self.inicio_leitura = inicio_leitura
        self.final_leitura = final_leitura
        self.resenha = resenha
        self.livro = livro # composiçao, recebe o objeto livro

# metodos concretos (subclasses herdam)
    def adicionar_etiqueta(self,etiqueta):
        self.etiqueta = etiqueta # atualizar valor 

    def excluir_etiqueta(self):
        self.etiqueta = None

    def atribuir_nota(self,nota):
        self.nota = nota # atualizar valor 

    def remover_nota(self):
        self.nota = None

    def escrever_resenha(self,resenha):
        self.resenha = resenha # atualizar valor 

    def remover_resenha(self):
        self.resenha = None

    def data_inicio(self,inicio_leitura):
        #converter string informada pelo usuario para uma data 

        self.inicio_leitura = inicio_leitura # atualizar valor 
        self.inicio_leitura = datetime.strptime(self.inicio_leitura, "%d/%m/%Y").date() # retornar apenas data, sem a hora

    def data_final(self,final_leitura):
        #converter string informada pelo usuario para uma data 

        self.final_leitura = final_leitura # atualizar valor 
        self.final_leitura = datetime.strptime(self.final_leitura, "%d/%m/%Y").date() # retornar apenas data, sem a hora
    

# metodos abstratos (cada subclasse vai implementar com suas diferenças)

    @abstractmethod
    def progresso_leitura(self,numero):
        pass
    

    def __str__(self):
        infos_classe_composicao = self.livro.__str__() # reaproveitando 
        return f"{infos_classe_composicao}, ETIQUETA: {self.etiqueta}, NOTA: {self.nota}, RESENHA: {self.resenha}, DATA INÍCIO: {self.inicio_leitura}, DATA FINAL: {self.final_leitura}"



class LivroFisico_Ebook(Leitura):
    def __init__(self,livro,total_paginas,pagina_atual=0, emprestado_para = None):
        super().__init__(livro)
        #self.livro = livro
        self.total_paginas = total_paginas
        self.pagina_atual = pagina_atual
        self.emprestado_para = emprestado_para


    def progresso_leitura(self,pagina):
        if pagina > 0 and pagina <= self.total_paginas: # checar se é valido
            self.pagina_atual = pagina
            porcentagem = (self.pagina_atual/self.total_paginas) * 100

            print(f"Progresso atualizado: {self.pagina_atual}/{self.total_paginas} ({porcentagem:.1f}%)")

            if self.pagina_atual >= self.total_paginas:
                self.finalizar_leitura()     
                print("Livro concluído!")  

            return porcentagem 


    def emprestar(self,pessoa):
        self.emprestado_para = pessoa
        
    def devolvido(self):
        self.emprestado_para = None
    
    def __str__(self):
        infos_mae = super().__str__()
        return f"{infos_mae}, PÁGINA ATUAL: {self.pagina_atual}/{self.total_paginas}, PROGRESSO: {self.calcular_porcentagem():.1f}%, EMPRESTADO PARA: {self.emprestado_para}"

class Audiobook(Leitura):
    def __init__(self,livro,narrador,tempo_total,nota_narracao = None, tempo_ouvido = 0):
        super().__init__(livro)
        #self.livro = livro
        self.tempo_total = tempo_total
        self.tempo_ouvido = tempo_ouvido
        self.narrador = narrador
        self.nota_narracao = nota_narracao


        # converter duracao_total de "HH:MM:SS" para segundos internamente
        duracao_convertida = datetime.strptime(tempo_total, "%H:%M:%S")
        self.tempo_total = (duracao_convertida.hour * 3600) + (duracao_convertida.minute * 60) + duracao_convertida.second


    def progresso_leitura(self,tempo):
        tempo_convertido = datetime.strptime(tempo, "%H:%M:%S")
        segundos_totais = (tempo_convertido.hour * 3600) + (tempo_convertido.minute * 60) + tempo_convertido.second

        if segundos_totais <= self.tempo_total: # se esta dentro do tempo
            self.tempo_ouvido = segundos_totais
            porcentagem = (self.tempo_ouvido/self.tempo_total) * 100

            print(f"Progresso atualizado: {porcentagem:.1f}%)")
            print(f"Tempo ouvido: {tempo} de {self.tempo_total}") 
            
            if self.tempo_ouvido >= self.tempo_total:
                self.finalizar_leitura()
                print("Audiobook concluído!")  
                 
            return porcentagem

    def avaliar_narracao(self,nota):
        self.nota_narracao = nota


    def __str__(self):
        infos_classe_mae = super().__str__()
        return f"{infos_classe_mae}, NARRADOR: {self.narrador}, NOTA DA NARRAÇÃO: {self.nota_narracao}, PROGRESSO: {self.calcular_porcentagem():.1f}%"




#pastas = categorias
class Categoria:
    def __init__(self,nome):
        self.nome = nome
        self.leituras_adicionadas = []
      
    # RECEBE O OBJETO LEITURA (QUE SERA LIVRO FISICO OU AUDIOBOOK)
    def adicionar_leitura(self, livro):
        self.leituras_adicionadas.append(livro)
        return livro

    def retirar_livro(self,livro):
        self.leituras_adicionadas.remove(livro)

    # PRINTAR CONTEUDO DA CATEGORIA
    def printar_categoria(self):
       # print(f'\nLivros na categoria: {self.nome}')
        return self.leituras_adicionadas
            

    def __str__(self):
        return f"{self.nome}"




class Biblioteca_Pessoal:
    def __init__(self):
        self.lista_leituras = [] #LISTA DE CLASSE LIVROS ADICIONADOS
        self.lista_categorias = [] #LISTA DE CLASSE CATEGORIAS
        self.meta_literaria_anual = []
        self.meta_literaria_mensal = []

    # ADICIONAR NO GERAL, SEM SER EM CATEGORIA
    def adicionar_leitura(self, livro, formato, total_paginas=None, narrador=None, tempo_total=None):
       # if formato == "Fisico/Ebook":
        if formato == 1:
            leitura = LivroFisico_Ebook(livro, total_paginas)
       # elif formato == "Audiobook":
        elif formato == 2:
            leitura = Audiobook(livro, narrador, tempo_total)
    
        self.lista_leituras.append(leitura)
        return leitura

    def ver_ordem_alfabetica(self):
        # sorted retorna uma lista ordenada
        # usar key lambda para ordenar pelo atributo título
        # leitura -> objeto LivroFisico ou Audiobook
        # leitura.livro -> objeto Livro dentro dele por composição
        return sorted(self.lista_leituras, key=lambda leitura: leitura.livro.titulo)

    def adicionar_categoria(self,categoria):
        categoria = Categoria(categoria)        
        self.lista_categorias.append(categoria)
        return categoria

    def excluir_livro(self, leitura):
        self.lista_leituras.remove(leitura)


    def ver_infos(self):
       # print("Livros na biblioteca: ")
       # for i in self.lista_leituras:
            #print(i)
        return self.lista_leituras
    

    # mostra os livros que estão em cada categoria
    def ver_pastas_conteudo(self):

        biblioteca = {}

       # print("Aqui está sua biblioteca: ")
        for i in self.lista_categorias:
           # print(f"Categoria {i}: ")
            biblioteca[i.nome] = i.leituras_adicionadas
        #for j in i.leituras_adicionados: 
                #print(f"Livro: {j}\n")
           # return j
        
        #retornar dicionario
        return biblioteca

    def ver_categorias(self):
        #print("Categorias: ")
        #for i in self.lista_categorias:
           #S print(i)
           # return i
        return self.lista_categorias
    

    def retrospectiva(self,ano):
        retrospectiva_anual = []
        for i in self.lista_leituras: 
            if i.final_leitura is not None:
            # se o ano de finalização esta cadastrado E é igual ao ano informado pelo usuário
                if i.final_leitura.year and i.final_leitura.year == ano:
                    retrospectiva_anual.append(i)
       # for j in retrospectiva_anual:  #j é o objeto livro
           # print(j)
          #  return j
        return retrospectiva_anual

# essa meta é a quantidade de livros 

    def definir_meta_anual(self,livro):
        self.meta_literaria_anual.append(livro) # ja recebe o objeto livro do menu
       # for i in self.meta_literaria_anual:
           # print("Desejo ler: ", i)
          #  return i
        return self.meta_literaria_anual

    def definir_meta_mensal(self,livro):
        self.meta_literaria_mensal.append(livro) # ja recebe o objeto livro do menu
       # for i in self.meta_literaria_mensal:
           # print("Desejo ler: ", i)
          #  return i
        return self.meta_literaria_mensal



# CADASTRO
class Usuario:
    def __init__(self, nome,email,senha):
        self.nome = nome
        self.email = email
        self.biblioteca_pessoal = []
        self.ultimo_acesso = None

        #encapsulamento
        self.__senha = senha # dois underlines para proteger o dado sigiloso do acesso em outras classes
        self.ph = PasswordHasher() # para que os metodos (login) possam acessar
        
        self.__senha = self.ph.hash(senha) # criptografar a senha

    # como a senha é privada, o property permite o banco de dados acessar a senha pelo property
    # acesso controlado
    @property 
    def senha(self):
        return self.__senha    


    def login(self,email_dado,senha_dada):
        if self.email == email_dado and self.ph.verify(self.__senha,senha_dada):

            self.ultimo_acesso = datetime.now()
           # print("Login realizado!\n")

           # print("Último acesso:",self.ultimo_acesso)
            return True 
        else:
         #   print("Senha ou e-mail incorretos")
            return False # não inicializa o menu

    def verificar_inatividade(self):   
        # saber a quantos dias o usuario não faz login para enviar o incentivo
        # evitar que o python faça subtração com None
        if self.ultimo_acesso is not None:
            diferenca_dias = datetime.now() - self.ultimo_acesso
            if diferenca_dias > timedelta(days=30):  #timedelta = duração do tempo
                enviar_email(self.email) # script smtplib
        
        

 

