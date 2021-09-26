from django.test import TestCase
from .models import Customer


class CustomerTestCase(TestCase):
    url = "/customer/"
    def setUp(self):
        Customer.objects.create(firstName="Marko", lastName="Markovic", email="mail@gmail.com", subject="Problem", problemDescription="Problem with computer")
        
    def test_created_customer(self):
        customer = Customer.objects.get(email="mail@gmail.com")
        self.assertEqual(customer.lastName, 'Markovic')


    def test_post_customer(self):
        data = {
            'firstName': 'Sreten2',
            'lastName': 'Sretenovic3',
            'email': 'sreten1@gmail.com',
            'subject': 'Keyboard2',
            'problemDescription': 'Problem with keyboard1',
        }
        response = self.client.post(self.url, data=data)
        self.assertEqual(response.status_code, 302)

       
