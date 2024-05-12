#!/usr/bin/python3
"""make a request and get response and handle errors"""


import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    my_data = {'q': q}
    response = requests.post("http://0.0.0.0:5000/search_user", data=my_data)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    # print(type(respons.headers))
    else:
        if response.headers.get('content-type').startswith('application/json'):
            data = response.json()
            if data.get('id') and data.get('name'):
                print('[' + data['id'] + ']', data['name'])
            else:
                print("No result")
        else:
            print("Not a valid JSON")
            data = response.text


# ssh -o PasswordAuthentication=yes <ssh-key>
