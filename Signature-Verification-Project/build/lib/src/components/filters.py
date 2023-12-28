# This file contains functions for data_ingestion


'''
This file contains different filters for feature extractions
'''

import numpy as np
import pandas as pd
import cv2 as cv
import os
import sys
from src.exception import CustomException
from src.logger import logging
from sklearn.model_selection import train_test_split
from dataclasses import dataclass
from skimage.feature import hog
import matplotlib.pyplot as plt
from skimage import exposure
import cv2 as cv

class FiltersClass:

    def __init_(self):
        pass

    def filter01(self,images): # takes the folder path, read all the images and retruns a list containing all the images
        try:
            feature_vector = []
            for img in images:
                # write code here
                print('apply filter')
                    # Read your image using OpenCV
                #print(img.shape)  # Check the shape of the image

                # Resize the image if needed
                resized_img = cv.resize(img, (194, 90))

                # Compute HOG features
                fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                                    cells_per_block=(2, 2), visualize=True)
                feature_vector.append(fd)
            return feature_vector # returns feature vector and hog filtered image

        except Exception as e:
            logging.info("error occured while filtering at filter01")
            raise CustomException(e,sys)

    def filter02(self,image):
        pass











# class DataIngestion():
#         def __init__(self):
#               self.ingestion_config = DataIngestionConfig()        
#         def initiate_data_ingestion(self):
#              logging.info("Data Ingestion starts")
#              try:                   
#                    # main ingestion code to be written here
#                    print("Hello World")
#                    df = pd.read_csv(os.path.join('Notebooks/data','gemstone.csv'))
#                    logging.info("main data file is read")

#                    os.makedirs(os.path.dirname(self.ingestion_config.raw_data_path),exist_ok=True)
#                    df.to_csv(self.ingestion_config.raw_data_path,index=False)
#                    logging.info('Train test split')
#                    train_set,test_set=train_test_split(df,test_size=0.30,random_state=42)
#                    train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
#                    test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
#                    logging.info("train,test and raw data files are created")
#                    # since transformation class will be using train and test data thus after ingestion we have to
#                    # return paths for train_data and test_data

#                    return(
#                          self.ingestion_config.train_data_path,
#                          self.ingestion_config.test_data_path
#                    )
#              except Exception as e:
#                    logging.info("Exception occured during data ingestion")
#                    raise CustomException(e,sys)
             
        
# The following code was just run in the begining to check if the train, test, raw files are created or not
# if __name__ == "__main__":
#       data = DataIngestion()
#       data.initiate_data_ingestion()
      

