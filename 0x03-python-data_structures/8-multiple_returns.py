#!/usr/bin/python3

def multiple_returns(sentence):
    #if (sentence is not None): //if it's = "" will be true and that's wrong
    if (sentence): # if sentence is  "" or 'None'  will be false
        return (len(sentence), sentence[0])
    else:
        return (0, "")
