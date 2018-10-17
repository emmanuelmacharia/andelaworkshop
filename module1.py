from flask import Flask, request
from flask_restful import Api, Resource

app  = Flask(__name__)
api = Api(app)


products = {}

class AdminProducts(Resource):
    '''Endpoints for creating and viewing products in the application'''

    def get(self):
        '''Views all the products in the application'''
        return jsonify({'products':products})

    def post(self):
        '''Creates a new product in the store'''
        id = len(products)+1
        data = request.get_json()
        name = data['name']
        description = data['description']
        category = ['category']
        price = ['price']

        payload = {'name': name, 'description': description, 'category': category, 'price': price}

        products[id] = payload

        return orders, 201

class AttendantProducts(Resource, AdminProducts):
    '''endpoints for viewing all the products in the inventory by the attendant'''
    def get(self):
         super().post(self)


sales ={}
class AttendantSales(Resource):
    '''endpoint for creating and viewing sales'''
    def get(self):
        '''views all sales made by the attendant'''
        return jsonify({'sales':sales})

    
    def post(self):
        '''Creates a new sale by the attendant'''
        id = len(sales)+1
        data = request.get_json()
        price = data['price']
        quantity = data['quantity']
        productname = data['productname']
        description = data['description']

        payload = {'product':productname, 'description': description, 'quantity': quantity , 'price': price}
        sales[id] = payload

        return sales, 201


class Product(Resource):
    '''Endpoint that allows a user to view a single product'''

    def get(self, id):
        '''view a single product'''
        if id in products:
            return products[AdminProducts.id], 200
        return 404

        
class Sale(Resource):
    '''Endpoint for viewing a single sale'''
    def get(self):
        '''views single sale'''
        if id not in sales:
            return 404
        else:
            return sales[id] ,200


api.add_resourse(AdminProducts, '/admin/products')
api.add_resourse(AdminProducts, '/attendant/products')
api.add_resourse(AttendantSales, '/attendant/sales')
api.add_resourse(Sale, '/admin/sales/<int:id>')
api.add_resource(Product, '/products/<int:id>')
