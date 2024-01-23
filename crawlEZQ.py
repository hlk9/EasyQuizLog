#!/usr/bin/env python
import requests
import time
import configparser
from pathlib import Path
import pymongo
import json

config = configparser.ConfigParser()
configPath = str(Path.joinpath(Path.cwd(),"config.ini"))
config.read(configPath)
timeDelay = config.get("general","time")
db_url = config.get("general","db_url")
mongoClient = pymongo.MongoClient(str(db_url))
mongoDatabase = mongoClient["local"]
databaseCollections = mongoDatabase["easy_quiz_log"]
while True:
    rawResponse = requests.get("https://api.quizpoly.xyz/quizpoly/using")   
    if(rawResponse.status_code==200):
       data = json.loads(rawResponse.content)
       x = databaseCollections.insert_many(data)
       print("Done!")
    else:
        print("Error")
    print("Waiting for the next request...")
    time.sleep(int(timeDelay))
  
   