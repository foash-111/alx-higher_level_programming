#!/usr/bin/python3
"""make a request and get response"""


import urllib.request

if __name__ == "__main__":
    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    try:
        with urllib.request.urlopen(req) as respons:
            page = respons.read()
        print("Body response:")
        print("    - type:", type(page))
        print("    - content:", page)
        print('    - utf8 content: OK')
        print(type(respons.headers))
    except urllib.error.URLError as e:
        if hasattr(e, 'reason'):
            print(e.reason)
        elif hasattr(e, 'code'):
            print(e.code)
