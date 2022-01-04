from flask import Flask 
from flask_restful import Api
from resources.user import RegisterUsers, Login
from resources.data import Data
from sql_alchemy import db
from flask_jwt_extended import JWTManager
from datetime import timedelta


app = Flask(__name__)

# Configuração de variaveis do SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# configuraçâo de variaveis do JWT
app.config['JWT_SECRET_KEY'] = 'secret' # Mude isso para um segredo escolhido por vc ou gerado aleatoriamente
app.config['JWT_ALGORITHM'] = 'HS512' # escolha um algoritimo de sua preferencia HS256 é o padrão, neste caso escolhi o HS512 = SHA512
app.config["JWT_DECODE_ALGORITHMS"] = 'HS512'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)


api = Api(app) 
db.init_app(app)
jwt = JWTManager(app)

# antes da primeira requisição cria se o banco de dados
@app.before_first_request
def create_db():
    db.create_all()



api.add_resource(Login,'/login') # rota para login e retorna um token
api.add_resource(RegisterUsers,'/login/register') # rota para se cadastrar usuarios
api.add_resource(Data,'/data') # rota para acessar os " dados do usuario "

if __name__ == '__main__':
    app.run(debug=True)
