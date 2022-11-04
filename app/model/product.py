from app import db
from datetime import datetime
from app.model.category import Category_product

class Product(db.Model):
    kd      = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    nama    = db.Column(db.String(200), nullable = False)
    jumlah  = db.Column(db.BigInteger, nullable=False)
    harga   = db.Column(db.Float, nullable=False)
    kd_cat  = db.Column(db.BigInteger, db.ForeignKey(Category_product.kd_cat))
    
    def __repr__(self):
        return '<Product {}>'.format(self.nama)