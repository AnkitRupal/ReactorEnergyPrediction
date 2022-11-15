import streamlit as st
import numpy as np
import os
import pickle

st. set_page_config(layout="wide")

@st.cache(allow_output_mutation=True)
def load_data():
    dirname = os.path.abspath("")
    filename1 = os.path.join(dirname, 'model.pkl')

    parameters = pickle.load(open(filename1, 'rb'))
    return parameters



model_data = load_data()



def predict(temperature,vacuum,pressure,humidity):
    inp = [temperature,vacuum,pressure,humidity,1.0]
    return round(np.matmul(model_data,inp),2)



st.title('REACTOR ENERGY ESTIMATION')

temperature = st.slider(label = "Temperature", min_value = 1.00, max_value = 40.00,value = 20.00,step = 0.01)

vacuum = st.slider(label = "Vacuum", min_value = 25.00, max_value = 80.00,value = 54.00,step = 0.01)

pressure = st.slider(label = "Pressure", min_value = 992.00, max_value = 1035.00,value = 1015.00,step = 0.01)

humidity = st.slider(label = "Humidity", min_value = 25.00, max_value = 100.00,value = 75.00,step = 0.01)

st.write("The estimated energy output is :", predict(temperature,vacuum,pressure,humidity))
