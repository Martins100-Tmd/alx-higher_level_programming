#!/usr/bin/python3
'''
Write a python script that fetches
a url
'''
if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status')as Info:
        obj = Info.read()
        obj_d = obj.decode("utf-8")

        print("Body response:")
        print("\t- type: {}".format(type(obj)))
        print("\t- content: {}".format(obj))
        print("\t- utf8 content: {}".format(obj_d))
