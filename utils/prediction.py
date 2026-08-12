import joblib
import streamlit as st


#fonction permettant de charger le pipeline du classifieur
@st.cache_resource 
def pipeline_load_predict():
    pipeline = joblib.load('models/timeCantonRegressor.pkl')
    return pipeline

#fonction de prediction du pipeline
def make_prediction(pipeline, input):
    prediction = pipeline.predict(input)[0]
    return prediction