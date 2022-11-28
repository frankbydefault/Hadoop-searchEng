from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("mongodb://root:rootpassword@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0")
    
    db = client['data']
    collection = db['words']

    print("Connection Succesfull")

print('Escriba la palabra que quiere buscar:\n')
word = input()

cursor = collection.find({},{word:1})

for document in cursor:
    print(document)