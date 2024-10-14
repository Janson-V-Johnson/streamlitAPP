import streamlit as st
import pandas as pd

def upload_and_preprocess():
    st.markdown('<h1 class="main-header">Upload & Preprocess Data</h1>', unsafe_allow_html=True)
    
    uploaded_file = st.file_uploader("Upload your CSV file", type="csv", help="Upload your dataset in CSV format.")
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.markdown('<h2 class="sub-header">Preview of Uploaded Data</h2>', unsafe_allow_html=True)
        st.dataframe(df.head())
        
        # Preprocessing steps
        st.markdown('<h2 class="sub-header">Data Preprocessing Options</h2>', unsafe_allow_html=True)
        
        if st.checkbox("Show Data Types"):
            st.write(df.dtypes)
        
        if st.checkbox("Handle Missing Values"):
            st.markdown("Before handling missing values:")
            st.write(df.isnull().sum())
            
            action = st.selectbox("Choose method to handle missing values", ["Drop Rows", "Fill with Mean", "Do Nothing"])
            
            if action == "Drop Rows":
                df = df.dropna()
            elif action == "Fill with Mean":
                df = df.fillna(df.mean(numeric_only=True))
        
        # Handling non-numeric columns
        st.markdown('<h2 class="sub-header">Handling Non-Numeric Columns</h2>', unsafe_allow_html=True)
        non_numeric_cols = df.select_dtypes(exclude=['number']).columns
        
        if len(non_numeric_cols) > 0:
            non_numeric_action = st.selectbox("How would you like to handle non-numeric columns?",
                                              ["Remove Non-Numeric Columns", "Attempt to Convert to Numeric", "Do Nothing"])
            
            if non_numeric_action == "Remove Non-Numeric Columns":
                df = df.drop(columns=non_numeric_cols)
            elif non_numeric_action == "Attempt to Convert to Numeric":
                for col in non_numeric_cols:
                    df[col] = pd.to_numeric(df[col], errors='coerce')
        
        return df
    return None
