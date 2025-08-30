import streamlit as st
import pandas as pd
import pickle

# Load model
with open("model.pkl","rb") as f:
    model=pickle.load(f)

# Load encoders
with open("label_encoders.pkl","rb") as f:
    label_encoders=pickle.load(f)

st.title("✈️ Flight Price Prediction App")

# Load dataset just to know feature columns
df=pd.read_csv("cleaned_dataset.csv")
feature_columns=[col for col in df.columns if col!="price"]

user_input={}

for col in feature_columns:
    if col in label_encoders:  
        user_input[col]=st.selectbox(col,list(label_encoders[col].classes_))
    else:
        # Numeric input
        default_val=int(df[col].median()) if pd.api.types.is_numeric_dtype(df[col]) else 0
        user_input[col]=st.number_input(col,value=default_val)

# Convert to DataFrame
input_data=pd.DataFrame([user_input])

# Encode categorical columns
for col in label_encoders:
    input_data[col]=label_encoders[col].transform(input_data[col])

if st.button("Predict Price"):
    prediction=model.predict(input_data)[0]
    st.success(f"Estimated Flight Price: ₹ {int(prediction):,}")
