import streamlit as st
import pandas as pd

st.title("Feature engineering demo app")

file_upload = st.file_uploader("Upload your dataset (csv)", type="csv")


if file_upload:
    df = pd.read_csv(file_upload)
else:
    st.info("Using default Titanic dataset")
    df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

option = st.radio("Select a preprocessing step:", (
    "None",
    "Fill Missing Values",
    "Encode Categorical Variables",
    "Scale Features"
))

if option == "Fill Missing Values":
    df.fillna(method='ffill', inplace=True)

elif option == "Encode Categorical Variables":
    df = pd.get_dummies(df)

elif option == "Scale Features":
    from sklearn.preprocessing import StandardScaler
    num_cols = df.select_dtypes(include='number').columns
    df[num_cols] = StandardScaler().fit_transform(df[num_cols])
    df[num_cols] = StandardScaler().fit_transform(df[num_cols])

st.write("Dataset Preview:")
st.dataframe(df)

