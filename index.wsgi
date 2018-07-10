# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 13:58:15 2018

@author: Administrator
"""

# encoding=utf8
import sae,numpy,math
import sae.kvdb

kv = sae.kvdb.Client()

#导入Bottle模块
from bottle import Bottle,route, run, template, request, response,  post, get,static_file,debug
app=Bottle()
debug(True)  #打开debug功能
import matplotlib.pyplot as plt
from io import BytesIO
import base64
def plot():
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="12" color="blue">.</font></p></center>
    <center><p><font size="12" color="blue">.</font></p></center>
    <title>线性回归方程求解</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">线性回归方程求解</font></h1></center>
    <center><p><font size="12" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
    <div id="navfirst">
<ul id="menu">
<li id="hh"><a href="/19" title="十九大报告中英文全文"><font size="8" color="blue">十九大报告中英文全文</font></a></li>
</ul>
</div>
    <form method = "POST" id="form">
    <h3><font size="12" color="red">请输x内容</font>
    <input name="x" style='font-size:40px;background: #F0F8FF;'size=35 /></h3>
    <h3><font size="12" color="red">请输y内容</font>
    <input name="y" style='font-size:40px;background: #F0F8FF;' size=35/></h3>
    <h3><font size="12" color="red">是否取对所有数据取对数</font>
    <input name="d" style='font-size:40px;background: #F0F8FF;' size=10/></h3>
    <h3><input type='submit' style='font-size:40px;background: #F0F8FF;' value='确定' /></h3>
	</form>
    </body> </html>'''
    return page
    
    
def linear(number,xstr,ystr):
        xtuple=eval(xstr)
        xlist=[]
        if number=='yes':
            for x in xtuple:
                if x>0:
                    xlist.append(math.log(float(x))) #这里的numpy.log(是为了金属工艺学实验而加的，后面必须去掉)变为：xlist=list(xtuple)
                else:
                    return '222333','222333'
        else:
            for i in xtuple:xlist.append(float(i))
        ytuple=eval(ystr)
        ylist=[]
        if number=='yes':
            for y in ytuple:
                if y>0:
                    ylist.append(math.log(float(y))) #这里的numpy.log(是为了金属工艺学实验而加的，后面必须去掉)变为：xlist=list(xtuple)
                else:
                    return '222333','222333'
        else:
            for i in ytuple:ylist.append(float(i))
        if len(ylist)==len(xlist):
            pass
        else:
            return '222333','222333'
        xaver=float(sum(xlist))/len(xlist)
        yaver=float(sum(ylist))/len(ylist)
        xy=[] 
        for i in xlist:
            for j in ylist:
                if xlist.index(i)==ylist.index(j):
                    a=i*j
                    xy.append(a)
        xx=[]
        for ii in xlist:
            b=ii**2
            xx.append(b)
        xyaver=float(sum(xy))/len(xy)
        xxaver=float(sum(xx))/len(xx)
        if (xaver**2-xxaver)!=0:
            para=(xaver*yaver-xyaver)/(xaver**2-xxaver)
            bbb=yaver-para*xaver
            if bbb>=0:
                if number=='yes':
                    return round((math.e)**bbb,4),round(para,4)
                else:
                    	return para,bbb
        else:
            return '222333','222333'
     
def get_data():
    page='''<html>
    <head>
    <meta charset="utf8">
    <center><p><font size="12" color="blue">.</font></p></center>
    <center><p><font size="12" color="blue">.</font></p></center>
    <title>我的云笔记</title>
    </head>
    <body>
    <center><h1><font size="12" color="red">我的云笔记</font></h1></center>
    <center><p><font size="12" color="blue">.</font></p></center>
    <h5><font size="6" color="green">友情链接</font></h5>
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
    <li id="w"><a href="/images/text.txt" ><font size="8" color="green">小彩蛋——点击阅读700篇文章</font></a></li>
</ul>
</div>
    <form method = "POST" id="form">
    <center><h3><font size="12" color="red">请输入内容</font></h3></center>
		<center><textarea name="note" style='font-size:40px;background: #F0F8FF;' cols="45" rows="5"></textarea></center>
	</form>
 
	<button type="submit" form="form"><font size="12" >提交<br></font></button>

'''
    data=kv.getkeys_by_prefix('', limit=1000000, marker=None)
    for i in data:
        page=page+'<p style="width:965px; word-wrap:break-word;"><font size="12">&nbsp;&bull;&nbsp;&nbsp;'
        page=page+kv.get(i)
        page=page+'</font></p>'
    page=page+'</body> </html>'
    return page

@app.get('/')
def data():
    return plot()

@app.post('/')
def plot_data():
    xx = request.forms.get('x')
    yy = request.forms.get('y')
    d=request.forms.get('d')
    if xx!=None and yy!=None:
        para,bbb=linear(d,xx,yy)
        x=list(eval(xx))
        y=list(eval(yy))
        if para!='222333':
            if d=='yes':
                zz=numpy.arange(min(x),max(x),0.001)
                yyy=round(para,4)*(zz**(round(bbb,4)))
                plt.title('linear')  # 图名
                plt.plot(x, y, 'ro')  # 图上的点,最后一个参数为显示的模式
                plt.plot(zz,yyy,'b-',label='y='+str(para)+'x^'+str(round(bbb,4))) 
                buffer = BytesIO()
                label='y='+str(para)+'x^'+str(round(bbb,4))
                plt.savefig(buffer)  
                plot_data = buffer.getvalue()
                
                # 图像数据转化为 HTML 格式
                imb = base64.b64encode(plot_data)  
                #imb = plot_data.encode('base64')   # 对于 Python 2.7可用 
                ims = imb.decode()
                imd = "data:image/png;base64,"+ims
                iris_im = "<img src='%s'>"% imd   
                
                root = "<title>Iris Dataset</title>"
                root = root + iris_im+"<center><h1>result:"+label+"</h1></center>  " #将多个 html 格式的字符串连接起来
                plt.close()
                return root
            else:
                zz=numpy.arange(min(x),max(y),0.001)
                yyy=para*zz+bbb
                plt.title('linear')  # 图名
                plt.plot(x, y, 'ro')  # 图上的点,最后一个参数为显示的模式
                plt.plot(zz,yyy,'b-',label='y='+str(round(para,4))+'x+'+str(round(bbb,4))) 
                buffer = BytesIO()
                plt.savefig(buffer)  
                plot_data = buffer.getvalue()
                label='y='+str(round(para,4))+'x+'+str(round(bbb,4))
                # 图像数据转化为 HTML 格式
                imb = base64.b64encode(plot_data)  
                #imb = plot_data.encode('base64')   # 对于 Python 2.7可用 
                ims = imb.decode()
                imd = "data:image/png;base64,"+ims
                iris_im = "<img src='%s'>" % imd 
                
                root = "<title>Iris Dataset</title>"
                root = root + iris_im+"<center><h1>result:"+label+"</h1></center>  " #将多个 html 格式的字符串连接起来
                plt.close()
                return root
    else:
        return '<h1>您的输入为空，请重新输入<h1>'

@app.get("/index")
def web_login():
    return template("index")

@app.get("/bn")
def bn():
    return template("bn")
@app.get("/19")
def party():
    return template("19")

@app.get("/images/:filename")
def file_images(filename):
    return static_file(filename,root='images')

@app.get('/login')
def login_form():
    return get_data()

@app.post('/login')
def login():
    name = request.forms.get('note')
    if name!='':
        if len(name.replace(' ','&nbsp;').replace('\r\n','<br>'))>=250:
    		kv.set(name.replace(' ','&nbsp;').replace('\r\n','<br>')[:200],name.replace(' ','&nbsp;').replace('\r\n','<br>'))
    		return get_data()
        else:
    		kv.set(name.replace(' ','&nbsp;').replace('\r\n','<br>'),name.replace(' ','&nbsp;').replace('\r\n','<br>'))
    		return get_data()
    else:
        return '<h1>您的输入为空，请重新输入<h1>'

@app.get("/business")
def business():
    return template("business")
@app.get("/technology")
def technology():
    return template("technology")
@app.get("/education")
def education():
    return template("education")
@app.get("/culture")
def culture():
    return template("culture")
@app.get("/science")
def science():
    return template("science")
@app.get("/opinion")
def opinion():
    return template("opinion")

@app.get("/other")
def other():
    return template("other")

application = sae.create_wsgi_app(app)
