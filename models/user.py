from sql_alchemy import db
import hashlib

class UserModel(db.Model):
    __tablename__ = 'users'
    
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(128))
    
    def __init__(self,email,password):
        self.email = email
        self.password = password
        
    
    

           
        
                      