#!/usr/bin/env python
# coding=utf-8

import http.client

httpClient = http.client.HTTPConnection('localhost', 26591, timeout=30)
httpClient.request('GET', '/hellocyworld/welcome?s=fff&num=3')

# response是HTTPResponse对象
response = httpClient.getresponse()
print(response.status)
print(response.reason)
print(response.read().decode("utf-8"))
