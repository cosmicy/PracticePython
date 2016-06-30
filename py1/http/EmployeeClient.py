#!/usr/bin/env python
#coding=utf8

import http.client
import urllib
from urllib import request

httpClient = None



def Get(httpClient):
	httpClient.request('GET', '/api/employees?department=4')
	return httpClient.getresponse()

def Post(httpClient):
	values = {"FirstName":"sss","LastName":"ddd","Department":"3"}
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8')

	url = "http://localhost:5245/api/employees"

	return request.urlopen(url,data)


try:
    httpClient = http.client.HTTPConnection('localhost', 5245, timeout=30)

    response = Post(httpClient)

    print(response.status)
    print(response.reason)
    print(response.read().decode("utf-8"))
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()

