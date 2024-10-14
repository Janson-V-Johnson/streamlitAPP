import streamlit as st

def show_basic_analysis(df):
    st.markdown('<h1 class="main-header">Simple Data Analysis</h1>', unsafe_allow_html=True)
    
    st.markdown('<h2 class="sub-header">Basic Data Statistics</h2>', unsafe_allow_html=True)
    st.write(df.describe())
    
    st.markdown('<h2 class="sub-header">Column-wise Analysis</h2>', unsafe_allow_html=True)
    column = st.selectbox("Select a column for analysis", df.columns)
    st.write(f"Statistics for column `{column}`:")
    st.write(df[column].describe())
    
    if st.checkbox("Show Unique Values for Categorical Columns"):
        cat_columns = df.select_dtypes(include=['object', 'category']).columns
        if len(cat_columns) > 0:
            selected_cat_col = st.selectbox("Select a categorical column", cat_columns)
            st.write(f"Unique values in `{selected_cat_col}`: {df[selected_cat_col].unique()}")
        else:
            st.write("No categorical columns found.")
