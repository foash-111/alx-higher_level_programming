#!/usr/bin/python3
"""make a request and get response"""


import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    try:
        with urllib.request.urlopen(req) as respons:
            page = respons.read()
        print("Body response:")
        print("\t- type:", type(page))
        print("\t- content:", page)
        print('\t- utf8 content:', page.decode('utf-8'))
        # print(type(respons.headers))
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
