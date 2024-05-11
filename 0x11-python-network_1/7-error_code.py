#!/usr/bin/python3
"""make a request and get response and handle errors"""


import requests
import sys

if __name__ == "__main__":
   
    response = requests.get(sys.argv[1])
    if response.status_code >= 400:     
        print("Error code:", response.status_code)
    # print(type(respons.headers))
    
