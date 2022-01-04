# FLASK_API DOCUMETAÇÃO


* ## Preparando o Ambiente para Executando a Api


Clone ou faça o Download do repositorio em uma pasta em sua maquina
abra a pasta raiz da aplicação em um editor de texto de sua preferência e execute os comandos:

Antes de qualquer coisa **certifique que tenha o python3 instaldo em sua maquina** executando o camando ``$ python3 --version`` (linux), caso não tenha siga as instruções do <www.python.org/downloads/>.


Após a instalação do python digite os comandos:

``$ python3 -m venv .venv``


``$ source .venv/bin/activate``


``$ pip install requirements.txt``


**PARA EXECUÇÃO EM localhost:5000** padrão flask

``$ flask run``


**PARA EXECUÇÃO EM 0.0.0.0:<port docker>** 
 
 
Caso não tenha o docker na maquina host instale o Docker em : <https://docs.docker.com/get-docker/> .

 
Crie uma conta no Docker Hub <https://hub.docker.com/> .
 
 
Na pasta raiz do projeto execute as instruções:

 
``$ docker pull python:3.9.9-bullseye``
 
 
``$ docker build -t flask-app:dev-0.0.1 .``
 
 
``$ docker run -d -P flask-app:dev-0.0.1``
 

Verifique a execução do conteiner:

``$ docker ps``

Caso seu conteiner estiver executando corretamente copie a porta de execução para consumir a Api.

 
 
* ## Consumindo Api
 

### Usando o Postman para fazer requisições


Instale o Postman  em <www.postman.com/downloads/> .Após isso crie um 'workspace' e crie as seguintes rotas:


* ``/login``


* ``/data``


* ``/login/register``

Agora basta seguir as '**Instruções de Uso**' para fazer as requisições.


### Usando o testes/teste.py para fazer requisições

Na pasta raiz da aplicação abra um terminal e digite as seguites instruções:

``$ cd testes``


``$ python3 teste.py``


E siga as interações do script.

**ATENÇÃO: Mude a variavel URL caso a api esteja em um conteiner ou outro servidor.**




* # Instruções de Uso

Este documento explicita com exemplos, como utilizar os recursos disponíveis no FLASK API de login, acesso de dados, e registro. Assim como, as formas de se realizar uma requisição e suas possíveis respostas.

## 1. Registro:


***Requisição***
 
Exemplo de Requisição cadastrar um novo usuário.

|**Method**   | **URL**                          |
|-------------|----------------------------------|
|   POST      |  /login/register                 | 



|**Header**         |                            |
|-------------------|----------------------------|
|  Content-Type     |  application/json          | 


|**Request Body**                                                                        |
|----------------------------------------------------------------------------------------|
 ```json 
      {
      "cpf":"11111111111",
      "email":"documentacao@email.com", 
      "password":"secret"
      }
  ```
  

***Resposta***


Como resposta, obtém-se uma mensagem de sucesso informado que usuário foi criado, e status code 201 Created (Criado).


|**Status**         | **Response Body**                                   |
|-------------------|-----------------------------------------------------|
|  201 Created      |  ```{"mensage":"User created successfully"} ```     | 



***Requisição***
 
Exemplo de Requisição cadastrar outro usuario com cpf e/ou email ja existentes.

|**Method**   | **URL**                          |
|-------------|----------------------------------|
|   POST      |  /login/register                 | 



|**Header**         |                            |
|-------------------|----------------------------|
|  Content-Type     |  application/json          | 


|**Request Body**                                                                        |
|----------------------------------------------------------------------------------------|
 ```json 
      {
      "cpf":"11111111111",
      "email":"documentacao@email.com", 
      "password":"secret"
      }
  ```
  

***Resposta***


Como resposta, obtém-se uma mensagem de erro, informando que um usuário com o email ou cpf ja existe.


Caso exista usuario ja cadastrado com o email:


|**Status**             | **Response Body**                                                                      |
|-----------------------|----------------------------------------------------------------------------------------|
|  400 Bad Request      |  ```{"mensage":"Address email: documentação@email.com is already registered."} ```     | 


