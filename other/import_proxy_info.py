#! /usr/bin/python3
import logging

http_proxy = '<PUT YOUR PROXY INFORMATION HERE>'
https_proxy = '<PUT YOUR PROXY INFORMATION HERE>'

my_proxy = {
    'http': http_proxy,
    'https': https_proxy
}

if __name__ == "__main__":
    logging.info(my_proxy)
