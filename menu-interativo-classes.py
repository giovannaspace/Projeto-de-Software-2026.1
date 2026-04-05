#funcionalidade 1 - Perfil do usuário
#funcionalidade 2 - Catálogo de livros
#funcionalidade 3 - Biblioteca pessoal
#funcionalidade 4 - Adicionar resenha literária
#funcionalidade 5 - Categorizar livros
#funcionalidade 6 - Etiquetar livros
#funcionalidade 7 - Definir metas literárias
#funcionalidade 8 - Armazenar datas de início/fim de leituras
#funcionalidade 9 - Retrospectiva dos livros datados naquele ano
#funcionalidade 10 - Incentivo de leitura via e-mail

# CÓDIGO COM MENU PARA TESTE/SIMULAÇÃO DE FUNCIONALIDADES

# ESCONDER SENHA
import getpass

# CRIAÇÃO DE VENV PRA UTILIZAR BIBLIOTECA DE PROTEÇÃO DE SENHAS
from argon2 import PasswordHasher

# BIBLIOTECA PARA MANIPULAÇÃO DE DATAS
from datetime import datetime,timedelta


# SUPER CLASSE LIVRO -> PRESENTE NO CATÁLOGO DO MENU
class Livro:
    def __init__(self,nome,autor):
        self.nome = nome
        self.autor = autor

    #printar elementos dessa classe com esse formato
    def __str__(self):
        return f"TÍTULO: {self.nome}, AUTOR(A): {self.autor}"

   

# SUB CLASSE LIVROS DO USUARIO -> LIVROS SALVOS NA BIBLIOTECA DO USUÁRIO 
# INFORMAÇÕES A MAIS: ETIQUETA, DATAS DE INÍCIO E FIM DE LEITURA , NOTAS E RESENHAS
class Livros_Usuario(Livro):
    def __init__(self,livro,inicio_leitura = None,final_leitura = None,etiqueta=None,nota=None,resenha=None):  #parametro livro pra extrair nome e autor (infos primarias) 
        # reaproveitando (chamando) os atributos (informações do livro) da classe mãe e também a formatação da exibição (str):
        super().__init__(livro.nome,livro.autor)

        # atributos opcionais que podem ser adicionados depois pelo usuário
        self.etiqueta = etiqueta
        self.nota = nota
        self.inicio_leitura = inicio_leitura
        self.final_leitura = final_leitura
        self.resenha = resenha

    def adicionar_etiqueta(self,etiqueta):
        self.etiqueta = etiqueta # atualizar valor 
        print(f'Nova etiqueta para o livro "{self.nome}":  "{self.etiqueta}" ')

    def excluir_etiqueta(self):
        self.etiqueta = None

    def atribuir_nota(self,nota):
        self.nota = nota # atualizar valor 
        print(f"Nota: {self.nota}/5")

    def remover_nota(self):
        self.nota = None

    def escrever_resenha(self,resenha):
        self.resenha = resenha # atualizar valor 
        print("Resenha adicionada: ", self.resenha)

    def remover_resenha(self):
        self.resenha = None

    def data_inicio(self,inicio_leitura):
        #converter string informada pelo usuario para uma data 
        #self.inicio_leitura = input("Digite a data de início da leitura no formato DIA/MÊS/ANO: ")

        self.inicio_leitura = inicio_leitura # atualizar valor 
        self.inicio_leitura = datetime.strptime(self.inicio_leitura, "%d/%m/%Y").date() # retornar apenas data, sem a hora

    def data_final(self,final_leitura):
        #converter string informada pelo usuario para uma data 
       #self.final_leitura = input("Digite a data de término da leitura no formato DIA/MÊS/ANO: ")

        self.final_leitura = final_leitura # atualizar valor 
        self.final_leitura = datetime.strptime(self.final_leitura, "%d/%m/%Y").date() # retornar apenas data, sem a hora
    
    def ver_datas(self):
        print(f'Datas cadastradas para esse livro:\nInício de leitura:{self.inicio_leitura}\nFinal de leitura: {self.final_leitura}')


    def __str__(self):
        infos_classe_mae = super().__str__() # reaproveitando TITULO e AUTOR
        return f"{infos_classe_mae}, ETIQUETA: {self.etiqueta}, NOTA: {self.nota}, RESENHA: {self.resenha}, DATA INÍCIO: {self.inicio_leitura}, DATA FINAL: {self.final_leitura}"



