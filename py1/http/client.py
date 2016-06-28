#!/usr/bin/env python
#coding=utf8

import http.client

httpClient = None

try:
    httpClient = http.client.HTTPConnection('localhost', 46010, timeout=30)

    # httpClient.request('POST', '/api/account/register')
    # #response是HTTPResponse对象
    # response = httpClient.getresponse()
    # print(response.status)
    # print(response.reason)
    # print(response.read())

    httpClient.request('GET', '/api/values')

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