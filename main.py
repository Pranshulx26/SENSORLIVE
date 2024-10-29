from sensor.exception import SensorException
import sys 
from sensor.logger import logging
from sensor.utils import dump_csv_file_to_mongodb_collection


# def test_exception():
#     try:
#         logging.info("ki yha pe bhaiya ek error aayegi division by zero vaali")
#         a=1/0
#     except Exception as e:
#         raise SensorException(e, sys)

if __name__=='__main__':
    file_path=r"C:\Users\91965\SENSORLIVE\notebook\data\aps_failure_training_reduced.csv"
    database_name='livesensor'
    collection_name='sensor'
    dump_csv_file_to_mongodb_collection(file_path=file_path, database_name=database_name, collection_name=collection_name)
    
    
    # try:
    #     test_exception()
    # except Exception as e:
    #     print(e)