#pastas = categorias
class Categoria:
    def __init__(self,nome):
        self.nome = nome
        self.livros_adicionados = []
      
    # CLASSE LIVROS DENTRO DA CATEGORIA
    def adicionar_livro(self,livro):
        livro_usuario = Livros_Usuario(livro)
        self.livros_adicionados.append(livro_usuario)
        return livro_usuario

    def retirar_livro(self,livro):
        self.livros_adicionados.remove(livro)

    # PRINTAR CONTEUDO DA CATEGORIA
    def printar_categoria(self):
        print(f'\nLivros na categoria: {self.nome}')
        for i in self.livros_adicionados:
            print(i)

    def __str__(self):
        return f"{self.nome}"


# api de livros (google livros é uma opção)
class Catalogo:
    def __init__(self):
        self.lista_catalogo = []  

    def montar_catalogo(self,livros):
        self.lista_catalogo.append(livros)

    def ver_infos(self):
        print("Livros no catálogo: ")
        for i in self.lista_catalogo:
            print(i)
        



class Biblioteca_Pessoal:
    def __init__(self):
        self.lista_livros = [] #LISTA DE CLASSE LIVROS ADICIONADOS
        self.lista_categorias = [] #LISTA DE CLASSE CATEGORIAS
        self.meta_literaria = []

    # ADICIONAR NO GERAL, SEM SER EM CATEGORIA
    def adicionar_livro(self,livro):
        #converter para SUBCLASSE para ADICIONAR MAIS INFORMAÇÕES 
        livro_usuario = Livros_Usuario(livro)
        self.lista_livros.append(livro_usuario)
        return livro_usuario

    def adicionar_categoria(self,categoria):
        categoria = Categoria(categoria)        
        self.lista_categorias.append(categoria)
        return categoria

    def excluir_categoria(self,categoria):
        #categoria = input("Digite a categoria que deseja excluir: ")
        self.lista_categorias.remove(categoria)

    def ver_infos(self):
        print("Livros na biblioteca: ")
        for i in self.lista_livros:
            print(i)

    # mostra os livros que estão em cada categoria
    def ver_pastas_conteudo(self):
        print("Aqui está sua biblioteca: ")
        for i in self.lista_categorias:
            print(f"Categoria {i}: ")
            for j in i.livros_adicionados: 
                print(f"Livro: {j}\n")
    

    def ver_categorias(self):
        print("Categorias: ")
        for i in self.lista_categorias:
            print(i)

    def retrospectiva(self,ano):
        retrospectiva_anual = []
        for i in self.lista_livros: 
            # se o ano de finalização esta cadastrado E é igual ao ano informado pelo usuário
            if i.final_leitura.year and i.final_leitura.year == ano:
                retrospectiva_anual.append(i)
        for j in retrospectiva_anual:  #j é o objeto livro
            print(j)


    def definir_meta(self,livro):
        self.meta_literaria.append(livro) # ja recebe o objeto livro do menu
        for i in self.meta_literaria:
            print("Desejo ler: ", i)