Caso exista usuario ja cadastrado com o cpf:


|**Status**             | **Response Body**                                                                      |
|-----------------------|----------------------------------------------------------------------------------------|
|  400 Bad Request      |  ```{"mensage":"Cpf number: 11111111111 is already registered."} ```                   |


## 2. Login de Usuário


***Requisição***


Exemplo de Requisição logar com um usuário.


|**Method**   | **URL**                          |
|-------------|----------------------------------|
|   POST      |  /login                          | 


|**Header**         |                            |
|-------------------|----------------------------|
|  Content-Type     |  application/json          | 


|**Request Body**                                                                        |
|----------------------------------------------------------------------------------------|
 ```json 
      {
      "cpf":"11111111111",
      "email":"documentacao@email.com", 
      "password":"secret"
      }
  ```
  

***Resposta***


Como resposta, obtém-se uma mensagem o token de acesso que será necessário para fazer as requisições que só podem ser feitas com login ou pode ocorrer algum erro do servidor ao gerar o token.



|**Status**             | **Response Body**                                                                      |
|-----------------------|----------------------------------------------------------------------------------------|
|  200 OK               |  ```{"access_token": "Bearer                                  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY0MTMxMzg0MywianRpIjoiNWI0ZTJmZTEtN2U0MC00OWI1LWJiMTMtOTBjMjdjZTA4ZmZmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6eyJjcGYiOiIwMDAwMDAwMDAwMCIsImVtYWlsIjoiZG9jdW1lbnRhXHUwMGU3XHUwMGUzb0BlbWFpbC5jb20ifSwibmJmIjoxNjQxMzEzODQzLCJleHAiOjE2NDEzMTc0NDN9.MLokeR2UG8M-QWxKnfhU_mF7mZJ8zvXs74kMrLLK9__wupRra3_E7SWmSsFlpMuKtddG_QyzFOFo0K4TX3Jkvw"} ```                                 | 
| 500 INTERNAL SERVER ERROR | ```{'mensage':'Login Failed:Internal Server Error '}```                            |         


***Requisição***


Exemplo de Requisição para tentar fazer login com um usuário que não existe..


|**Method**   | **URL**                          |
|-------------|----------------------------------|
|   POST      |  /login                          | 


|**Header**         |                            |
|-------------------|----------------------------|
|  Content-Type     |  application/json          | 


|**Request Body**                                                                        |
|----------------------------------------------------------------------------------------|
 ```json 
      {
      "cpf":"cpf_que_nao_existe",
      "email":"email_que_nao_existe", 
      "password":"secret"
      }
  ```
  

***Resposta***


Como resposta, obtém-se uma mensagem de erro 401 não autorizado, informando que cpf ou email estão incorretos.



|**Status**             | **Response Body**                 |
|-----------------------|-----------------------------------|
|  401 OK               | ```{"mensage": "Login Failed"}``` |


## 3.Acessar Dados

***Requisição***

|**Method**   | **URL**                          |
|-------------|----------------------------------|
|   POST      |  /data                           | 


|**Header**         |                            |
|-------------------|----------------------------|
|  Content-Type     |  application/json          |
| Authorization     |  Bearer {token_de_acesso}  |


***Resposta***

Exemplos de Respostas: primeiro, a mensagem de sucesso com a mensagem de acesso permitido.Depois a mensagem de token
expirado,neste caso sera preciso gerar outro token, eles tem duração de 1 hora depois que são gerados.Outra mensagem possivel sera a solicitação de um header caso o usuario nao tenha fornecido.

|**Status**             | **Response Body**                                              |
|-----------------------|----------------------------------------------------------------|
|  200 OK               | ```{"message": "Acesso permitido para {e-mail do usuário}"}``` |
|  401 UNAUTHORIZED     | `` {"msg": "Token has expired"}``                              |
|  401 UNAUTHORIZED     |  ``"msg": "Missing Authorization Header"``                     |



