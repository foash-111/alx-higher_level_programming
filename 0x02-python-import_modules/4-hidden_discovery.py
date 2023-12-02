#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    arr = sorted(dir(hidden_4))
    for i in arr:
        if (i.startswith('__')):
            pass
        else:
            print("{}".format(i))

