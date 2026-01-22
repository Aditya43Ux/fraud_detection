import streamlit as st
import pandas as pd
import sys

# Fix for scikit-learn version mismatch
import sklearn.compose._column_transformer
import sklearn.preprocessing._encoders

# Patch 1: _RemainderColsList
class _RemainderColsList(list):
    pass

sklearn.compose._column_transformer._RemainderColsList = _RemainderColsList
sys.modules['sklearn.compose._column_transformer']._RemainderColsList = _RemainderColsList

# Patch 2: Fix OneHotEncoder sparse attribute
from sklearn.preprocessing import OneHotEncoder

original_getattribute = OneHotEncoder.__getattribute__

def patched_getattribute(self, name):
    if name == 'sparse':
        return original_getattribute(self, 'sparse_output')
    return original_getattribute(self, name)

OneHotEncoder.__getattribute__ = patched_getattribute

# Now load the model
import joblib
model = joblib.load("C:/Users/Goku/Downloads/Fraud_detection_pipline (2).pkl")

st.title("Fraud Detection Application")
st.markdown("Please enter the transaction details and use the predict button")
st.divider()

transaction_type = st.selectbox("Transaction Type", ["PAYMENT", "TRANSFER", "CASH_OUT", "DEBIT"])
amount = st.number_input("Amount", min_value=0.0, value=1000.0)
oldbalanceOrg = st.number_input("Old Balance (Sender)", min_value=0.0, value=10000.0)
newbalanceOrig = st.number_input("New Balance (Sender)", min_value=0.0, value=9000.0)
oldbalanceDest = st.number_input("Old Balance (Receiver)", min_value=0.0, value=0.0)
newbalanceDest = st.number_input("New Balance (Receiver)", min_value=0.0, value=0.0)

if st.button("Predict"):
    input_data = pd.DataFrame({
        'type': [transaction_type],
        'amount': [amount],
        'oldbalanceOrg': [oldbalanceOrg],
        'newbalanceOrig': [newbalanceOrig],
        'oldbalanceDest': [oldbalanceDest],
        'newbalanceDest': [newbalanceDest]
    })

    prediction = model.predict(input_data)

    st.subheader(f"Prediction Result: {int(prediction[0])}")
    
    if prediction[0] == 1:
        st.error("⚠️ This transaction is FRAUDULENT")
    else:
        st.success("✅ This transaction is LEGITIMATE")