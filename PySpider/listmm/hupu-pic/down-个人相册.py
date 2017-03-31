
import urllib.request
from bs4 import BeautifulSoup

IMAGE_DIR = 'image'  # 存放目录
title = "test"
index = 1


def down_img(soup):
    '''ff'''
    srcs = get_img_srcs(soup)  # 如何获取本页的img src
    for src in srcs:
        # image/xxx-title/1.jpg
        global index  # 因为需要修改index值
        dot = src.rindex('.')
        ext = src[dot:]  # .jpg
        path = u"{0}/{1}/{2:02}{3}".format(IMAGE_DIR, title, index, ext)
        print(u"正在下载第{0:02}张 : {1}".format(index, src))
        urllib.request.urlretrieve('http:' + src, path)
        index += 1


def get_img_srcs(soup):  # 如何获取本页的img src
    '''s'''
    imgs = [soup.select(".tag a")[2].string]
    return imgs

# 页面源码


def request(url, encoding=None):
    '''
    返回页面源码
    '''
    # 如果不加上下面的这行出现会出现urllib.error.HTTPError: HTTP Error 403: Forbidden错误
    # 主要是由于该网站禁止爬虫导致的，可以在请求加上头信息，伪装成浏览器访问User-Agent,具体的信息可以通过火狐的FireBug插件查询
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    page = urllib.request.urlopen(req).read()

    if not encoding is None:
        # 已指定encoding
        page = page.decode(encoding)

    return ''.join(page)

ARG_URL = 'http://photo.hupu.com/soccer/p16178-1.html'
ARG_NUM = 36



URL_DOT = ARG_URL.rindex('.')
URL_SLASH = ARG_URL.rindex('-')

url = ''
print("go")

for i in range(1,36):
    url = ARG_URL[0:URL_SLASH+1]+str(i)+'.html'
    ss = BeautifulSoup(request(url, "GB2312"))  # 创建soup
    down_img(ss)
print("finished")
