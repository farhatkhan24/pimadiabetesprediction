import pickle
import streamlit as st
from PIL import Image

diabetes_model=pickle.load(open('diabetes_pickle_file','rb'))
st.title(' PIMA Diabetes Predicton Using ML')

image=Image.open("diabetes_image.jpg")
st.image(image,use_column_width=True)

col1,col2,col3 =st.columns(3)
with col1:
    Pregnancies=st.text_input('Number of Pregnancies')
with col2:
   Glucose=st.text_input('Number of Glucose')
with col3:
    BloodPressure=st.text_input('Number of BloodPressure')
with col1:
    SkinThickness=st.text_input('Number of SkinThickness')
with col2:
    Insulin=st.text_input('Number of Insulin')
with col3:
    BMI=st.text_input('Number of BMI')
with col1:
    DiabetesPedigree=st.text_input('Number of DiabetesPedigree')
with col2:
    Age=st.text_input('Nmuber of Age')

diab_diagnosis = ''
if st.button('Diabetes Test Result'):
    diab_prediction = diabetes_model.predict(
        [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigree, Age]])

    if (diab_prediction[0] == 1):
        diab_diagnosis = 'The Person is diabetic'
    else:
        diab_diagnosis = 'The person is not diabetic'
st.success(diab_diagnosis)