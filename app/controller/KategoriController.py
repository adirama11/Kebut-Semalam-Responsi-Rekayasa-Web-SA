from flask import request
from app.model import category
from app.model.category import Category_product
from app import response, app
from flask import request
from app import db

def index():
    try:
        kategori  = Category_product.query.all()
        data    = transform(kategori)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def transform(kategori):
    array   = []
    for i in kategori:
        array.append({
            'kd_cat': i.kd_cat,
            'category': i.category
        })
    return array

def show(id):
    try:
        kategori  = Category_product.query.filter_by(kd_cat=id).first()
        if not Category_product:
            return response.badRequest([], 'Empty....')
        data = singleTransfrom(kategori)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def singleTransfrom(kategori):
    data = {
        'kd_cat': kategori.kd_cat,
        'category': kategori.category
    }
    return data

def create():
    try:
        # kd_cat    = request.json['kd_cat']
        category    = request.json['category']
        
        kategori = Category_product(category=category)
        db.session.add(kategori)
        db.session.commit()
        
        return response.ok('', 'Succes create data!!!!!')
    except Exception as e:
        print(e)
        
def update(id):
    try:
        category    = request.json['category']
        
        kategori = Category_product.query.filter_by(kd_cat=id).first()
        kategori.category = category
        db.session.commit()
        
        return response.ok('', 'Succes Update Data!!!!')
    
    except Exception as e:
        print(e)
        
def delete(id):
    try:
        kategori = Category_product.query.filter_by(kd_cat=id).first()
        if not kategori:
            return response.badRequest([], 'Empty...')
        
        db.session.delete(kategori)
        db.session.commit()
        
        return response.ok('', 'Succes Delete Data!!!')
    except Exception as e:
        print(e)
