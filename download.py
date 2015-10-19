# coding=gbk
import urllib,urllib2
import cookielib
import re
def Down(url,typeid):
    try:
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
                'Referer':'http://www2.ahnu.edu.cn/ftp/eftphelp.htm'
            }
        req = urllib2.Request(url,headers=headers)
        opener.open(req)

        url = 'http://210.45.192.104/userOperator.do?flag=queryClassify&typeid='+typeid
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
                'Referer':'http://210.45.192.104'
            }
        req = urllib2.Request(url,headers=headers)
        rlt = (opener.open(req)).read()
        rule = 'title="(.*?)"'
        lst = re.findall(rule,rlt)
        for i in xrange(len(lst)):
            print i,lst[i]
        fileid = raw_input('请输入所要下载资源的序号:\n')

        rule = 'href="/down(.*?)"'
        urlst = re.findall(rule,rlt)

        rule = 'id=(.*)'
        s = urlst[int(fileid)]
        loadid = re.findall(rule,s)        
        urlnew = 'http://210.45.192.104/downOrLookFile.do?flag=downloadfile&fileid='+loadid[0]
        #print urlnew
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:41.0) Gecko/20100101 Firefox/41.0',
                'Referer':'http://210.45.192.104/userOperator.do?flag=queryClassify&typeid='+typeid
            }
        req = urllib2.Request(urlnew,headers=headers)
        rlt = opener.open(req)

        print urlst[int(fileid)]
        #print rlt.read()

        print '开始下载，请耐心等待......'
        filename = 'F:\\校园网络资源下载\\'
        name = lst[int(fileid)].decode('utf-8').encode('gbk')

        f = open(filename+name,'wb')
        f.write(rlt.read())
    except Exception,e:
        print str(e)

if __name__ == '__main__':
    while 1:
        #Down('http://210.45.192.104')
        hintstr = '''-------------------------
类型id：
1:电影
2:视频资源
3:音乐
4:文档
5:电视剧
-------------------------'''
        print hintstr
        typeid = raw_input('请输入所要下载资源的类型id：\n')
        if typeid == '5':
            typeid = '6'
        Down('http://210.45.192.104',typeid)
        print '下载完毕!'
        flag = raw_input('是否继续下载？y/n\n')
        if flag!='y':
            break