# CADASTRO
class Usuario:
    def __init__(self, nome,email,senha):
        self.nome = nome
        self.email = email
        self.__senha = senha # dois underlines para proteger o dado sigiloso do acesso em outras classes
        self.ph = PasswordHasher() # para que os metodos (login) possam acessar
        self.__senha = self.ph.hash(senha) # criptografar a senha


    def login(self,email_dado,senha_dada):
        if self.email == email_dado and self.ph.verify(self.__senha,senha_dada):

            self.ultimo_acesso = datetime.now()
            print("Login realizado!\n")

            print("Último acesso:",self.ultimo_acesso)
            return True 
        else:
            print("Senha ou e-mail incorretos")
            return False # não inicializa o menu

    def incentivo_leitura(self):
        # saber a quantos dias o usuario não faz login para enviar o incentivo
        diferenca_dias = datetime.now() - self.ultimo_acesso
        if diferenca_dias > timedelta(days=30):  #timedelta = duração do tempo
            pass #ENVIAR INCENTIVO POR EMAIL 
        # USAR smtplib 
        

 

if __name__ == "__main__":


    # LIVROS ESCOLHIDOS PARA O CATÁLOGO PARA EXEMPLO DE FUNCIONALIDADE
    livro1 = Livro("Romeu e Julieta", "William Shakespeare")
    livro2 = Livro("Crônicas de Nárnia", "C.S. Lewis")
    livro3 = Livro("Crime e Castigo", "Fiódor Dostoiévski")
    livro4 = Livro("The essence of software", "Daniel Jackson")
    livro5 = Livro("Estruturas de Dados em C", "Márcio Ribeiro")
    livro6 = Livro("Jujutsu Kaisen Vol 19", "Gege Akutami")


    catalogo = Catalogo()
    catalogo.montar_catalogo(livro1)
    catalogo.montar_catalogo(livro2)
    catalogo.montar_catalogo(livro3)
    catalogo.montar_catalogo(livro4)
    catalogo.montar_catalogo(livro5)
    catalogo.montar_catalogo(livro6)



    print("------------ Cadastro e Login de Usuário ------------\n")

    print("Seja bem-vindo(a) a sua estante! Para fazer o cadastro, utilize seu e-mail e defina seu nome de usuário e senha.\n")
    input_usuario = input("Digite seu nome de usuario: \n")
    input_email = input("Digite seu e-mail: \n")
    input_senha = getpass.getpass("Crie sua senha: \n")  

    usuario = Usuario(input_usuario,input_email,input_senha)

    print("Agora faça seu login para acessar as funcionalidades.\n")
    login_email = input("Digite seu e-mail: \n")
    login_senha = getpass.getpass("Digite sua senha: \n")  # falta mascarar a senha coom *

    checagem = usuario.login(login_email,login_senha)

    if not checagem:
        print("Erro ao inicializar menu.")

    else:
        #livro_adicionado = None # poder usar os atributos especificos no menu
        minha_biblioteca = Biblioteca_Pessoal()

        while True:

            print("Selecione o que deseja fazer: \n")

            opcao = float(input("Opção 1 - Mostrar Catálogo\nOpção 2 - Acessar Biblioteca Pessoal\n"))

            if opcao == 1:
                print("-------- Catálogo de Livros ----------\n")
                catalogo.ver_infos()
                print("\n")
                numero = int(input("Deseja adicionar livros na sua biblioteca?\nDigite o numero (1 a 6) do livro escolhido:"))

                if numero > 6:
                    print("Livro não encontrado.")
                    break
                
                novo_livro = catalogo.lista_catalogo[numero - 1]
                
                minha_biblioteca.adicionar_livro(novo_livro) 
               
            
            elif opcao == 2:
                print("----------- Biblioteca Pessoal ----------\n")  # categorias, etiqueta, nota, resenha
                # CHECAR SE ALGUM LIVRO FOI ADICIONADO NA BIBLIOTECA
                if not minha_biblioteca.lista_livros:
                    print("Aviso: Para conseguir utilizar as funcionalidades em um livro, adicione-o em sua biblioteca primeiro =)\n")
                    print("Nenhum livro foi adicionado ainda.\n")
                    break
                else:
                    minha_biblioteca.ver_infos()
                    print("\n")
                    print("Selecione o que deseja fazer: \n")
                    #print("Aviso: Para conseguir utilizar as funcionalidades em um livro, adicione-o em sua biblioteca primeiro =)\n")

                    opcao_interna = float(input("Opção 1 - Adicionar etiqueta em um livro\nOpção 2 - Adicionar avaliação em um livro\nOpção 3 - Adicionar resenha literária em um livro\nOpção 4 - Criar categoria\nOpção 5 - Preencher categoria\nOpção 6 - Add data de início\nOpção 7 - Add data finalização\nOpção 8 - Ver informações da biblioteca pessoal\nOpção 9 - Ver retrospectiva anual\nOpção 10 - Definir meta de leitura\nOpção 11 - Voltar para o menu\n"))
                   
                   #ETIQUETA
                    if opcao_interna == 1:
                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))
                        etiqueta_add = input("Digite sua nova etiqueta: \n" )

                        if livro > len(minha_biblioteca.lista_livros):
                            print("Livro não encontrado.")
                            break
                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        livro_escolhido.adicionar_etiqueta(etiqueta_add)

                    #AVALIAÇÃO
                    elif opcao_interna == 2:
                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))                        
                        nota_add = float(input("Digite sua avaliação: \n"))

                        if livro > len(minha_biblioteca.lista_livros):
                            print("Livro não encontrado.")
                            break

                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        livro_escolhido.atribuir_nota(nota_add)                        
                                              
                    #RESENHA
                    elif opcao_interna == 3:
                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))                         
                        resenha_add = input("Digite sua resenha literária: \n")

                        if livro > len(minha_biblioteca.lista_livros):
                            print("Livro não encontrado.")
                            break

                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        livro_escolhido.escrever_resenha(resenha_add)

                    #CATEGORIA
                    elif opcao_interna == 4:
                        nome_categoria = input("Digite a categoria que deseja criar: ")
                        nova_categoria = minha_biblioteca.adicionar_categoria(nome_categoria)
                        minha_biblioteca.ver_categorias()

                    #PREENCHER CATEGORIA
                    elif opcao_interna == 5:

                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))   
                        minha_biblioteca.ver_categorias() 
                        categoria_add = int(input("Digite o índice da categoria que deseja adicionar o livro: \n"))

                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        categoria_escolhida = minha_biblioteca.lista_categorias[categoria_add - 1]
                        
                        categoria_escolhida.adicionar_livro(livro_escolhido)
                        categoria_escolhida.printar_categoria()
                        minha_biblioteca.ver_pastas_conteudo()                    

                    #DATA DE INICIO
                    elif opcao_interna == 6:
                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))   
                        data_add = input("Digite a data de início de leitura no formato DD/MM/YYYY")

                        if livro > len(minha_biblioteca.lista_livros):
                            print("Livro não encontrado.")
                            break

                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        livro_escolhido.data_inicio(data_add)

                    #DATA DE FIM
                    elif opcao_interna == 7:
                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))                           
                        data_add = input("Digite a data de fim de leitura no formato DD/MM/YYYY: ")

                        if livro > len(minha_biblioteca.lista_livros):
                            print("Livro não encontrado.")
                            break

                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        livro_escolhido.data_final(data_add)

                    #VER TUDO DA BIBLIOTECA
                    elif opcao_interna == 8:
                        minha_biblioteca.ver_infos()

                    #RETROSPECTIVA ANUAL
                    elif opcao_interna == 9:
                        ano_escollhido = input("Informe o ano que você deseja ver a retrospectiva literária (formato YYYY): ")
                        minha_biblioteca.retrospectiva(int(ano_escollhido))

                    #DEFINIR META LITERÁRIA
                    elif opcao_interna == 10:
                        minha_biblioteca.ver_infos()
                        livro = int(input("Digite o numero (1 a 6) do livro escolhido (BIBLIOTECA): \n"))
                        if livro > len(minha_biblioteca.lista_livros):
                            print("Livro não encontrado.")
                            break

                        livro_escolhido = minha_biblioteca.lista_livros[livro - 1]
                        minha_biblioteca.definir_meta(livro_escolhido) 
