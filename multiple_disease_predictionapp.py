# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 00:01:29 2023
@author: SUKANTA DUTTA
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu




# Loading the saved models
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('trained_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Sidebar navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Testing System Using ML',
                           
                           ['Diabetes Test',
                            'Heart Disease Test',
                            'Parkinsons Test'],
                           
                           icons = ['prescription2', 'heart-pulse-fill', 'person'],
                           default_index= 2 )


# Diabetes Prediction page
if selected == 'Diabetes Test':
    # Page title
    st.title('Diabetes Testing Using ML')
    
    
    #getting the input data from user
    #columns for input feilds
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Glucose Level')
        
    with col3:
        BloodPressue = st.text_input('Blood Pressue Value')
        
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
        
    with col2:
        Insulin = st.text_input('Insulin Level')
        
    with col3:    
        BMI = st.text_input('BMI Value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
        
    with col2:
        Age = st.text_input('Age of the person')
    
    
      
    
     
    
    
    
    


    #code for Prediction
    diab_diagnosis = ''
    diab_prediction = None
 
 
 #creating a burron for Prediction
 
    if st.button('Diabetes Test Result'):
         diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressue, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
     
    if(diab_prediction is not None and diab_prediction[0] == 1):
         diab_diagnosis = 'The Person is Diabetic'
    else:
         diab_diagnosis = 'The Person is not Diabetic'
         
    st.success(diab_diagnosis)
     

# Heart Disease Test page
if selected == 'Heart Disease Test':
    # Page title
    st.title('Heart Disease Testing Using ML')
    
    col1, col2, col3 = st.columns(3)
    
    # Input fields
    with col1:
        try:
            age = float(st.text_input('Age'))
        except ValueError:
            st.error('Please enter a valid numeric value for Age.')
            st.stop()
        
    with col2:
        try:
            sex = int(st.text_input('Sex'))
        except ValueError:
            st.error('Please enter a valid numeric value for Sex.')
            st.stop()
        
    with col3:
        try:
            cp = float(st.text_input('Chest Pain Types'))
        except ValueError:
            st.error('Please enter a valid numeric value for Chest Pain Types.')
            st.stop()
        
    with col1:
        try:
            trestbps = float(st.text_input('Resting Blood Pressure'))
        except ValueError:
            st.error('Please enter a valid numeric value for Resting Blood Pressure.')
            st.stop()
        
    with col2:
        try:
            chol = float(st.text_input('Serum Cholestrol in mg/dl'))
        except ValueError:
            st.error('Please enter a valid numeric value for Serum Cholestrol.')
            st.stop()
        
    with col3:    
        try:
            fbs = int(st.text_input('Fasting Blood Sugar > 120 mg/dl'))
        except ValueError:
            st.error('Please enter a valid numeric value for Fasting Blood Sugar.')
            st.stop()
        
    with col1:
        try:
            restecg = float(st.text_input('Resting Electrocardiographic results'))
        except ValueError:
            st.error('Please enter a valid numeric value for Resting Electrocardiographic results.')
            st.stop()
        
    with col2:
        try:
            thalach = float(st.text_input('Maximum Heart Rate Acheived'))
        except ValueError:
            st.error('Please enter a valid numeric value for Maximum Heart Rate Acheived.')
            st.stop()
        
    with col3:
        try:
            exang = int(st.text_input('Exercise induced Angina'))
        except ValueError:
            st.error('Please enter a valid numeric value for Exercise induced Angina.')
            st.stop()
        
    with col1:
        try:
            oldpeak = float(st.text_input('ST depression induced by exercise'))
        except ValueError:
            st.error('Please enter a valid numeric value for ST depression induced by exercise.')
            st.stop()
        
    with col2:
        try:
            slope = float(st.text_input('Slope of the Peak Exercise ST Segment'))
        except ValueError:
            st.error('Please enter a valid numeric value for Slope of the Peak Exercise ST Segment.')
            st.stop()
        
    with col3:    
        try:
            ca = float(st.text_input('Major Vessels colored by flourosopy'))
        except ValueError:
            st.error('Please enter a valid numeric value for Major Vessels colored by flourosopy.')
            st.stop()
        
    with col1:
        try:
            thal = float(st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect'))
        except ValueError:
            st.error('Please enter a valid numeric value for thal.')
            st.stop()
    
    # Code for Prediction
    heart_diagnosis = ''
    heart_prediction = None
    
    # Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
      
        if(heart_prediction is not None and heart_prediction[0] == 1):
            heart_diagnosis = 'The Person is Having Heart Disease'
        else:
            heart_diagnosis = 'The Person is Not Having Heart Disease'
        
        st.success(heart_diagnosis)
     
     
    
# Parkinson's Disease Test page
if selected == 'Parkinsons Test':
    # Page title
    st.title('Parkinsons Testing Using ML')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
        
    with col3:
         flo = st.text_input('MDVP:Flo(Hz)')
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col1:    
        RAP = st.text_input('MDVP:RAP')
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col3:
        DDP = st.text_input('Jitter:DDP')
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col1:
         APQ3 = st.text_input('Shimmer:APQ3')
        
    with col2:    
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
         DDA = st.text_input('Shimmer:DDA')
        
    with col5:    
        NHR = st.text_input('NHR')
        
    with col1:
        HNR = st.text_input('HNR') 
        
    with col2:
         RPDE = st.text_input('RPDE')
        
    with col3:    
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:    
        spread2 = st.text_input('spread2')
        
    with col1:
        D2 = st.text_input('D2') 
        
    with col2:
         PPE = st.text_input('PPE')
        
    
      #code for Prediction
    parkinsons_diagnosis = ''
    #parkinsons_prediction = None
      
      #creating a button for prediction
      
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if(parkinsons_prediction[0]==1):
              parkinsons_diagnosis = 'The Person is Having Parkinsons Disease'
        else:
              parkinsons_diagnosis = 'The Person is Not Having Parkinsons Disease'
          
        st.success(parkinsons_diagnosis)    
    
