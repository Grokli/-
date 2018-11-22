# 读取JSON
import json

str = """
[{
    "name":"Bob",
    "gender":"male",
    "birthday":"1992-10-18"
},{
    "name":"Selina",
    "gender":"female",
    "birthday":"1995-10-18"
}]
"""
print(type(str))
data = json.loads(str)
print(data)
print(type(data))
print(data[0].get('age',25))

data = [{
    'name':'Bob',
    'gender':'male',
    'birthday':'1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))

data = [{
    'name':'王伟',
    'gender':'男',
    'birthday':'1992-10-18'
}]
with open('data1.json','w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))