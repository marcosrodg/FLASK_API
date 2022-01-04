from sql_alchemy import db # importa a instancia do banco de dados
import hashlib 

class UserModel(db.Model):
    """Classe UserModel onde estao funções usadas por metodos de usuarios,
    podemos passar dados tipo (cpf,email,password) para que sejam moldados conforme a classe

    Tambem é a classe modelo para o banco de dados 'banco.db'
    
    """
    __tablename__ = 'users' # cria a tabela users
    
    cpf = db.Column(db.String(11), primary_key=True) # cria a coluna cpf como chave primaria
    email = db.Column(db.String(50)) # cria a coluna email
    password = db.Column(db.String(128)) # cria a coluna password
    
    def __init__(self,cpf,email,password):
        """ Metodo inicializadora da classe UserModel

        Args:
            cpf (str): Cpf fornecido pelo usuario
            email (str): email fornecido pelo usuario
            password (str): senha fornecida pelo usuario
        """
        self.cpf = cpf
        self.email = email
        self.password = password
    
    @classmethod
    def generate_hash(cls,passwd):
        """ Metodo da classe onde se gera um hash do passwd

        Args:
            passwd (str): string qualquer a ser trasnformada em hash 

        Returns:
            metodo retorna ao hash da senha
        """
        hash = hashlib.sha512( str( passwd).encode("utf-8") ).hexdigest()
        return hash
    
    @classmethod
    def find_by_email(cls,email):
        """Metodo procura usuario usando email como parametro

        Args:
            email (str): A função recebe o argumento email e procura por sua primeira ocorrencia no banco de dados

        Returns:
            Retorna o email encontrado ou None caso nenhuma ocorrencia
        """
        user = cls.query.filter_by(email=email).first()# filtra pelo primeiro usuario encontrado com este email
        if user : # encontrado o cpf retorna os dados do usuario encontrado
            return user
        return None
    
    @classmethod
    def find_by_cpf(cls,cpf):
        """Metodo procura usuario usando cpf como parametro

        Args:
            cpf (str): A função recebe o argumento cpf e procura por sua primeira ocorrencia no banco de dados

        Returns:
            Retorna o cpf encontrado ou None caso nenhuma ocorrencia
        """
        user = cls.query.filter_by(cpf=cpf).first() # filtra pelo primeiro usuario encontrado com este cpf
        if user : # encontrado o email retorna os dados do usuario encontrado
            return user
        return None
    
    def save_user(self):
        # uso: dados.save_user()
        db.session.add(self) # recebe a sessão da conexao aberta com o banco e salva o referido dado no banco de dados 
        db.session.commit() # commita o dado salvo no banco de dados 
        

           
        
                      