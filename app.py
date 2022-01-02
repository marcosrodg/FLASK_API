from flask import Flask
from flask_restful import Api
#from resources.user import UserLogin
from resources.user import RegisterUsers
from sql_alchemy import db



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


api = Api(app)
db.init_app(app)

@app.before_first_request
def create_db():
    db.create_all()



#api.add_resource(UserLogin,'/login')
api.add_resource(RegisterUsers,'/login/register')

if __name__ == '__main__':
    app.run(debug=True)
