#!/usr/bin/python3
"""make a request and get response in string format"""


import requests

if __name__ == "__main__":
   
    
    response = requests.get("https://alx-intranet.hbtn.io/status")       
    page = response.text
    # print(respons.headers)
    # print(type(respons.headers))
    print("Body response:")
    print("    - type:", type(page))
    print("    - content:",page)
