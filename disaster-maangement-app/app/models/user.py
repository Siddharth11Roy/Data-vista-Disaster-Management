
from .. import db
from flask_login import UserMixin

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    username=db.Column(db.String(80),unique=True,nullable=False)
    email=db.Column(db.String(120),unique=True,nullable=False)
    phone=db.Column(db.String(20),unique=True,nullable=False)
    password=db.Column(db.String(120),nullable=False)
    def __repr__(self):
        return f"<User {self.username}>"


#UserMixin
#gives model default implementations for methods like is_authenticated,is_active,is_anonymous,get_id()