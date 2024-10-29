from dataclasses import dataclass, field
import os 
import pymongo 

@dataclass
class EnvironmentVariable:
    mongo_db_url: str = field(init=False)

    def __post_init__(self):
        self.mongo_db_url = os.getenv('MONGO_DB_URL')
        if self.mongo_db_url is None:
            print("VARIABLE_NAME is not set in the .env file")
        else:
            print(f"The value of VARIABLE_NAME is: {self.mongo_db_url}")

env_var = EnvironmentVariable()

mongo_client = pymongo.MongoClient(env_var.mongo_db_url)
