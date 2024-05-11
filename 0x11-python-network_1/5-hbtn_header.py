#!/usr/bin/python3
"""make a request and get response in string format and print a header"""


import requests
import sys

if __name__ == "__main__":
   
    
    response = requests.get(sys.argv[1])       
    page = response.text
    print(response.headers['X-Request-Id'])
    # print(type(respons.headers))
