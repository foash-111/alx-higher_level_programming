#!/usr/bin/python3
"""make a POST request and get response in string format"""


import requests
import sys

if __name__ == "__main__":
    form_data = {}
    form_data['email'] = sys.argv[2]
    response = requests.post(sys.argv[1], data=form_data)
    page = response.text
    print(page)
    # print(type(respons.headers))
