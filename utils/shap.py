import joblib
from utils.prediction import pipeline_load_predict
import streamlit as st

pipeline = pipeline_load_predict() #Chargement du modèle

#SHAP global importance des features du modèle
@st.cache_resource
def load_shape():
    shape_infos = joblib.load("models/shape_cache_time.pkl")
    return shape_infos['explainer'], shape_infos['shap_values_globaux'], shape_infos['expected_value'], shape_infos['dataset']
