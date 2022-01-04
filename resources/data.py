from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt



class Data(Resource):
    """Classe Data herda recursos do modulo Resource

    Args:
        Resource (class): Uma classe que é herdada pela classe Data 

    """
    @jwt_required() # É requerido o token de acesso (JWT) gerado em /login
    def get(self):
        """Metodo get : para acessar é preciso que o usuario esteja logado

        Returns:
            Retorna um json com uma mensagem de acesso permitido para o {email} do usuario logado
        """
        jwt_email= get_jwt()['sub'] # busca no token de acesso a informação do email
        return {'mensage':f'Acesso permitido para {jwt_email["email"]}.'}