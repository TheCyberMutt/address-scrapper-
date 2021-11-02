import requests
from requests import get
from bs4 import BeautifulSoup

# Usefule if you run loop on URL list to keep data organized
# import pandas as pd 
# import numpy as np

example_url = "https://stores.footlocker.com/us/mt/billings/300-south-24th-st-w.html"

phone_number = []
address = []
zipcode = []


def get_the_address(url):
    results = requests.get(url)

    soup = BeautifulSoup(results.text, "html.parser")

    location = soup.find('div', class_='Core-address')
    number = soup.find('div', class_='Core-phone')

    phone = number.find('a', class_="Phone-link")
    num = BeautifulSoup(phone.text, "html.parser")
    phone_number.append(num)

    postal = location.find('span', class_="c-address-postal-code")
    postalcode = BeautifulSoup(postal.text, 'html.parser')
    zipcode.append(postalcode)
    
    street = location.find('span', class_="c-address-street-1")
    street_address = BeautifulSoup(street.text, "html.parser")
    address.append(street_address)
    

get_the_address(example_url)

# Use these to test that you have the correct tags 
# print(phone_number)
# print(zipcode)
# print(address)
