#__author__ = 'cm'
#! /usr/bin/python

import urllib2

def iopenurl(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()

if __name__ == '__main__':
    url = 'http://www.baidu.com'
    iopenurl(url)
