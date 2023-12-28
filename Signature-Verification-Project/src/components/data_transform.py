import numpy as np
import pandas as pd
import cv2 as cv
import os
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
from src.components.data_ingestion import Data_ingestion
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.model_selection import train_test_split
from src.components.filters import FiltersClass
from src.utils import save_object
from dataclasses import dataclass

# from data_ingestion import get_data_frame

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pkl')

class Data_transform:
    def __init__(self):
        #self.current_dir = os.path.dirname(os.path.abspath(__file__))
        #self.grandparent_dir = os.path.join(self.current_dir, '..', '..')

        #self.hgenuine_path = os.path.join(self.grandparent_dir, 'images', 'Hgenuine')
        #self.hforged_path = os.path.join(self.grandparent_dir, 'images', 'Hforged')
        self.hgenuine_path = 'D://One Drive Data//7th Semester//Digital Image Processing//DIP Project//images//Hgenuine'
        self.hforged_path = 'D://One Drive Data//7th Semester//Digital Image Processing//DIP Project//images//Hforged'
        self.fil = FiltersClass()
        self.data_transformation_config=DataTransformationConfig()

    
    def get_final_data(self):
        try:
            # call the data_ingestion_function for both genuine and forged
            self.ingest = Data_ingestion()
            # self.forged = Data_ingestion()

            images1 = self.ingest.get_images(self.hgenuine_path)
            feature_vector = self.fil.filter01(images1)
            # call the filter for images here and return list of feature_vectors
            df1 = self.ingest.get_data_frame(feature_vector,1) # pass feature vector here
            logging.info("genuine images loaded successfully, Length of images1: {len(images1)}")


            images2 = self.ingest.get_images(self.hforged_path)
            feature_vector2  = self.fil.filter01(images2)
            df2 = self.ingest.get_data_frame(feature_vector2,0)
            logging.info("forged images loaded successfully, length of images2: {len(images2)}")

            # create final dataframe
            final_data = pd.concat([df1,df2], ignore_index=True)
            logging.info("final_data has been achieved, data shape = {final_data.shape}")

            return final_data
        except Exception as e:
            logging.info("error")
            raise CustomException(e,sys)


    def transform_data(self,df):
        try:

            # this funciton will take final_data and apply feature engineering
            # Passing the model to the SVM for predictions
            df.columns = df.columns.astype(str)
            x = df.iloc[:,:-1] # all features excluding target value
            y = df['target']

            x_train, x_test , y_train, y_test = train_test_split(x, y,test_size = 0.7 , random_state = 42)
            logging.info("Cross validation is completed successfully")

            # Scale the features using StandardScaler
            scaler = StandardScaler()
            x_train_scaled = scaler.fit_transform(x_train)
            x_test_scaled = scaler.transform(x_test)
            logging.info("scalling has been performed successfully")

            train_arr = np.c_[x_train_scaled, np.array(y_train)]
            test_arr = np.c_[x_test_scaled, np.array(y_test)]

            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=scaler

            )
            logging.info('Preprocessor pickle file saved')


            # do other processes if required
            return x_train_scaled, x_test_scaled, y_train, y_test

        except Exception as e:
            logging.info('Error in data_tranform while cross validation')
            raise CustomException(e,sys)



        # Placeholder method for data transformation logic

# If you want to use the main block for directory path retrieval
# if __name__ == "__main__":

#     data = Data_transform()
#     data.get_final_data()

