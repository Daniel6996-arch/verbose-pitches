from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch:
    '''
    Pitch class to define Pitch Objects
    '''

    def __init__(self,content,author,upvote,downvote ):
        self.content = content
        self.author = author
        self.upvote = upvote
        self.downvote = downvote
        
class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255))
    pitch_id = db.Column(db.Integer,db.ForeignKey('newpitches.id'))

    @property
    def password(self):
        raise AttributeError('You cannnot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")



    def __repr__(self):
        return f'User {self.username}'

class PitchAdd(db.Model):
    __tablename__ = 'newpitches'

    id = db.Column(db.Integer,primary_key = True)
    author = db.Column(db.String(255),index = True)
    pitch = db.Column(db.String(1000),index = True)   
    users = db.relationship('User',backref = 'newpitches',lazy="dynamic")

    def __repr__(self):
        return f'User {self.username}'
