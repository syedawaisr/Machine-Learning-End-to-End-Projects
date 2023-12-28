
'''
This file is created to create a full pipeline from taking an image to predicting its output
and saving that image, start by creating a method to take an image, then
1. resize the image
2. pass the image to the filter.
3. save the image if needed
4. get the filtered output and convert it into 1D array 
5. pass the image to the model and predict the output
'''

import numpy as np
import pandas as pd
import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import Data_ingestion
from src.components.data_transform import Data_transform
from src.components.training import Training_models

if __name__ == "__main__":

    obj = Data_ingestion()
    
    obj = Training_models()
    obj.initiate_training()






