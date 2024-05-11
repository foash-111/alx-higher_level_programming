#!/usr/bin/python3
"""make a request and get response and print header file
and handle errors connections"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as respons:
            page = respons.read().decode('utf-8')
        # print(respons.headers)
        # print(type(respons.headers))
        print(page)
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
