from app.model.category import Category
from app import db
from flask import request
from app.response import success, badRequest 

def index():
    try:
        categories = Category.query.all()
        data = format_array(categories)
        return success(data, "Success list categories")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def store():
    try:
        name = request.json['name']
        category = Category(name=name)
        db.session.add(category)
        db.session.commit()
        return success(single_object(category), "Success add category")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def update(id):
    try:
        name = request.json['name']
        category = Category.query.filter_by(id=id).first()
        
        if not category:
             return badRequest([], "Category not found")

        category.name = name
        db.session.commit()
        return success(single_object(category), "Success update category")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def delete(id):
    try:
        category = Category.query.filter_by(id=id).first()
        if not category:
            return badRequest([], "Category not found")
            
        db.session.delete(category)
        db.session.commit()
        return success('', "Success delete category")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def format_array(datas):
    array = []
    for i in datas:
        array.append(single_object(i))
    return array

def single_object(data):
    return {'id': data.id, 'name': data.name}