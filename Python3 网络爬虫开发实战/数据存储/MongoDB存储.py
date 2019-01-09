# 连接MongoDB
import pymongo
client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')

# 指定数据库
db = client.test

# 指定集合
collection = db.students

# 插入数据
student = {
    'id':'20170101',
    'name':'Jordan',
    'age':20,
    'gender':'male'
}

result = collection.insert(student)
print(result)

student1 = {
    'id':'20170102',
    'name':'Bow',
    'age':21,
    'gender':'male'
}

student2 = {
    'id':'20170103',
    'name':'Mary',
    'age':19,
    'gender':'female'
}

result = collection.insert([student1, student2])
print(result)

# result = collection.insert_one(student)
# print(result)
# print(result.inserted_id)
#
# result = collection.insert_many([student1, student2])
# print(result)
# print(result.inserted_ids)

# 查询
result = collection.find_one({'name':'Mary'})
print(result)
print(type(result))

from bson.objectid import ObjectId
result = collection.find_one({'_id': ObjectId('5c1e29e1a45858289098b56b')})
print(result)


student3 = {
    'id':'20170104',
    'name':'Mark',
    'age':20,
    'gender':'male'
}

student4 = {
    'id':'20170105',
    'name':'Madong',
    'age':20,
    'gender':'male'
}

collection.insert_many([student3, student4])

results = collection.find({"age":20})
print(results)
print(type(results))
for result in results:
    print(result)

print('*'*20)
results = collection.find({'age':{'$gt':20}})
for result in results:
    print(result)
print('*'*20)
results = collection.find({'name':{'$regex':'^M.*'}})
for result in results:
    print(result)
print('*'*20)

# 计数
count = collection.find().count()
print(count)

count = collection.find({'age':20}).count()
print(count)

# 排序
results = collection.find().sort('age', pymongo.ASCENDING)
print([result['name'] for result in results])

results = collection.find().sort('age', pymongo.DESCENDING)
print([result['name'] for result in results])

# 偏移
results = collection.find().sort('age', pymongo.ASCENDING).skip(2)
print([result['name'] for result in results])

results = collection.find().sort('age', pymongo.ASCENDING).skip(2).limit(2)
print([result['name'] for result in results])

# 更新
student = collection.find_one({'name':'Mary'})
print(student)
student['age'] = 25
result = collection.update({'name':'Mary'}, student)
print(result)
result = collection.update({'name':'Mary'},{'$set':student})
print(result)

condition = {'name':'Mark'}
student = collection.find_one(condition)
student['age'] = 26
result = collection.update_one(condition,{'$set':student})
print(result)
print(result.matched_count, result.modified_count)

condition = {'age':{'$gt':20}}
result = collection.update_one(condition, {'$inc':{'age':1}})
print(result)
print(result.matched_count,result.modified_count)

condition = {'age':{'$gt':20}}
result = collection.update_many(condition, {'$inc':{'age':1}})
print(result)
print(result.matched_count,result.modified_count)

# 删除
result = collection.remove({'name':'Mary'})
print(result)

result = collection.delete_one({'name':'Mary'})
print(result)
print(result.deleted_count)
result = collection.delete_many({'age':{'$gt':25}})
print(result)
print(result.deleted_count)