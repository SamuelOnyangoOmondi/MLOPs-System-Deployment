from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
import joblib

app = FastAPI()

model_path = './models/_model_name.pkl'  # Adjust the model file name as needed

# Load the model
try:
    model = joblib.load(model_path)
except FileNotFoundError:
    print(f"Model file not found at {model_path}. Please check the file path and name.")
    raise HTTPException(status_code=500, detail="Model file not found on server")

class PredictionRequest(BaseModel):
    features: list  # Define the shape of your features appropriately

@app.post("/predict/")
async def predict(request: PredictionRequest):
    """
    Receives a POST request with features and returns the model prediction.
    """
    # Convert the list of features into a numpy array and reshape for prediction
    features_array = np.array(request.features).reshape(1, -1)
    prediction = model.predict(features_array)
    return {"prediction": prediction.tolist()}  # Convert numpy array to list for JSON serialization
