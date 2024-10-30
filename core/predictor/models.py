from django.db import models

# Create your models here.
import joblib  

MODEL_PATH = 'static/adaboost_model/adaboost_model.pkl'  # Path to the saved model  
model = joblib.load(MODEL_PATH)  # Load the AdaBoost model