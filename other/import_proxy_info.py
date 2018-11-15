#! /usr/bin/python3

http_proxy  = '<PUT YOUR PROXY INFORMATION HERE>'
https_proxy = '<PUT YOUR PROXY INFORMATION HERE>'

myProxy = {
        'http': http_proxy,
        'https': https_proxy
        }

if __name__ == "__main__":
    print(myProxy)
