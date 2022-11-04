# from app import db
# from datetime import datetime

# class Users(db.Model):
#     id          = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
#     name        = db.Column(db.String(230), nullable = False)
#     email       = db.Column(db.String(120), index = True, unique = True, nullable = False)
#     password    = db.Column(db.String(128), nullable = False)
#     created_at  = db.Column(db.DateTime, default=datetime.utcnow)
#     update_at   = db.Column(db.DateTime, default=datetime.utcnow)
    
#     def __repr__(self):
#         return '<User {}>'.format(self.name)
    
# class Todos(db.Model):
#     id          = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
#     todo        = db.Column(db.String(140), nullable = False)
#     description = db.Column(db.Text, nullable=True)
#     created_ad  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     updated_ad  = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id     = db.Column(db.BigInteger, db.ForeignKey(Users.id))
    
#     def __repr__(self):
#         return '<Todo {}>'.format(self.todo)
    
# class Category_product(db.Model):
#     kd_cat    = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
#     category  = db.Column(db.String(20), nullable = False) 
    
#     def __repr__(self):
#         return '<Category_product {}>'.format(self.category)   
     
# class Product(db.Model):
#     kd      = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
#     nama    = db.Column(db.String(200), nullable = False)
#     jumlah  = db.Column(db.BigInteger, nullable=False)
#     harga   = db.Column(db.Float, nullable=False)
#     kd_cat  = db.Column(db.BigInteger, db.ForeignKey(Category_product.kd_cat))
    
#     def __repr__(self):
#         return '<Product {}>'.format(self.nama)