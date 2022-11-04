from app import db
from datetime import datetime

class Category_product(db.Model):
    kd_cat    = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    category  = db.Column(db.String(20), nullable = False) 
    
    def __repr__(self):
        return '<Category_product {}>'.format(self.category)   
     