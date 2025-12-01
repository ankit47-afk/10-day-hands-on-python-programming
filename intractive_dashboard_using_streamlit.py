import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- PAGE SETTINGS ---
st.set_page_config(page_title="Interactive Dashboard", layout="wide")

st.title("Interactive Data Dashboard")
st.write("This dashboard is built using Streamlit. You can upload your own dataset and explore it interactively.")

# --- DATA UPLOAD ---
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("File uploaded successfully!")

    st.subheader("Data Preview")
    st.dataframe(df.head())

    st.subheader(" Summary Statistics")
    st.write(df.describe())

    # --- SIDEBAR FILTERS ---
    st.sidebar.header("Filters")
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

    if len(numeric_columns) >= 2:
        x_axis = st.sidebar.selectbox("Select X-axis", numeric_columns)
        y_axis = st.sidebar.selectbox("Select Y-axis", numeric_columns)

        chart_type = st.sidebar.radio("Chart Type", ["Scatter Plot", "Line Chart", "Bar Chart"])

        # --- CHART GENERATION ---
        if chart_type == "Scatter Plot":
            fig = px.scatter(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")
        elif chart_type == "Line Chart":
            fig = px.line(df, x=x_axis, y=y_axis, title=f"{x_axis} over {y_axis}")
        else:
            fig = px.bar(df, x=x_axis, y=y_axis, title=f"{x_axis} vs {y_axis}")

        st.plotly_chart(fig, use_container_width=True)

    else:
        st.warning("Dataset must contain at least **two numeric columns** to create charts.")

else:
    st.info("Please upload a CSV file to begin.")
