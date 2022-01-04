# FLASK_API Doc

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



