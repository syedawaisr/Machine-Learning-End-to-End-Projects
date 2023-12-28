# This file contains functions for data_ingestion


'''
There are 2 folders, 1 foor genuine images and another
for forged images. create a function to get the images.
take genuine in genuine_images list and forged in forged_images list.
then use data_frames with same names and acquire the fina data as DataFrame
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
from src.components.filters import FiltersClass


# @dataclass
# class Data_ingestion_config:
#     # train_data_path = os.path.join('images','Hgenuine')
#     # test_data_path =  os.path.join('images','Hforged')
#     pass

class Data_ingestion:

    def __init__(self):
        # self.ingestion_config= Data_ingestion_config()
        self.fil = FiltersClass()

    def get_images(self,directory): # takes the folder path, read all the images and retruns a list containing all the images

        try:
            # List to store images
            images = []
            # Loop through all files in the directory
            for filename in os.listdir(directory):
                if filename.endswith(".JPG") or filename.endswith(".jpg") or filename.endswith(".HEIC") or filename.endswith(".heic") :  # Check for image extensions
                    filepath = os.path.join(directory, filename)
                    image = cv.imread(filepath, cv.IMREAD_GRAYSCALE)
                    if image is not None:
                        image = cv.resize(image, (194, 90))
                        #feature_vector,_ = self.fil.filter01(image)
                        images.append(image)
                    else:
                        print(f"Could not read {filename}")
            # after reading all the images, return them in a list named as images
            return images
        except Exception as e:
            logging.info("error while creating images list from Hgenuine or forged images")
            raise CustomException(e,sys)


    def get_data_frame(self,images,target): # takes image_array list and assign them target then return that dataframe
        try:

            # take images list and assign them the given target
            df = pd.DataFrame()
            for image in images:
                arr = image.flatten()
                new_row = arr.reshape(arr.size)
                # Convert the new row to a DataFrame
                new_row_df = pd.DataFrame([new_row])
                # Concatenate the existing DataFrame with the new row DataFrame
                df = pd.concat([df, new_row_df], ignore_index=True)
                df['target'] = target
                df
            return df
        except Exception as e:
            logging.info("Error while converting images to dataframe")
            raise CustomException(e,sys)







