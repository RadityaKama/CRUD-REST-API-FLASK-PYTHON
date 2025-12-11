from app.model.product import Product
from app.response import success, badRequest
from app import db
from flask import request

def index():
    try:
        products = Product.query.all()
        data = format_array(products)
        return success(data, "Success list products")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def store():
    try:
        name = request.json['name']
        harga = request.json['harga']  # <-- Ambil 'harga'
        desc = request.json['description']
        cat_id = request.json['category_id']
        
        # Masukkan ke kolom 'harga'
        product = Product(name=name, harga=harga, description=desc, category_id=cat_id)
        
        db.session.add(product)
        db.session.commit()
        return success(single_object(product), "Success add product")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def update(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
             return badRequest([], "Product empty")

        product.name = request.json['name']
        product.harga = request.json['harga'] # <-- Update kolom 'harga'
        product.description = request.json['description']
        product.category_id = request.json['category_id']
        
        db.session.commit()
        return success(single_object(product), "Success update product")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

def delete(id):
    try:
        product = Product.query.filter_by(id=id).first()
        if not product:
            return badRequest([], "Product not found")
            
        db.session.delete(product)
        db.session.commit()
        return success('', "Success delete product")
    except Exception as e:
        print(e)
        return badRequest([], "Error")

# --- Helper Functions ---
def format_array(datas):
    array = []
    for i in datas:
        array.append(single_object(i))
    return array

def single_object(data):
    return {
        'id': data.id,
        'name': data.name,
        'harga': data.harga, # <-- Tampilkan 'harga'
        'description': data.description,
        'category_id': data.category_id
    }