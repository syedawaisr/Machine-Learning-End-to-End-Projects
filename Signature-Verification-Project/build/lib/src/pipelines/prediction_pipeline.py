import sys
import os
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object
import pandas as pd
from src.components.filters import FiltersClass
import numpy as np

class PredictPipeline:
    def __init__(self):
        self.fil = FiltersClass()

    def predict(self,img):
        try:
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            model_path=os.path.join('artifacts','model.pkl')

            preprocessor=load_object(preprocessor_path)
            model=load_object(model_path)

            image = [img]
            for  img in image:
                pass
                # print(img.shape)
                # print(img.size)
            features = self.fil.filter01(image)
            img_array = np.array(features[0]).reshape(1, -1)  # Flatten the image to a 1D array

            data_scaled=preprocessor.transform(img_array)

            pred=model.predict(data_scaled)
            return pred
            

        except Exception as e:
            logging.info("Exception occured in prediction")
            raise CustomException(e,sys)
        
