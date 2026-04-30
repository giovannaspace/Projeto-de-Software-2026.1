
# My Bookshelf - Etapa 1

Repositório para a disciplina de Projeto de Software  
Engenharia de computação - UFAL  
---

O banco de dados para a primeira parte do projeto começou a ser implementado para cadastro e login, pelo uso do **PostgreSQL** e hospedagem no **NeonConsole**. Para ter acesso à tabela gerada:
1. Acesse: [Neon Console](https://console.neon.tech/) e crie uma conta gratuitamente; 
2. Crie um novo projeto (banco de dados) para gerar uma `DATABASE_URL`; 
3. Utilize essa URL no seu arquivo **.env**. 

O script para envio do e-mail requer que você defina um e-mail **Gmail**  como remetente. Para isso, você precisará acessar/gerar sua senha de app (não é a senha da conta) em:
1. [Minha Conta - Google](myaccount.google.com)
2. Segurança -> Senhas de app   
- **Obs.:** A verificação em duas etapas precisa estar ativa.

Após isso, crie um arquivo nomeado **.env** na raiz do projeto e inclua suas variáveis:
```
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_SENHA=sua_senha_de_app
DATABASE_URL=url_criada_do_neon
```

**Após configurar os passos acima, execute:**  
1. `git clone <url do repositório>`  
2. `python -m venv venv`  
3.  - WSL/Linux/Mac -> `source venv/bin/activate`  
    - Windows -> `venv\Scripts\activate`  

4.`pip install -r requirements.txt`  
5.`python main.py`  