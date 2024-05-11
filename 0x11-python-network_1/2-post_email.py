#!/usr/bin/python3
"""make a POST request and get response and print header file"""


import urllib.request, urllib.parse
import sys

if __name__ == "__main__":
    #data as a dict
    data = {'email' : sys.argv[2]}
    #encoding data <like a serialize>
    data = urllib.parse.urlencode(data)
    # make a request with data and '?' as a swparator between url and query,
    #name=value&name=value in url after ? called query 
    req = urllib.request.Request(sys.argv[1] + '?' + data)
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
