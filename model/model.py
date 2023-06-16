from keras.models import load_model
from pathlib import Path

__version__ = "0.1.0"

BASE_DIR = Path(__file__).resolve(strict=True).parent

# with open("./model/hi.h5", "rb") as f:
#     model = load_model(f)
model = load_model('./model/my_h5_model.h5')

def predict_pipeline(arr):

    pred= model.predict_step(arr)
    return pred 

