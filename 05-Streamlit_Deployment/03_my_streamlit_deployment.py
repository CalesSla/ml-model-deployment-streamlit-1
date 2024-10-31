import streamlit as st
import os
import boto3
import pickle

bucket_name = "slavabucket1"

local_path = "LinearModel"
s3_prefix = "ml-models/LinearModel/"

s3 = boto3.client("s3")

def download_dir(local_path, s3_prefix):
    os.makedirs(local_path, exist_ok=True)
    paginator = s3.get_paginator("list_objects_v2")
    for result in paginator.paginate(Bucket=bucket_name, Prefix=s3_prefix):
        if "Contents" in result:
            for key in result["Contents"]:
                s3_key = key["Key"]
                local_file = os.path.join(local_path, os.path.relpath(s3_key, s3_prefix))
                s3.download_file(bucket_name, s3_key, local_file)

st.title("My Linear Model ")

button = st.button("Download Model")
if button:
    with st.spinner("Downloading... Please wait!"):
        download_dir(local_path, s3_prefix)

value1 = st.text_area("Enter Your Review", "10")
value2 = st.text_area("Enter Second Value", "10")
values = [[int(value1), int(value2)]]

predict = st.button("Predict")

with open('LinearModel/linear_regression_model.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
if predict:
    with st.spinner("Predicting..."):
        output = loaded_model.predict(values)
        st.write(output)
# st.info(output)