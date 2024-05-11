#!/usr/bin/python3
"""make a request and get response and handle errors"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    response = requests.get("http://0.0.0.0:5000/search_user")
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    # print(type(respons.headers))
    else:
        data = response.json()
        print(type(data))
        print(data)


# ssh -o PasswordAuthentication=yes <ssh-key>
