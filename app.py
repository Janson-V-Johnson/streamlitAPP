import streamlit as st
import pandas as pd
from data_processing import upload_and_preprocess
from simple_analysis import show_basic_analysis
from visualization import show_visualizations, perform_eda

# Set page layout and title
st.set_page_config(page_title="Data Explorer", layout="wide", initial_sidebar_state="expanded")

# Sidebar for global actions
st.sidebar.header("Data Explorer App")
st.sidebar.markdown("""
    This app allows you to:
    - Upload a CSV file
    - Preprocess the data
    - Perform basic data analysis
    - Visualize the data with various plots
""")

# Main Tabs for Each Module
tabs = st.tabs(["Upload & Preprocessing", "Simple Data Analysis", "Exploratory Data Analysis (EDA)", "Visualizations"])

# Global Variables (for reusability across tabs)
uploaded_file = None
df = None

# Module 1: Upload & Preprocessing Tab
with tabs[0]:
    df = upload_and_preprocess()

# Module 2: Simple Data Analysis Tab
with tabs[1]:
    if df is not None:
        show_basic_analysis(df)

# Module 3: Exploratory Data Analysis (EDA) Tab
with tabs[2]:
    if df is not None:
        perform_eda(df)

# Module 4: Visualizations Tab
with tabs[3]:
    if df is not None:
        show_visualizations(df)
