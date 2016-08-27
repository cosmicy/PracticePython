# encoding:utf-8

#################################################################################
#自定义区
#beautiful soup doc : http://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html
#################################################################################
DEBUG = False #是否在调试
EXAMPLE_URL = 'http://dp.pconline.com.cn/photo/list_2450419.html' #示例网址
HTML_ENCODING =None #返回的encoding,默认就好
IMAGE_DIR = 'image' #存放目录

def getTitle(soup): #获取标题,文件夹名
    #<div class="dTitInfo"><strong class="yh" title="明泰手机特约+烟火的季节">
    return soup.find('div',class_="dTitInfo").strong["title"]
def getImgSrcs(soup): #如何获取本页的img src
    #span.pic img alt="明泰手机特约+烟火的季节" src=
    #xx1364406470921_mthumb.jpg"
    imgs = soup.select("span.pic img")

    srcs = []
    for img in imgs:
        src = img["src"]
        _index = src.rindex('_mthumb')
        src = src[:_index] + src[_index+7:] #去掉_mthumb
        srcs.append(src)
    return srcs
#################################################################################
#################################################################################



import urllib,sys,urllib2,os,sys,time
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

soup = BeautifulSoup(request(argUrl,'gbk')) #创建soup    
title = getTitle(soup) #如何获取标题,只获取当前页
print(u"图片系列为 : {0}".format(title))

#image文件夹    
if not os.path.exists(IMAGE_DIR):
    os.mkdir(IMAGE_DIR)

#子文件夹
if not os.path.exists(IMAGE_DIR + "/" + title):
    os.mkdir(IMAGE_DIR + "/" + title) #以title新建文件夹    


#########################
#说明文件
intro = soup.find("div",class_="authorBrief")
intro_path = u"{0}/{1}/说明.txt".format(IMAGE_DIR,title)
f = open(intro_path,'w')
'''
http://xxx
标题
时间

'''
f.write(argUrl.encode("utf8")+"\n")
f.write(title.encode("utf8")+"\n")
#time http://www.cnblogs.com/wanpython/archive/2010/08/07/1794598.html
f.write(time.strftime("%Y-%m-%d %H:%M:%S").encode('utf8')+'\n')
f.write("\n")
for s in intro.strings:
    f.write(s.encode('utf8')+"\n")
f.close()
#########################


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