# get()
import requests

r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)

r = requests.post('http://httpbin.org/post')
r = requests.put('http://httpbin.org/put')
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

data = {
    'name':'germey',
    'age':22
}
r = requests.get('http://httpbin.org/get', params=data)
print(r.text)
print(type(r.text))
print(r.json())
print(type(r.json()))

# 抓取网页
import requests
import re

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"
}
r = requests.get('https://www.zhihu.com/explore', headers=headers)
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)
titles = re.findall(pattern, r.text)
print(titles)

# 抓取二进制数据

import requests

r = requests.get("https://github.com/fluidicon.png")
print(r.text)
print(r.content)
with open('favicon.ico','wb') as f:
    f.write(r.content)

# POST请求
import requests

data = {'name':'germey', 'age':'22'}
r = requests.post('http://httpbin.org/post', data=data)
print(r.text)

# 响应
import requests

r = requests.get('http://www.jianshu.com')
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)

exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
