# 解析器
from bs4 import BeautifulSoup

soup = BeautifulSoup('<p>Hello</p>', 'lxml')
print(soup.p.string)

# 基本用法
html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!--Elsie--></a>
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")
print(soup.prettify())
print(soup.title.string)

# 选择元素
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)

# 提取信息
print(soup.title.name)
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])
print(soup.p.string)

# 嵌套选择
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.head.title)
print(type(soup.head.title))
print(soup.head.title.string)

# 关联选择
# 子节点和子孙节点
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")
print(soup.p.contents)

print(soup.p.children)
for i,child in enumerate(soup.p.children):
    print(i, child)

print(soup.p.descendants)
for i, child in enumerate(soup.p.descendants):
    print(i, child)

# 父节点和祖父节点
html = """
<html>
<head>
<title>The Dormouse's story</title>
</head>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
</p>
<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.a.parent)

print(type(soup.a.parents))
print(list(enumerate(soup.a.parents)))

# 兄弟节点
html = """
<html>
<body>
<p class="story">
            Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">
<span>Elsie</span>
</a>
        Hello
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.
</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "lxml")
print('Next Sibling', soup.a.next_sibling)
print('Prev Sibling', soup.a.previous_sibling)
print('Next Sibling', list(enumerate(soup.a.next_siblings)))
print('Prev Siblings',list(enumerate(soup.a.previous_siblings)))

# 提取信息
html = """
<html>
<body>
<p class="story">
        Once upon a time there were three little sisters; and their names were
<a href='http://example.com/elsie' class="sister" id="link1">Bob</a><a href="http://example.com/lacie"
class="sister" id="link2">Lacie</a>
</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print('Next Sibling:')
print(type(soup.a.next_sibling))
print(soup.a.next_sibling)
print(soup.a.next_sibling.string)
print('Parent:')
print(type(soup.a.parents))
print(list(soup.a.parents)[0])
print(list(soup.a.parents)[0].attrs['class'])

# 方法选择器
# find_all()
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))

for ul in soup.find_all(name='ul'):
    print(ul.find_all(name='li'))
    for li in ul.find_all(name='li'):
        print(li.string)

# attrs
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find_all(attrs={"id":"list-1"}))
print(soup.find_all(attrs={"class":"element"}))

print(soup.find_all(id='list-1'))
print(soup.find_all(class_='element'))

# text
import re

html="""
<div class="panel">
<div class="panel-body">
<a>Hello, this is a link</a>
<a>Hello, this is a link, too</a>
</div>
</div>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html,"lxml")
print(soup.find_all(text=re.compile("link")))

# find()
html = """
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

# CSS选择器
from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
print(soup.select(".panel .panel-heading"))
print(soup.select("ul li"))
print(soup.select("#list-2 .element"))
print(type(soup.select('ul')[0]))

for ul in soup.select('ul'):
    print(ul.select('li'))

# 获取属性
from bs4 import BeautifulSoup

soup = BeautifulSoup(html,'lxml')
for ul in soup.select('ul'):
    print(ul['id'])
    print(ul.attrs['id'])

# 获取文本
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
for li in soup.select('li'):
    print('Get Text:', li.get_text())
    print("String:", li.string)

