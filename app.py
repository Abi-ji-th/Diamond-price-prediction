import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_model():
    return joblib.load('diamond_model.joblib')

model = load_model()

st.set_page_config(page_title="Diamond Price Predictor", page_icon="💎")
st.title("💎 Diamond Price Predictor")
st.write("Enter the characteristics of a diamond to estimate its price!")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Categorical Features")
    cut = st.selectbox("Cut", ['Ideal', 'Premium', 'Very Good', 'Good', 'Fair'])
    color = st.selectbox("Color (D is best, J is worst)", ['D', 'E', 'F', 'G', 'H', 'I', 'J'])
    clarity = st.selectbox("Clarity (IF is best, I1 is worst)",
                           ['IF', 'VVS1', 'VVS2', 'VS1', 'VS2', 'SI1', 'SI2', 'I1'])

with col2:
    st.subheader("Physical Measurements")
    carat = st.number_input("Carat Weight", min_value=0.1, max_value=5.0, value=1.0, step=0.1)
    depth = st.number_input("Depth %", min_value=40.0, max_value=80.0, value=61.5)
    table = st.number_input("Table %", min_value=40.0, max_value=80.0, value=57.0)

st.subheader("Dimensions (mm)")
col3, col4, col5 = st.columns(3)
with col3:
    x = st.number_input("Length (x)", min_value=0.0, max_value=15.0, value=6.5)
with col4:
    y = st.number_input("Width (y)", min_value=0.0, max_value=15.0, value=6.5)
with col5:
    z = st.number_input("Depth (z)", min_value=0.0, max_value=10.0, value=4.0)

if st.button("Predict Price", type="primary"):
    input_data = pd.DataFrame({
        'carat': [carat], 'cut': [cut], 'color': [color], 'clarity': [clarity],
        'depth': [depth], 'table': [table], 'x': [x], 'y': [y], 'z': [z]
    })
    prediction = model.predict(input_data)[0]
    st.success(f"### Estimated Price: ${prediction:,.2f}")
    st.balloons()