# -*- coding: utf-8 -*-
"""wine_type_d.ipynb"""

import numpy as np
import pickle
import streamlit as st

model =joblib.load('model.pkl')

st.set_page_config(page_title="wine type prediction", layout="centered")
st.title("wine type prediction App")
st.write("predict whether the wine is **Red** or **white** using chemical properties")

fixed_acidity = st.number_input("value of fixed acidity",value=None)
volatile_acidity = st.number_input("value of volatile acidity",value=None)
citric_acid = st.number_input("value of citric acid",value=None)
residual_sugar = st.number_input("value of residual sugar",value=None)
chlorides = st.number_input("value of chlorides",value=None)
free_sulfur_dioxide = st.number_input("value of free sulfur dioxide",value=None)
total_sulfur_dioxide = st.number_input("value of total sulfur dioxide",value=None)
density = st.number_input("value of density",value=None)
pH = st.number_input("value of pH",value=None)
sulphates = st.number_input("value of sulphates",value=None)
alcohol = st.number_input("value of alcohol",value=None)
quality= st.number_input("value of quality",value=None)
if st.button("predict"):
    input_data = np.array([[fixed_acidity,
                            volatile_acidity,
                            citric_acid,
                            residual_sugar,
                            chlorides,
                            free_sulfur_dioxide,
                            total_sulfur_dioxide,
                            density,
                            pH,
                            sulphates,
                            alcohol,
                            quality
                            ]])
    
    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("white wine")
    else:
        st.success("red wine")
