# from crypt import methods
from flask import Flask, render_template, url_for, redirect
from flask import request
from app import app
from app.model import user
from app.model.user import Users
from app.model.product import Product
from app.controller import KategoriController, ProdukController, TodoController, UserController

# @app.route('/login', methods=['POST'])
# def login():
#     return UserController.login()

# @app.route('/users', methods = ['POST', 'GET'])
# def users():
#     if request.method == 'GET':
#         return UserController.index()
#     else:
#         return UserController.store()
        

# @app.route('/users/<id>', methods = ['PUT', 'GET', 'DELETE'])
# def usersDetail(id):
#     if request.method == 'GET':
#         return UserController.show(id)
#     elif request.method == 'PUT':
#         return UserController.update(id)
#     elif request.method == 'DELETE':
#         return UserController.delete(id)
    
# @app.route('/todo', methods = ['POST', 'GET'])
# def todo():
#     if request.method == 'GET':
#         return TodoController.index()
#     else:
#         return TodoController.store()
        

# @app.route('/todo/<id>', methods = ['PUT', 'GET', 'DELETE'])
# def todoDetail(id):
#     if request.method == 'GET':
#         return TodoController.show(id)
#     elif request.method == 'PUT':
#         return TodoController.update(id)
#     elif request.method == 'DELETE':
#         return TodoController.delete(id)
    
  
# @app.route('/kategori', methods = ['POST', 'GET'])
# def Kategori():
#     if request.method == 'GET':
#         return KategoriController.index()
#     else:
#         return KategoriController.create()
        

# @app.route('/kategori/<id>', methods = ['PUT', 'GET', 'DELETE'])
# def KategoriDetail(id):
#     if request.method == 'GET':
#         return KategoriController.show(id)
#     elif request.method == 'PUT':
#         return KategoriController.update(id)
#     elif request.method == 'DELETE':
#         return KategoriController.delete(id)
    
# @app.route('/produk', methods = ['POST', 'GET'])
# def Produk():
#     if request.method == 'GET':
#         return ProdukController.index()
#     else:
#         return ProdukController.create()
        

# @app.route('/produk/<id>', methods = ['PUT', 'GET', 'DELETE'])
# def ProdukDetail(id):
#     if request.method == 'GET':
#         return ProdukController.show(id)
#     elif request.method == 'PUT':
#         return ProdukController.update(id)
#     elif request.method == 'DELETE':
#         return ProdukController.delete(id)
    
# @app.route("/refreesh", methods=['POST'])
# def refresh():
#     return UserController.refresh()

@app.route('/')
def index():
    return render_template('dasboard.html')

@app.route('/produk')
def produk():
    return render_template('produk.html')
    
@app.route('/kontak')
def kontak():
    return render_template('kontak.html')

@app.route('/form_barang')
def formBeli():
    return render_template('form_beli.html')

@app.route('/form_daftar')
def formDaftar():
    return render_template('form_daftar.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and 'inpEmail' in request.form and 'inpPass' in request.form:
        email = request.form['inpEmail']
        password = request.form['inpPass']

        user = Users.query.filter_by(email=email, password=password).first()

        if user:
            return redirect(url_for('admin'))

        if not user:
            # flash('Login gagal, cek kembali email dan password Anda.')
            return redirect(url_for('login'))
    else:
        return render_template('index.html')

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/produk_admin")
def product():
    product = Product.query.all()
    return render_template('product.html',product=product)

@app.route("/data_plg")
def dataPlg():
    plg = Users.query.all()
    return render_template('pelanggan.html', plg = plg)

@app.route('/contact')
def ContactUS():
    return render_template('contact.html')