from sql_alchemy import db
import hashlib

class UserModel(db.Model):
    __tablename__ = 'users'
    
    cpf = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String(128))
    
    def __init__(self,cpf,email,password):
        self.cpf = cpf
        self.email = email
        self.password = password
        
    def generate_hash(self,*args):
        word=''
        for arg in args:
            tmp=str(arg)
            word+=tmp
        m=hashlib.sha512()
        m.update(word.encode('utf-8'))
        return m.hexdigest()
    
    @classmethod
    def find_by_email(cls,email):
        user = cls.query.filter_by(email=email).first()
        if user :
            return user
        return None
    
    @classmethod
    def find_by_cpf(cls,cpf):
        user = cls.query.filter_by(cpf=cpf).first()
        if user :
            return user
        return None
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
    
           
        
                      