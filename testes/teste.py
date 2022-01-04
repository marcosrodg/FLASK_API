
# Consumindo a Api usando python

import requests


headers_user = {'Content-Type':'application/json'} # header da requisição
route = 0

def body(cpf,email,password):
    """[summary]

    Args:
        cpf (str): Recebe um numero de cpf do usuario
        email (str): Recebe um endereço de email do usuario
        password (str): Recebe a senha do usuario

    Returns:
        json: retorna dados em formato json
    """
    return {
        'cpf': f'{cpf}',
        'email': f'{email}',
        'password': f'{password}'
    }

while route != 4:
    URL = 'http://0.0.0.0:5000' # caso seja uma rota diferente mude isso!
    
    # preciso informar o numero do endpoint que deseja acessar
    route = int(input("""\nACESSAR ENDPOINT: 
                [1] - /login/register
                [2] - /login
                [3] - /data
                [4] - exit
                
                >>> """))

    # Acessa o endpoint /login/register
    if route  == 1:
        cpf = str(input("Informe o cpf: "))
        email = str(input("Informe o email: "))
        password = str(input("Informe o password: "))
        
        body_cadastro = body(cpf, email, password)
        
        URL+='/login/register'# incrementa a url
            
        r = requests.post(URL,json=body_cadastro,headers=headers_user) # faz a requisião a api
        print(r.json()) # retorno da requisicao espera se : {'mensage':f'User created successfully.'}
        print(r.status_code) # status da requisição
        
        print('\n Corrigir dados informados')

    elif route == 2:
        
        cpf = str(input("Informe o cpf: "))
        email = str(input("Informe o email: "))
        password = str(input("Informe o password: "))
        
        body_cadastro = body(cpf, email, password) # cchama a função body que retorna json dos dados
        
        URL+='/login'
        
        
        r = requests.post(URL,json=body_cadastro,headers=headers_user) # faz a requisião a api
        print('\n')
        print('Copie todo o dicionario abaixo:')
        print('\n')
        print(r.json()) # retorno da requisicao espera se algo do tipo: {'access_token':f'Bearer {access_token}'}
        print(r.status_code) # status da requisição
        
        
    elif route == 3:
        
        access_token = str(input("Informe o Token de acesso:")) # requer um dicionario com o access token
        URL+='/data' # incrementa a url
        
        try:
            headers_user = {'Content-Type':'application/json',
                        'Authorization':access_token.split("'")[3].replace('}','')} # Header da requisião a api
        except:
            print('Formato de tokenn invalido') # precisa informar um dicionario recebido /login
        finally:
            r = requests.get(URL,headers=headers_user)
            print('\n')
            print(r.json()) #retorno da requisição espera se algo do tipo : {"message": "Acesso permitido para {e-mail do usuário}"}
            print(r.status_code) # status da requisição
        
    else:
        print('\n Endpoint não encontrado') # informe  apenas 1 , 2 ou 3 


    
