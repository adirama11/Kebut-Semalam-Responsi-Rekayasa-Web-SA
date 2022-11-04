from app import db
from datetime import datetime
# from app.model import user
from app.model.user import Users
# from ..routes import users

class Todos(db.Model):
    id          = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    todo        = db.Column(db.String(140), nullable = False)
    description = db.Column(db.Text, nullable=True)
    created_ad  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    updated_ad  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id     = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    users       = db.relationship("Users", backref="user_id")
    token_acces = db.Column(db.Text, nullable=True)
    token_refresh= db.Column(db.Text, nullable=True)
    
    def __repr__(self):
        return '<Todo {}>'.format(self.todo)