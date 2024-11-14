# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 16:27:58 2024

@author: Admin
"""

import pandas as pd
import numpy as np
import pickle5 as pickle
import streamlit as st

file1 = open('Titanic.pkl', 'rb')
Logi = pickle.load(file1)
file1.close()

st.title("Titanic Survivor")

Name=st.text_input("Name")

Age=st.number_input("Age in year")

Sex=st.selectbox("Gender",['Male','Female'])

SibSp=st.select_slider('No of siblings or spouse accompnying',options=range(0,9))

Parch=st.select_slider('No of parents or children accompanying',options=range(0,7))

Fare=st.number_input('Enter the Amount paid in $')

Pclass=st.selectbox('Enter the passenger class',['I','II','III'])

Embarkment=st.selectbox('Enter the port of Embarkment',['S','C','Q'])


if st.button('Likelihood of survival'):
    if Sex=='Male':
        add='Mr'
    else:
        add='Mrs'	       
      
    if Sex=='Male':
    	Sex=1
    else:
        Sex=0
        
        
    if Parch >0:
        Parch=1
    else:
        Parch=0
        
        
    if Pclass=='I':
        Pc_1=1
    else:
        Pc_1=0
        
    if Pclass=='II':
        Pc_2=1
    else:
        Pc_2=0
        
    if Pclass=='I':
        Pc_3=1
    else:
        Pc_3=0
        
        
    if Embarkment=='S':
        Em_S=1
    else:
        Em_S=0
        
        
    if Embarkment=='C':
    	Em_C=1
    else:
        Em_C=0 
       
       
    if Embarkment=='Q':
    	Em_Q=1
    else:
        Em_Q=0
        
    Age=int(Age)

    
       
    query=np.array([Sex,Age,SibSp,Parch,Fare,Pc_1,Pc_2,Pc_3,Em_C,Em_Q,Em_S])
        
        
    query=query.reshape(1,11)    
   
   
    prediction=Logi.predict(query)[0]
   
    if prediction ==1:
    	res='alive'
    else:
    	res='dead'
   
    st.title(add+' '+Name+" is most likely "+ res)
    
