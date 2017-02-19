
import urllib.request

IMAGE_DIR = 'image' #存放目录
title = "test"
index = 1

def downImg():
    srcs = getImgSrcs() #如何获取本页的img src
    for src in srcs:
        #image/xxx-title/1.jpg
        global index #因为需要修改index值
        dot = src.rindex('.')
        ext = src[dot:] # .jpg
        path = u"{0}/{1}/{2:02}{3}".format(IMAGE_DIR,title,index,ext)
        print(u"正在下载第{0:02}张 : {1}".format(index,src))
        urllib.request.urlretrieve(src,path)
        index+=1

# http://724.169pp.net/169mm/201612/068/36.jpg

# http://724.169pp.net/169mm/201608/189/1.jpg
# http://724.169pp.net/169mm/201608/189/50.jpg

def getImgSrcs():
    srcs = []
    time = '201702';
    cat = '102';
    total = 45;
    url = 'http://724.169pp.net/169mm/'
    for i in range(1,total+1):
        pass
        urlsrc = url + time + '/' + cat + '/' + str(i)+ '.jpg'
        srcs.append(urlsrc)
    return srcs

print("go")
downImg()
print("finished")