from flask_restful import Resource, reqparse
from models.user import UserModel
from werkzeug.security import safe_str_cmp
from flask_jwt_extended import create_access_token


attributes = reqparse.RequestParser() # Recebe  os argumentos passados cliente
attributes.add_argument('cpf',type=str,required=True,help='Invalid CPF number') # Recebe o argumento cpf como obrigatorio
attributes.add_argument('email', type=str, required=True, help='The field E-MAIL cannot be empty.')  # Recebe o argumento email como obrigatorio
attributes.add_argument('password',type=str, required=True, help='The field PASSWORD cannot be empty.')  # Recebe o argumento password como obrigatorio


class RegisterUsers(Resource):
    """Função Para Criar Usuarios Novos
    Args:
        Resource (classe): RegisterUsers Herda recursos da classe Resource
    """
    def post(self):
        """Metodo post onde se faz o registo de novos usuarios 
        a função requer header:
        
        Content-Type : application/json
        
        body:
            {
                "cpf":"<cpf_user>",
                "email":"<email_user>",
                "password":"<password_user>"
            }

        Returns:
            O metodo tem retornos diferentes de acordo com os dados passados em forma de json
        """
        data = attributes.parse_args()
        
        # Verifica a existencia de usuario com o email fornecido, se sim retorna uma Bad Request (400)
        if UserModel.find_by_email(data['email']): 
            return {'mensage':f'Address email: {data["email"]} is already registered.'},400 # Bad Request
        
        # Verifica a existencia de usuario com o cpf fornecido, se sim retorna uma Bad Request (400)
        if UserModel.find_by_cpf(data['cpf']):
            return {'mensage':f'Cpf number: {data["cpf"]} is already registered.'},400 # Bad Request
        
        user_hash = UserModel.generate_hash(data['password']) # Gera um hash da senha 
        user = UserModel(data['cpf'],data['email'],user_hash) # Cria se uma instancia do Usuario
        try:
            user.save_user() # Salva no banco a instancia de usuario criada 
            return {'mensage':f'User created successfully.'},201 # Created
        except:
            return {'mensage':'An error occurred while saving user.'},500 # Internal Server Error
                    
        
class Login(Resource):
    """Login herda recursos do Resource

    Args:
        Classe cotem o metodo post para que o usuario possa fazer login na aplicação

    """
    @classmethod
    def post(cls):
        """O metodo faz o login com um usuario e recebe um token de autenticação

        Returns:
        Caso de sucesso ao logar:
            Retorna token de autenticação jwt do tipo : 
            "Bearer <token_access>"

        Caso nao haja êxito no login:
            Retorna a respectiva mensagem informando o que houve
        """
        data = attributes.parse_args() # recebe os dados passados pelo usuario em formato json (cpf, email, senha)
        user = UserModel.find_by_cpf(data['cpf']) # busca opor um usuario com o cpf fornecido
        
        hash_passwd = UserModel.generate_hash(data['password'])# gera hash da senha para compara com a salva o banco de dados
        
        if user and safe_str_cmp(user.password, hash_passwd) and safe_str_cmp(user.email, data['email']): # verifica se exister o user ese senha e  email sao iguais ao salvos
            
            # dados do usuario atual para gerar o token
            payload = {
                "cpf":user.cpf,
                "email":user.email
            }
            
            # cria se um token com os dados do payload e e assinatura digital SHA-512 configurada em "app"
            access_token = create_access_token(identity=payload)
            return {'access_token':f'Bearer {access_token}'}, 200 #OK
            
        return {'mensage':'Login Failed'}, 401 #unauthorized