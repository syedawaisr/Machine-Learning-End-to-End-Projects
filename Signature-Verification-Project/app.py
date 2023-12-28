# from flask import Flask, request, render_template
# from src.pipelines.prediction_pipeline import PredictPipeline
# import numpy as np
# import cv2

# app = Flask(__name__)

# predictor = PredictPipeline()

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get the uploaded file from the request
#         uploaded_file = request.files['file']
        
#         # Read the file content as bytes
#         img_bytes = uploaded_file.read()
        
#         # Convert bytes to a numpy array that represents the image
#         nparr = np.frombuffer(img_bytes, np.uint8)
        
#         # Decode the numpy array into an image using OpenCV
#         img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)  # Change IMREAD_COLOR to IMREAD_GRAYSCALE for grayscale images
        
#         # Now 'img' is a numpy array that represents the image
#         # Use this 'img' array for further processing or pass it to the predictor
        
#         # Example: Pass the image to the predictor
#         prediction = predictor.predict(img)
#         prediction_str = str(prediction)
#         return prediction_str
#     except Exception as e:
#         return str(e)

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, render_template
from src.pipelines.prediction_pipeline import PredictPipeline
import numpy as np
import cv2

app = Flask(__name__)

predictor = PredictPipeline()

@app.route('/')
def index():
    return render_template('index.html', prediction="")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the uploaded file from the request
        uploaded_file = request.files['file']
        
        # Read the file content as bytes
        img_bytes = uploaded_file.read()
        
        # Convert bytes to a numpy array that represents the image
        nparr = np.frombuffer(img_bytes, np.uint8)
        
        # Decode the numpy array into an image using OpenCV
        img = cv2.imdecode(nparr, cv2.IMREAD_GRAYSCALE)  # Change IMREAD_COLOR to IMREAD_GRAYSCALE for grayscale images
        
        # Now 'img' is a numpy array that represents the image
        # Use this 'img' array for further processing or pass it to the predictor
        
        # Example: Pass the image to the predictor
        prediction = predictor.predict(img)
        prediction_str = str(prediction)
        return render_template('index.html', prediction=prediction_str)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
