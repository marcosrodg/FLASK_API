from flask_restful import Resource, reqparse
from models.user import UserModel

attributes = reqparse.RequestParser()
attributes.add_argument('cpf',type=int,required=True,help='The field cpf  cannot be empty.')
attributes.add_argument('email', type=str, required=True, help='The field email cannot be empty.')
attributes.add_argument('password',type=str, required=True, help='The field password cannot be empty.')


class Register(Resource):
    
    def post(self):
        data = attributes.parse_args()
        
        if UserModel.find_by_email(data['email']):
            return {'mensage':f"Address email '{data['email']}' is already registered."}
        
        user_hash = UserModel.generate_hash(data['password'])
        user = UserModel(data['cpf'],data['email'],user_hash)
        try:
            user.save_user()
            return {'mensage':f'User created successfully.'},201 # Created
        except:
            return {'mensage':'An error occurred while saving user.'},500 # Internal Server Error
                    
        
        