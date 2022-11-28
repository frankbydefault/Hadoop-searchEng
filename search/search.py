from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient("mongodb://root:rootpassword@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.0")
    
    db = client['data']
    collection = db['words']

    print("Connection Succesfull")

while True:
    print("----- Escribir .exit para salir -----")
    word = input("search > ")

    if word== ".exit":
        break

    cursor = collection.find({},{word:1})

    try:
        for document in cursor:
            print([url[0] for url in document[word]])

    except:
        print('No hay resultados')
