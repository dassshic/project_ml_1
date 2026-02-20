import streamlit as st
import pandas as pd
import pickle
import os

st.title("Предсказание цены автомобиля")

@st.cache_resource
def load_model():
    current_dir = os.path.dirname(__file__)
    model_path = os.path.join(current_dir, 'model.pickle')

    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

model = load_model()

input_data = {}

st.write("Введите характеристики автомобиля:")

input_data['year'] = st.number_input("Год выпуска", min_value=1980, max_value=2025, value=2015)

input_data['km_driven'] = st.number_input("Пробег (км)", min_value=0, max_value=500000, value=50000)

input_data['mileage'] = st.number_input("Расход топлива (км/л)", min_value=5.0, max_value=30.0, value=18.0)

input_data['engine'] = st.number_input("Объем двигателя (сс)", min_value=500, max_value=5000, value=1200)

input_data['max_power'] = st.number_input("Мощность (л.с.)", min_value=30, max_value=1000, value=80)

name = st.selectbox(
    "Модель автомобиля",
    ['Maruti Alto LXi', 'Maruti Swift Dzire VDI', 'Maruti Swift VDI', 'Maruti Swift VDI BSIV', 'Other']
)

for n in ['name_Maruti Alto LXi', 'name_Maruti Swift Dzire VDI', 'name_Maruti Swift VDI', 'name_Maruti Swift VDI BSIV', 'name_other']:
    input_data[n] = 0

if name == 'Maruti Alto LXi':
    input_data['name_Maruti Alto LXi'] = 1
elif name == 'Maruti Swift Dzire VDI':
    input_data['name_Maruti Swift Dzire VDI'] = 1
elif name == 'Maruti Swift VDI':
    input_data['name_Maruti Swift VDI'] = 1
elif name == 'Maruti Swift VDI BSIV':
    input_data['name_Maruti Swift VDI BSIV'] = 1
else:
    input_data['name_other'] = 1

fuel = st.radio("Тип топлива", ['Petrol', 'Diesel', 'LPG'])

for f in ['fuel_Diesel', 'fuel_LPG', 'fuel_Petrol']:
    input_data[f] = 0

if fuel == 'Diesel':
    input_data['fuel_Diesel'] = 1
elif fuel == 'LPG':
    input_data['fuel_LPG'] = 1
else:
    input_data['fuel_Petrol'] = 1

seller = st.selectbox("Продавец", ['Individual', 'Trustmark Dealer'])

input_data['seller_type_Individual'] = 1 if seller == 'Individual' else 0
input_data['seller_type_Trustmark Dealer'] = 1 if seller == 'Trustmark Dealer' else 0

transmission = st.radio("Коробка передач", ['Manual', 'Automatic'])

input_data['transmission_Manual'] = 1 if transmission == 'Manual' else 0

owner = st.selectbox(
    "Владелец",
    ['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car']
)

for o in ['owner_Fourth & Above Owner', 'owner_Second Owner', 'owner_Test Drive Car', 'owner_Third Owner']:
    input_data[o] = 0

if owner == 'Second Owner':
    input_data['owner_Second Owner'] = 1
elif owner == 'Third Owner':
    input_data['owner_Third Owner'] = 1
elif owner == 'Fourth & Above Owner':
    input_data['owner_Fourth & Above Owner'] = 1
elif owner == 'Test Drive Car':
    input_data['owner_Test Drive Car'] = 1

seats = st.selectbox("Количество мест", [4, 5, 6, 7, 8, 9, 10, 14])

for s in ['seats_4', 'seats_5', 'seats_6', 'seats_7', 'seats_8', 'seats_9', 'seats_10', 'seats_14']:
    input_data[s] = 0

input_data[f'seats_{seats}'] = 1

if st.button("Предсказать цену"):
    input_df = pd.DataFrame([input_data])[feature_names]

    prediction = model.predict(input_df)[0]
    

    st.write("Предполагаемая цена:", round(prediction, 2))
