from flask import request
from app import app
from app.controller import UserController
from app.controller import CategoryController, ProductController

@app.route('/')
def index():
    return "Halaman Home: Server Berjalan!"

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'GET':
        return UserController.index()
    else:
        return UserController.store()

@app.route('/users/<id>', methods=['GET', 'PUT', 'DELETE'])
def userDetail(id):
    if request.method == 'GET':
        return UserController.show(id)
    elif request.method == 'PUT':
        return UserController.update(id)
    elif request.method == 'DELETE':
        return UserController.delete(id)
    
@app.route('/categories', methods=['GET', 'POST'])
def categories():
    if request.method == 'GET':
        return CategoryController.index()
    else:
        return CategoryController.store()
    
@app.route('/categories/<id>', methods=['GET', 'PUT', 'DELETE'])
def category_detail(id):
    if request.method == 'GET':
        return CategoryController.show(id) 
    elif request.method == 'PUT':
        return CategoryController.update(id)
    elif request.method == 'DELETE':
        return CategoryController.delete(id)
    
@app.route('/products', methods=['GET', 'POST'])
def products():
    if request.method == 'GET':
        return ProductController.index()
    else:
        return ProductController.store()

@app.route('/products/<id>', methods=['GET', 'PUT', 'DELETE'])
def product_detail(id):
    if request.method == 'GET':
        return ProductController.index() 
    elif request.method == 'PUT':
        return ProductController.update(id)
    elif request.method == 'DELETE':
        return ProductController.delete(id)