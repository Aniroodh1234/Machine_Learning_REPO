import streamlit as st
import pandas as pd

st.title("This is streamlit web app")

name = st.text_input("ENter you Name: ")
st.write(f"Helllo {name}")

age = st.slider("Enter your age: ",0,100,25)
st.write(f"Your age is {age}")

options = ["Python", "Java", "C++", "JavaScript"]
choice = st.selectbox("choose your favourite subject: ",options)
st.write(f"You selected {choice}")

data = {
    "Name": ["John", "Jane", "Jake", "Jill"],
    "Age": [28, 24, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("choose a file: ",type = 'csv')
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.write(df)
