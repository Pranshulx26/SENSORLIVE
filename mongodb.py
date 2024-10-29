from pymongo import MongoClient  # type: ignore
import os 

from dotenv import load_dotenv
print(f"for reading the .env file")
load_dotenv()

uri = os.getenv('MONGO_DB_URL')




client = MongoClient(uri)
db = client['liveclass']
collection = db['mongoclass']
data = {
    "name": "pranshul Sharma",
    "age": 2,
    "email": "pranshulsharma83@gmail.com"
    
}
# inserting data
collection.insert_one(data)
# fetching data
# cursor = collection.find({})
# for i in cursor:
#     print(i)

