#!/usr/bin/env python
#coding=utf8

import http.client

httpClient = None

try:
    httpClient = http.client.HTTPConnection('localhost', 5248, timeout=30)
    httpClient.request('GET', '/api/values')

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print(response.status)
    print(response.reason)
    print(response.read())
except(Exception, e):
    print(e)
finally:
    if httpClient:
        httpClient.close()