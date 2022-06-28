# -*- coding: UTF-8 -*-

"""
@author:GaryPang
@time:2018/5/1
""" 
import urllib3
from urllib.parse import quote
import sys
import io
import json
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
http = urllib3.PoolManager()
x = quote(sys.argv[1])
y = "http://fanyi.youdao.com/openapi.do?keyfrom=SkyHacker&key=25021457&type=data&doctype=json&version=1.2&q="
r = http.request('GET', y+x)
r = r.data.decode('utf-8')
content = '<div id="json">'+r+'</div><div class="ydwrap"><div id="exp_w"><p>基本释义</p><div id="explains"></div></div><div id="web_w"><p>网络释义</p><div id="web"></div></div></div>'

head = """
<style>
#json{
display:none;
}
.ydwrap{
font-family:"Microsoft YaHei UI",tahoma;
font-size:14px;
line-height:22px;
margin-left:10px;
}
.ydwrap p{
margin:5px 0;
font-size:15px;
color: orangered;


}
.ydwrap div{
margin-bottom:22px;
}
</style>
<script>
window.onload = function(){
var json = document.getElementById("json").innerHTML;
var exp = document.getElementById("explains");
var web = document.getElementById("web");
var exp_w = document.getElementById("exp_w");
var web_w = document.getElementById("web_w");
var gg_w = document.getElementById("gg_w");
var obj=eval("("+json+")");
var explains="",webc="",a;
if(obj.basic){
if(obj.basic.explains){
var arr1 = obj.basic.explains;
for (a = 0; a < arr1.length; a++) {
	explains += arr1[a]+"<br/>";
}
exp.innerHTML = explains;
}
}
if(obj.web){
var arr2 = obj.web[0].value;
for (a = 0; a < arr2.length; a++) {
	webc += arr2[a]+"<br/>";
}
web.innerHTML = webc;
}
if(!exp.innerText){
exp_w.style.display="none";
}
if(!web.innerText){
web_w.style.display="none";
}
}
</script>"""

print('<head>\n%s\n</head>\n%s' % (head, content))
