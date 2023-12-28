import os
import sys
from sklearn.svm import SVC
from src.logger import logging
from src.exception import CustomException
from src.components.data_transform import Data_transform
from sklearn.metrics import accuracy_score, classification_report
from dataclasses import dataclass
from src.utils import save_object

@dataclass 
class ModelTrainerConfig:
    trained_model_file_path = os.path.join('artifacts','model.pkl')

class Training_models:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
        self.df = Data_transform()

    def initiate_training(self):
        # get final_data from data_transform

        final_data = self.df.get_final_data()
        print(final_data.head(40))

        # get data after feature engineering
        x_train, x_test, y_train, y_test = self.df.transform_data(final_data)

        svm = SVC(kernel='linear')  # You can choose different kernels like 'linear', 'rbf', 'poly', etc.

        # Train the classifier using scaled features
        svm.fit(x_train, y_train)

        # Make predictions on the scaled test set
        predictions = svm.predict(x_test)

        # Calculate accuracy
        accuracy = accuracy_score(y_test, predictions)
        print(f"Accuracy: {accuracy}")

        # Display classification report
        print("Classification Report:")
        print(classification_report(y_test, predictions))

        save_object(
                 file_path=self.model_trainer_config.trained_model_file_path,
                 obj=svm
            )


if __name__ == "__main__":

    obj = Training_models()
    obj.initiate_training()

