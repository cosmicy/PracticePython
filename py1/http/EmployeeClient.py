#!/usr/bin/env python
#coding=utf8

import http.client

httpClient = None

try:
    httpClient = http.client.HTTPConnection('localhost', 5245, timeout=30)
    httpClient.request('GET', '/api/employees?department=4')

    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print(response.status)
    print(response.reason)
    print(response.read().decode("utf-8"))
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()