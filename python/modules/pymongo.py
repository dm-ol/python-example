# Щоб вставити документ у колекцію, використовуйте метод insert one().
# Перший параметр методу insert one() — це словник, що містить імена та значення кожного поля в документі, який ви хочете вставити.

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

mydict = {"name": "John", "address": "Highway 37"}

x = mycol.insert_one(mydict)

# Метод повертає об'єкт InsertOneResult з властивістю insert id, що містить ідентифікатор вставленого документа.


# Щоб зробити розширені запити, можна використовувати модифікатори як значення в об'єкті запиту.


myclient = pymongo.MongoClient("mongodb: //localhost: 27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

myquery = {"address": {"$gt": "S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

# Наприклад, щоб знайти документи, в яких поле "адреса" починається з літери "S" або вище (за абеткою), використовуйте модифікатор "більше, ніж": {"$gt": "S"}.
