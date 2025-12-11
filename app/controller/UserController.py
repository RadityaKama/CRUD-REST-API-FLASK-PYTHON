from flask import request
from app.model.user import Users 
from app import response
from app import db

def index():
    try:
        users = Users.query.all() 
        
        data = format_array(users)
        return response.success(data, "Success mengambil data user")
        
    except Exception as e:
        print(e)
        return response.badRequest([], "Terjadi kesalahan")

def format_array(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data = {
        'id': data.id,
        'name': data.name,
        'email': data.email
    }
    return data

def show(id):
    try:
        users = Users.query.filter_by(id=id).first()
        
        if not users:
            return response.badRequest([], "Empty....")
        
        data = singleTransform(users)
        return response.success(data, "")
        
    except Exception as e:
        print(e)
        return response.badRequest([], "Terjadi kesalahan pada server")
    
def singleTransform(users):
    data = {
        'id': users.id,
        'name': users.name,
        'email': users.email
    }
    return data

def store():
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']
        
        users = Users(name=name, email=email)
        users.setPassword(password)
        db.session.add(users)
        db.session.commit()

        return response.success('', "Berhasil menambahkan data user")
    
    except Exception as e:
        print(e)
        return response.badRequest([], "Gagal menambahkan data user")
    
def update(id):
    try:
        name = request.json['name']
        email = request.json['email']
        password = request.json['password']

        users = Users.query.filter_by(id=id).first()
        users.email = email
        users.name = name
        users.setPassword(password)

        db.session.commit()

        return response.success('', "Berhasil mengupdate data user")
    
    except Exception as e:
        print(e)
        return response.badRequest([], "Gagal mengupdate data user")
    
def delete(id):
    try:
        users = Users.query.filter_by(id=id).first()
        if not users:
            return response.badRequest([], "Data user tidak ditemukan")
        
        db.session.delete(users)
        db.session.commit()

        return response.success('', "Berhasil menghapus data user")
    
    except Exception as e:
        print(e)
        return response.badRequest([], "Gagal menghapus data user")