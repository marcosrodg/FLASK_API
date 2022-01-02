from flask import Flask
from flask_restful import Api
from resources.user import UserLogin



app = Flask(__name__)
api = Api(app)

api.add_resource(UserLogin,'/login')
