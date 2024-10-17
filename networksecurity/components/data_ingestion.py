from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logger.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact

import os 
import sys
import pandas as pd
import numpy as np
import pymongo
from typing import List

from dotenv import loaad_dotenv
loaad_dotenv()
MONGO_DB_URL=os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

class DataIngestion:
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    def export_collection_as_dataframe(self):
        try:
            database_name=self.data_ingestion_config.database_name
            collection_name=self.data_ingestion_config.collection_name

            self.mongo_client=pymongo.MongoClient(MONGO_DB_URL)
            collection=self.mongo_client[database_name][collection_name]

            df=pd.DataFrame(list(collection.find()))

            if "_id" in df.columns.to_list():
                df=df.drop(columns=["_id"],axis=1)

            df.replace({"na":np.nan},inplace=True)

            return df

        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def export_data_into_feature_store(self,dataframe: pd.DataFrame):
        try:
            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating folder
            dir_path=os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)
            dataframe_to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        except Exception as e:
            raise NetworkSecurityException(e,sys)
    
    def split_data_as_train_test(self,dataframe: pd.DataFrame):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        