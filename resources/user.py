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
        Classe faz ologin com um usuario e recebe um token de autenticação

    """
    @classmethod
    def post(cls):
        
        data = attributes.parse_args() # recebe os dados passados pelo usuario em formato json (cpf, email, senha)
        user = UserModel.find_by_cpf(data['cpf']) # busca opor um usuario com o cpf fornecido
        
        hash_passwd = UserModel.generate_hash(data['password'])# gera hash da senha para compara com a salva o banco de dados
        
        if user and safe_str_cmp(user.password, hash_passwd) and safe_str_cmp(user.email, data['email']): # verifica se exister o user ese senha e  email sao iguais ao salvos
            access_token = create_access_token(identity=user.email+user.password) # gera um token com o email e o cpf(chave primaria)
            return {'access_token': access_token}, 200 #OK
            
        return {'mensage':'Login Failed'}, 401 #unauthorized