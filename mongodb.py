from pymongo import MongoClient 


uri = "mongodb+srv://pranshulx26:Pranshul26@cluster0.zyfrp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)
db = client['liveclass']
collection = db['mongoclass']
data = {
    "name": "prince katiyar",
    "age": 2,
    "email": "princekatiyar444234@gmail.com"
    
}

# collection.insert_one(data)
cursor = collection.find({})
for i in cursor:
    print(i)