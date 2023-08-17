import pandas as pd
import numpy as np
import streamlit as st
import pickle
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')



st.title("Salary Predictons web application")

# Load the model
model=pickle.load(open('RandomForest.pkl', 'rb'))


def main():
    age=st.number_input('age',min_value=17,max_value=90,value=17)
    workclass=st.selectbox('Select Work Class',[' State-gov', ' Self-emp-not-inc', ' Private', ' Federal-gov',
       ' Local-gov', 'Others', ' Self-emp-inc', ' Without-pay',
       ' Never-worked'])
    if workclass==' State-gov':
        workclass_1=0
    elif workclass==' Self-emp-not-inc':
        workclass_1=1   
    elif workclass==' Private':
        workclass_1=2
    elif workclass==' Federal-gov':
        workclass_1=3
    elif workclass==' Local-gov':
        workclass_1=4
    elif workclass=='Others':
        workclass_1=5
    elif workclass==' Self-emp-inc':
        workclass_1=6
    elif workclass==' Without-pay':
        workclass_1=7
    
    fnlwgt=st.number_input('select fnweight from',min_value=12285,max_value=1484705,value=12285)
    education=st.selectbox('Select Education',[' Bachelors', ' HS-grad', ' 11th', ' Masters', ' 9th',
       ' Some-college', ' Assoc-acdm', ' Assoc-voc', ' 7th-8th',
       ' Doctorate', ' Prof-school', ' 5th-6th', ' 10th', ' 1st-4th',
       ' Preschool', ' 12th'])
    if education==' Bachelors':
        education_1=0 
    elif education==' HS-grad':
        education_1=1
    elif education==' 11th':
        education_1=2
    elif education==' Masters':
        education_1=3
    elif education==' 9th':
        education_1=4
    elif education==' Some-college':
        education_1=5
    elif education==' Assoc-acdm':
        education_1=6
    elif education==' Assoc-voc':
        education_1=7
    elif education==' 7th-8th':
        education_1=8
    elif education==' Doctorate':
        education_1=9
    elif education==' Prof-school':
        education_1=10
    elif education==' 5th-6th':
        education_1=11
    elif education==' 10th':
        education_1=12
    elif education==' 1st-4th':
        education_1=13
    elif education==' Preschool':
        education_1=14
    elif education==' 12th':
        education_1=15
    education_num=st.number_input('education numbers',min_value=1,max_value=16,value=1)
    marital_status=st.selectbox('marital status',[' Never-married', ' Married-civ-spouse', ' Divorced',
       ' Married-spouse-absent', ' Separated', ' Married-AF-spouse',
       ' Widowed'])
    if marital_status==' Never-married':
        marital_status_1=0
    elif marital_status==' Married-civ-spouse':
        marital_status_1=1
    elif marital_status==' Divorced':
        marital_status_1=2
    elif marital_status==' Married-spouse-absent':
        marital_status_1=3
    elif marital_status==' Separated':
        marital_status_1=4
    elif marital_status==' Married-AF-spouse':
        marital_status_1=5
    elif marital_status==' Widowed':
        marital_status_1=6
    occupation=st.selectbox('occupation',[' Adm-clerical', ' Exec-managerial', ' Handlers-cleaners',
       ' Prof-specialty', ' Other-service', ' Sales', ' Craft-repair',
       ' Transport-moving', ' Farming-fishing', ' Machine-op-inspct',
       ' Tech-support', ' Others', ' Protective-serv', ' Armed-Forces',
       ' Priv-house-serv'])
    if occupation==' Adm-clerical':
        occupation_1=0
    elif occupation==' Exec-managerial':
        occupation_1=1
    elif occupation==' Handlers-cleaners':
        occupation_1=2
    elif occupation==' Prof-specialty':
        occupation_1=3
    elif occupation==' Other-service':
        occupation_1=4
    elif occupation==' Sales':
        occupation_1=5
    elif occupation==' Craft-repair':
        occupation_1=6
    elif occupation==' Transport-moving':
        occupation_1=7
    elif occupation==' Farming-fishing':
        occupation_1=8
    elif occupation==' Machine-op-inspct':
        occupation_1=9
    elif occupation==' Tech-support':
        occupation_1=10
    elif occupation==' Others':
        occupation_1=11
    elif occupation==' Protective-serv':
        occupation_1=12
    elif occupation==' Armed-Forces':
        occupation_1=13
    elif occupation==' Priv-house-serv':
        occupation_1=14
    relationship=st.selectbox('relationship',[' Not-in-family', ' Husband', ' Wife', ' Own-child', ' Unmarried',
       ' Other-relative'])
    if relationship==' Not-in-family':
        relationship_1=0
    elif relationship==' Husband':
        relationship_1=1
    elif relationship==' Wife':
        relationship_1=2
    elif relationship==' Own-child':
        relationship_1=3
    elif relationship==' Unmarried':
        relationship_1=4
    elif relationship==' Other-relative':
        relationship_1=5
    race=st.selectbox('race',[' White', ' Black', ' Asian-Pac-Islander', ' Amer-Indian-Eskimo',
       ' Other'])
    if race==' White':
        race_1=0
    elif race==' Black':
        race_1=1
    elif race==' Asian-Pac-Islander':
        race_1=2
    elif race==' Amer-Indian-Eskimo':
        race_1=3
    elif race==' Other':
        race_1=4
    sex=st.selectbox('sex',[' Male', ' Female'])
    if sex==' Male':
        sex_1=0
    elif sex==' Female':
        sex_1=1
    capital_gain=st.number_input('capital_gain',min_value=0,max_value=99999,value=0)
    capital_loss=st.number_input('capital_loss',min_value=0,max_value=4356,value=0)
    hours_per_week=st.number_input('hours_per_week',min_value=1,max_value=99,value=1)
    native_country=st.selectbox('native_country',[' United-States', ' Cuba', ' Jamaica', ' India', ' Others', ' Mexico',
       ' South', ' Puerto-Rico', ' Honduras', ' England', ' Canada',
       ' Germany', ' Iran', ' Philippines', ' Italy', ' Poland',
       ' Columbia', ' Cambodia', ' Thailand', ' Ecuador', ' Laos',
       ' Taiwan', ' Haiti', ' Portugal', ' Dominican-Republic',
       ' El-Salvador', ' France', ' Guatemala', ' China', ' Japan',
       ' Yugoslavia', ' Peru', ' Outlying-US(Guam-USVI-etc)', ' Scotland',
       ' Trinadad&Tobago', ' Greece', ' Nicaragua', ' Vietnam', ' Hong',
       ' Ireland', ' Hungary', ' Holand-Netherlands'])
    if native_country==' United-States':
        native_country_1=0
    elif native_country==' Cuba':
        native_country_1=1
    elif native_country==' jamaica':
        native_country_1=2
    elif native_country==' India':
        native_country_1=3
    elif native_country==' Others':
        native_country_1=4
    elif native_country==' Mexico':
        native_country_1=5
    elif native_country==' South':
        native_country_1=6
    elif native_country==' Puerto-Rico':
        native_country_1=7
    elif native_country==' Honduras':
        native_country_1=8
    elif native_country==' England':
        native_country_1=9
    elif native_country==' Canada':
        native_country_1=10
    elif native_country==' Germany':
        native_country_1=11
    elif native_country==' Iran':
        native_country_1=12
    elif native_country==' Philippines':
        native_country_1=13
    elif native_country==' Italy':
        native_country_1=14
    elif native_country==' Poland':
        native_country_1=15
    elif native_country==' Columbia':
        native_country_1=16
    elif native_country==' Cambodia':
        native_country_1=17
    elif native_country==' Thailand':
        native_country_1=18
    elif native_country==' Ecuador':
        native_country_1=19
    elif native_country==' Laos':
        native_country_1=20
    elif native_country==' Taiwan':
        native_country_1=21
    elif native_country==' Haiti':
        native_country_1=22
    elif native_country==' Portugal':
        native_country_1=23
    elif native_country==' Dominican-Republic':
        native_country_1=24
    elif native_country==' El-Salvador':
        native_country_1=25
    elif native_country==' France':
        native_country_1=26
    elif native_country==' Guatemala':
        native_country_1=27
    elif native_country==' China':
        native_country_1=28
    elif native_country==' Japan':
        native_country_1=29
    elif native_country==' Yugoslavia':
        native_country_1=30
    elif native_country==' Peru':
        native_country_1=31
    elif native_country==' Outlying-US(Guam-USVI-etc)':
        native_country_1=32
    elif native_country==' Scotland':
        native_country_1=33
    elif native_country==' Trinadad&Tobago':
        native_country_1=34
    elif native_country==' Greece':
        native_country_1=35
    elif native_country==' Nicaragua':
        native_country_1=36
    elif native_country==' Vietnam':
        native_country_1=37
    elif native_country==' Hong':
        native_country_1=38
    elif native_country==' Ireland':
        native_country_1=39
    elif native_country==' Hungary':
        native_country_1=40
    elif native_country==' Holand-Netherlands':
        native_country_1=41
    if st.button("Predictions"):
        scaler=StandardScaler()
        data=[age, workclass_1, fnlwgt, education_1, education_num,
        marital_status_1, occupation_1, relationship_1, race_1, sex_1,
        capital_gain, capital_loss, hours_per_week, native_country_1]
        data=scaler.fit_transform([data])
        result=model.predict(data)
        if result==0:
            st.write("The salary likely to be less than 50k")
        else:
            st.write("The salary likely to be more than 50k")


if __name__=="__main__":
    main()


    





        
    
    
    
    
