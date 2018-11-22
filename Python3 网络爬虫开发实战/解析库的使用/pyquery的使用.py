# 字符串初始化
html = """
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div> 
"""
from pyquery import PyQuery as pq

doc = pq(html)
print(doc('li'))

# URL初始化
from pyquery import PyQuery as pq

doc = pq(url='https://cuiqingcai.com')
print(doc('title'))

import requests

doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))

# 文件初始化
from pyquery import PyQuery as pq

doc = pq(filename='test.html')
print(doc('li'))

# 基本CSS选择器
html = """
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div> 
"""
from pyquery import PyQuery as pq

doc = pq(html)
print(doc("#container .list li"))
print(type(doc('#container .list li')))

# 查找节点
# 子节点
from pyquery import PyQuery as pq

doc = pq(html)
items = doc(".list")
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

lis = items.children()
print(type(lis))
print(lis)

lis = items.children('.active')
print(lis)

# 父节点
html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div> 
"""
from pyquery import PyQuery as pq

doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

parents = items.parents()
print(type(parents))
print(parents)

parent = items.parents('.wrap')
print(parent)

# 兄弟节点
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())

print(li.siblings('.active'))

# 遍历
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.item-0.active')
print(li)
print(str(li))

from pyquery import PyQuery as pq

doc = pq(html)
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li, type(li))

# 获取信息
from pyquery import PyQuery as pq

doc = pq(html)
a = doc('.item-0.active a')
print(a, type(a))
print(a.attr("href"))
print(a.attr.href)

a = doc('a')
print(a, type(a))
print(a.attr('href'))
print(a.attr.href)

doc = pq(html)
a = doc('a')
for item in a.items():
    print(item.attr("href"))

# 获取文本
from pyquery import PyQuery as pq

doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text())

doc = pq(html)
li = doc(".item-0.active")
print(li)
print(li.html())

doc = pq(html)
li = doc('li')
print(li.html())
print(li.text())
print(type(li.text()))

# 节点操作
from pyquery import PyQuery as pq

doc = pq(html)
li = doc('.item-0.active')
print(li)
li.removeClass('active')
print(li)
li.addClass('active')
print(li)

# attr、text和html
html = """
<ul class="list">
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
"""
from pyquery import PyQuery as pq

doc = pq(html)
li = doc(".item-0.active")
print(li)
li.attr("name","link")
print(li)
li.text('changed item')
print(li)
li.html("<span>changed item</span>")
print(li)

# remove()
html = """
<div class="wrap">
    Hello,World
<p>This is a paragrapg.</p>
</div>
"""
from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
print(wrap.text())

wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
html = """
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div> 
"""
from pyquery import PyQuery as pq

doc = pq(html)
li = doc("li:first-child")
print(li)
li = doc("li:last-child")
print(li)
li = doc("li:nth-child(2)")
print(li)
li = doc("li:gt(2)")
print(li)
li = doc("li:nth-child(2n)")
print(li)
li = doc("li:contains(second)")
print(li)
