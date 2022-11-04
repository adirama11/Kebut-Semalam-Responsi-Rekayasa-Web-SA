from datetime import timedelta
from flask import request
from app.model import todo, user
from app.model.user import Users
from app import response, app
from flask import request
from app import db
from flask_jwt_extended import*

def index():
    try:
        users = Users.query.all()
        data = transform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)


def transform(users):
    array = []
    for i in users:
        array.append({
            'id': i.id,
            'name': i.name,
            'email': i.email
        })
    return array

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], 'Empty....')
        data = singleTransform(users)
        return response.ok(data, "")
    except Exception as e:
        print(e)
        
def singleTransform(users, withTodo=True):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    if withTodo:
        todos = []
        for i in users.todos:
            todos.append({
                'id'            : i.id,
                'todo'          : i.todo,
                'description'   : i.description,
            })
        data['todos'] = todos
    return data

def store():
    try :
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()
        
        return response.ok('', 'Successfully create data!!!!')
    except Exception as e :
        print(e)
        
def update(id):#hapus id
    try:#id = request ke id
        name = request.json['name']#request.form
        email = request.json['email']
        password = request.json['password']
        
        user = Users.query.filter_by(id=id).first()# -> query.all()
        #user.id = id
        user.email = email
        user.name = name
        user.setPassword(password)#hilangkan setPass
        db.session.commit()
        
        return response.ok('', 'Succes Update Data!!!')
    
    except Exception as e:
        print(e)
        
def delete(id):
    try:
        user = Users.query.filter_by(id=id).first()
        if not user:
            return response.badRequest([], 'Empty...')
        
        db.session.delete(user)
        db.session.commit()
        
        return response.ok('', 'Succes Delete Data!!!')
    except Exception as e:
        print(e)
        
def login():
    try:
        email = request.json['email']
        password = request.json['password']
         
        user = Users.query.filter_by(email=email).first()
        if not user:
            return response.badRequest([], 'Empty....')
         
        if not user.checkPassword(password):
            return response.badRequest([], 'Your password is invalid')
        data = singleTransform(user, withTodo=False)
        expires=timedelta(days=1)
        expires_refresh= timedelta(days=3)
        acces_token= create_access_token(data, fresh=True, expires_delta=expires)
        refresh_token=create_refresh_token(data, expires_delta=expires_refresh)
        
        return response.ok({
            "data"  : data,
            "token_acces"   : acces_token,
            "token_refresh": refresh_token
        }, "")
    except Exception as e:
        print(e)
        
@jwt_required(refresh=True)
def refresh():
    try:
        user        = get_jwt_identity()
        new_token   = create_access_token(identity=user, fresh=False)
        
        return response.ok({
            "token_acces" : new_token
        }, "")
    except Exception as e:
        print(e)