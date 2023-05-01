from unittest import mock
from pytest_mock import MockFixture
import random

import requests

from monapp.example2 import get_random_pizzas


def test_get_pizzas_returns_correct_names(monkeypatch):
    product1, product2 = products = ['My product 1', 'My product 2']
    #mock pour requests.get()
    class MockResponse:
        status_code = 200

        def json(self):
            return {
                "products": [
                    {"product_name": product1}, 
                    {"product_name": product2}
                ]

            }

    def mock_get(self, *args, **kwargs):
        return MockResponse()
    
    #mock pour random.sample
    def mock_sample(liste, k):
        return liste[:k]

    #monkey patching de requests.get
    monkeypatch.setattr('requests.get', mock_get)
    
    """ backup_requests_get = requests.get
    requests.get = mock_get """

    #monkey patching de random.sample
    monkeypatch.setattr("random.sample", mock_sample)

    """ backup_sample = random.sample
    random.sample = backup_sample """

    assert get_random_pizzas(2) == products

    """ result = get_random_pizzas(2)
    assert result == [product1, product2] """

    #Faire le ménage
    """ requests.get = backup_requests_get
    random.sample = backup_sample """


""" def test_get_pizzas_returns_correct_names_with_mock(monkeypatch):
    product1, product2 = products = ['My product 1', 'My product 2']

    #Mock pour requests.get()
    mock_get = mock.MagicMock()
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "products": [{"product_name": product} for product in products]
    }
    
    #Autre façon de mocker sans MagicMock
    mock_get = requests.get("unfauxurl")
    mock_response = requests.get(" http://unfauxurl") #Faux requests get
    mock_response.status_code = 200
    #mock_get.status_code = 200 #requests.get.status_code

    
    #Mock pour requests.sample()
    mock_sample = mock.MagicMock
    mock_sample.return_value = products[:2]
    #mock pour requests.get()
    
    
    #monkey patching de requests.get
    monkeypatch.setattr('requests.get', mock_get)

    #monkey patching de random.sample
    monkeypatch.setattr("random.sample", mock_sample)

    assert get_random_pizzas(2) == products """



def test_get_pizzas_returns_correct_names_with_mocker(mocker):
    product1, product2 = products = ['My product 1', 'My product 2']

    #Mock pour requests.get()
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "products": [{"product_name": product} for product in products]
    }
    
    """ mock_get = requests.get("unfauxurl")
    mock_response = requests.get(" http://unfauxurl") #Faux requests get
    mock_response.status_code = 200 """
    #mock_get.status_code = 200 #requests.get.status_code

    #Mock pour requests.sample()
    mock_sample = mocker.patch('random.sample')
    mock_sample.return_value = products[:2]
    #mock pour requests.get()


    assert get_random_pizzas(2) == products
