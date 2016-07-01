#!/usr/bin/env python
#coding=utf8

import http.client
import urllib

import urllib.request

httpClient = None

#url = "http://172.16.11.177:8050/api/values"

#ip = '172.16.11.177'
#port = 8050

ip = 'localhost'
port = 5245


def Get(httpClient):
	httpClient.request('GET', '/api/employees?department=4')
	return httpClient.getresponse()

def Post(httpClient):
	values = {"FirstName":"sss","LastName":"ddd","Department":"5"}
	data = urllib.parse.urlencode(values)
	data = data.encode('utf-8')

	#url = "http://localhost:5245/api/employees"
    url = ip + ":" + port + "/api/employees"
	return urllib.request.urlopen(url,data)


try:
    httpClient = http.client.HTTPConnection(ip, port, timeout=30)

    #²»Í¬·½·¨µ÷ÓÃ
    response = Get(httpClient)

    print(response.status)
    print(response.reason)
    print(response.read().decode("utf-8"))
except Exception as e:
    print(e)
finally:
    if httpClient:
        httpClient.close()

