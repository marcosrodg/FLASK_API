from flask import Flask
from flask_restful import Api
#from resources.user import UserLogin
from resources.user import RegisterUsers, Login
from resources.data import Data
from sql_alchemy import db
from flask_jwt_extended import JWTManager



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret' # Mude isso
app.config['JWT_ALGORITHM'] = 'HS512'



api = Api(app)
db.init_app(app)
jwt = JWTManager(app)


@app.before_first_request
def create_db():
    db.create_all()



api.add_resource(Login,'/login')
api.add_resource(RegisterUsers,'/login/register')
api.add_resource(Data,'/data')

if __name__ == '__main__':
    app.run(debug=True)
