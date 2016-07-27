# encoding:utf-8

#################################################################################
#自定义区
#beautiful soup doc : http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#################################################################################
DEBUG = True #是否在调试
EXAMPLE_URL = 'http://www.mzitu.com/27236' #示例网址
HTML_ENCODING =None #返回的encoding,默认就好
IMAGE_DIR = 'image' #存放目录

def getTitle(soup): #获取标题,文件夹名
    #<h2 class="main-title"></h2>
    title = (soup.find_all("h2",class_ = "main-title"))[0].string
    return title

def getImgSrcs(soup): #如何获取本页的img src
    #<div class="main-body"><p><img src=
    imgs = soup.select(".main-body img")
    srcs = [img["src"] for img in imgs]
    return srcs

def has_next_page(soup): #还有下一页没啊
    #<div class="link_pages"> <a href=""><span>下一页</span></a></div>
    nav = soup.find("div",class_="link_pages")
    a = (nav.find_all('a'))[-1] #最后一个a标签
    return a.span and a.span.string == u'下一页'

def get_next_page(soup): #获取下一页地址
    #<div class="link_pages"> <a href=""><span>下一页</span></a></div>
    nav = soup.find("div",class_="link_pages")
    a = (nav.find_all('a'))[-1] #最后一个a标签
    return a["href"]
#################################################################################
#################################################################################



import urllib,sys,urllib2,os,sys
from bs4 import BeautifulSoup

#页面源码
def request(url,encoding=None):
    '''
    返回页面源码
    '''
    req = urllib2.Request(url) #Request
    res = urllib2.urlopen(req) #open->res
    page = res.read()

    if not encoding == None:
        #已指定encoding
        page = page.decode(encoding)

    return ''.join(page)
#写入一行
def writeLine(f,content):
    '''
    f = open()
    content : Unicode,use utf8 encode
    '''
    f.write(content.encode("utf8")+'\n')

if DEBUG:   #在debug,取example_url
    argUrl = EXAMPLE_URL
elif len(sys.argv) == 1: #正常运行时,提示帮助信息
    print(u"请指定图片所在网页(如{0})".format(EXAMPLE_URL))
    exit()
else:   #正常指定下载
    argUrl = sys.argv[1] #python [down.py http://xxxx]

soup = BeautifulSoup(request(argUrl)) #创建soup
title = getTitle(soup) #如何获取标题,只获取当前页
print(u"图片系列为 : {0}".format(title))


#image文件夹
if not os.path.exists(IMAGE_DIR):
    os.mkdir(IMAGE_DIR)
#子文件夹
if not os.path.exists(IMAGE_DIR + "/" + title):
    os.mkdir(IMAGE_DIR + "/" + title) #以title新建文件夹

index = 1 #第几张图片
def downImg(soup):
    srcs = getImgSrcs(soup) #如何获取本页的img src
    for src in srcs:
        #image/xxx-title/1.jpg
        global index #因为需要修改index值
        dot = src.rindex('.')
        ext = src[dot:] # .jpg
        path = u"{0}/{1}/{2:02}{3}".format(IMAGE_DIR,title,index,ext)
        print(u"正在下载第{0:02}张 : {1}".format(index,src))     
        urllib.urlretrieve(src,path)
        index+=1

downImg(soup) #下载本页的图片

#本页下载完成,点击下一页
while has_next_page(soup):
    next_url = get_next_page(soup) #获取下一页地址
    soup = BeautifulSoup(request(next_url)) #构建下一页的soup
    downImg(soup)