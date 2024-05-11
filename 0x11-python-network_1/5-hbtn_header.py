#!/usr/bin/python3
"""make a request and get response in string format and print a header"""


import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    page = response.text
    # print(response.headers['X-Request-Id'])
    # it's not safe, Directly accessing a dictionary
    # item using square brackets [] will raise a
    # KeyError if the key does not exist.
    # print(type(respons.headers))
    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)
