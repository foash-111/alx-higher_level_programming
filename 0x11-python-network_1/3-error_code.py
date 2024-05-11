#!/usr/bin/python3
"""make a request and get response and print header file
and handle errors connections"""


import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":

    try:
        with urllib.request.urlopen(sys.argv[1]) as respons:
            page = respons.read().decode('utf-8')
        # print(respons.headers)
        # print(type(respons.headers))
        print(page)
    except urllib.error.HTTPError as e:
            print("Error code:", e.code)
    # except urllib.error.URLError as e:
    #         print(e.reason)
