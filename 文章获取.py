# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 22:47:40 2018

@author: Administrator
"""

import requests,re

url=['http://www.qqenglish.com/bn/bn/','http://www.qqenglish.com/bn/business/',\
'http://www.qqenglish.com/bn/technology/','http://www.qqenglish.com/bn/education/',\
'http://www.qqenglish.com/bn/culture/','http://www.qqenglish.com/bn/science/',\
'http://www.qqenglish.com/bn/opinion/']
header={"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}
for j in url:
    r=requests.get(j,headers=header)
    r.encoding=r.apparent_encoding
    text=r.text
    #print(text)
    urls=re.compile('<li><span>(.*?)</span><a href="(.*?)" target=_blank').findall(text)
    n=1
    m='''<!doctype html>
<html>
<head>
<meta charset="utf8">
<title>英语阅读练习——by zf</title>

</head>
<body>
<center><p>.</p></center>
<center><p>.</p></center>
<a href="https://github.com/hfutzf" target="_blank"><center><h1><font size="12" color="blue">英语阅读练习——by zf</font></h1></center> </a>
 <center><p>.</p></center>
<center><p>.</p></center>
<div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
<li id="h"><a href="/bn" title="国际新闻类文章"><font size="8" color="blue">国际新闻类文章</font></a></li>
<li id="b"><a href="/business" title="商业经济类文章"><font size="8" color="blue">商业经济类文章</font></a></li>
<li id="s"><a href="/technology" title="科技类文章"><font size="8" color="blue">科技类文章</font></a></li>
<li id="d"><a href="/education" title="教育类文章"><font size="8" color="blue">教育类文章</font></a></li>
<li id="x"><a href="/culture" title="文化类文章"><font size="8" color="blue">文化类文章</font></a></li>
<li id="ws"><a href="/science" title="科学类文章"><font size="8" color="blue">科学类文章</font></a></li>
<li id="w"><a href="/opinion" title="观点类文章"><font size="8" color="blue">观点类文章</font></a></li>
<li id="o"><a href="/other" title="其他网站推荐" target="_blank"><font size="8" color="green">其他网站推荐</font></a></li>
</ul>
</div>'''
    for i in urls[:20]:
        try:
            
            #time.sleep(random.randint(3,6))
            #print(i[0],'http://www.qqenglish.com'+i[1])
            r=requests.get('http://www.qqenglish.com'+i[1],headers=header)
            r.encoding=r.apparent_encoding
            text=r.text
            title=re.compile('<H2>(.*?)</H2>').findall(text)[0]
            data=re.compile(r'</script></div>(.*?)全文请访问',re.DOTALL).findall(text)[0].replace('</div>','').replace('<FONT color=#666666>“','')[:-4]
            #print(title)
            #print(data)
            m=m+'<center><h1><font color="green">这是第'+str(n)+'篇文章</font></h1></center>\n'
            m=m+'<center><h1><font color="red">文章标题-'+title+'</font></h1></center>\n'
            m=m+'<center><p>日期-'+i[0]+'</p></center>\n'
            m=m+'<font size="7" face="arial">'
            m=m+data
            m=m+'</font>'
            m=m+'\n\n'
            n=n+1
            print(title)
        except:
            pass
    filename = 'F:\\蛐蛐英语'+re.compile(r'com/bn/(.*?)/',re.DOTALL).findall(j)[0]+'.txt'
    m=m+'</body> </html>'
    with open(filename,'w',encoding='utf-8') as fileobject: #使用‘w’来提醒python用写入的方式打开
         fileobject.write(m)
    
