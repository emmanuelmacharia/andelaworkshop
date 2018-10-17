
import unittest
from views import app



#remember to change the urls for these methods
class TestProductApis(unittest.Testcase):
     salemade = {
         'saleid':1, 'products':{'milk': 200, 'sugar': 300, 'dogfood': 2500, 'carrots': 100, 'tomatoes': 50}, 'total': 3150
         }
     newsale = {
         'saleid':1, 'product': 'Hp', 'quantity': 1, 'price': 5000
         }

     datapoint = {
          'name':'milk', 'description':'Tuzo 500ml', 'category':'food and drinks', 'price': 100
           }

     def setUp(self):
        self.app = app.test_client()



     def test_get_admin_products(self):
        '''Tests the get (view all) products method, asserts true if the test passes and gives a status code of 200'''
        response = self.app.AdminProducts.get('http://localhost:50931/')
        self.assertEqual(response.status_code, 200)

     def test_get_attendant_products(self):
        '''Tests the get (view all) products method for the attendant, asserts true if the test passes and gives a status code of 200'''
        response = self.app.AttendantProducts.get('http://localhost:50931/')
        self.assertEqual(response.status_code, 200)

     def test_get_admin_sales(self):
        '''Tests the get (view all) sales method for the admin, asserts true if the test passes and gives a status code of 200'''
        response = self.app.AdminSales.get('http://localhost:50931/')
        self.assertEqual(response.status_code, 200)

     def test_get_attendant_sales(self):
        '''Tests the get (view all) sales method by the attendant for the attendant, assets true if the test passes and gives the status code of 200'''
        response = self.app.AttendantSales.get('http://localhost:50931/')
        self.assertEqual(response.status_code, 200)

     def test_post_products(self):
        '''Tests whether the admin can create a new product successfully; (POST method); asserts true if the test passes and gives a status code of 201'''
       
        response = self.app.AdminProducts.post('http://localhost:50931/', data = json.dumps(datapoint), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

     def test_post_sales(self):
        '''Tests whether the attendant can successfully create a new sale record (POST method); asserts true if the test passes and status code = 201'''
        
        response = self.app.AttendantSales.post('http://localhost:50931/', data = json.dumps(salemade), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)

     def test_single_sale_found(self):
        '''Tests whether the sale with the id provided is there, returns status_code 404'''
       
        response = self.app.AttendantSales.post('http://localhost:50931/', data = json.dumps(salemade), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = app.AdminSingleSale.get('http://localhost:50931/<int')
        self.assertEqual(response.status_code, 200)

     def test_single_product(self):
        '''Tests for the get function to view a single product'''
        response = self.app.AdminProducts.post('http://localhost:50931/', data = json.dumps(datapoint), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        response = app.Products.get('http://localhost:50931/')
        self.assertEqual(response.status_code, 200)

     def test_no_product_found(self):
        '''Tests for non existent items'''
        response = app.Products.get('http://localhost:50931/')
        self.assertEqual(response.status_code, 404)

     def tearDown(self):
        self.app = app.test_client()



if __name__ == '__main__':
    unittest.main(exit = False)
