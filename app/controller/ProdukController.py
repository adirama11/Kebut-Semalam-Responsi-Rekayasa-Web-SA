from flask import request
from app.model import product
from app.model.product import Product
from app import response, app
from flask import request
from app import db

def index():
    try:
        produk  = Product.query.all()
        data    = transform(produk)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def transform(produk):
    array   = []
    for i in produk:
        array.append({
            'kd'    : i.kd,
            'nama'  : i.nama,
            'jumlah': i.jumlah,
            'harga' : i.harga,
            'kd_cat': i.kd_cat
        })
    return array

def show(id):
    try:
        produk  = Product.query.filter_by(kd=id).first()
        if not product:
            return response.badRequest([], 'Empty....')
        data = singleTransfrom(produk)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def singleTransfrom(produk):
    data = {
        'kd'    : produk.kd,
        'nama'  : produk.nama,
        'jumlah': produk.jumlah,
        'harga' : produk.harga,
        'kd_cat': produk.kd_cat
    }
    return data

def create():
    try:
        nama    = request.json['nama']
        jumlah  = request.json['jumlah']
        harga   = request.json['harga']
        kd_cat  = request.json['kd_cat']
        
        produk = Product(nama=nama, jumlah=jumlah, harga=harga, kd_cat=kd_cat)
        db.session.add(produk)
        db.session.commit()
        
        return response.ok('', 'Succes create data!!!!!')
    except Exception as e:
        print(e)
        
def update(id):
    try:
        nama    = request.json['nama']
        jumlah  = request.json['jumlah']
        harga   = request.json['harga']
        kd_cat  = request.json['kd_cat']
        
        produk = Product.query.filter_by(kd=id).first()
        produk.nama     = nama
        produk.jumlah   = jumlah
        produk.harga    = harga
        produk.kd_cat   = kd_cat
        db.session.commit()
        
        return response.ok('', 'Succes Update Data!!!!')
    
    except Exception as e:
        print(e)
        
def delete(id):
    try:
        produk = Product.query.filter_by(kd=id).first()
        if not produk:
            return response.badRequest([], 'Empty...')
        
        db.session.delete(produk)
        db.session.commit()
        
        return response.ok('', 'Succes Delete Data!!!')
    except Exception as e:
        print(e)