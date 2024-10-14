import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D  # For 3D plotting

def perform_eda(df):
    st.markdown('<h1 class="main-header">Exploratory Data Analysis (EDA)</h1>', unsafe_allow_html=True)
    
    all_columns = df.columns.tolist()
    selected_columns = st.multiselect("Select columns for EDA", all_columns, default=all_columns)
    
    row_start, row_end = st.slider("Select row range", 0, len(df), (0, len(df)))
    filtered_df = df.loc[row_start:row_end, selected_columns]
    st.dataframe(filtered_df.head())

    numeric_cols = filtered_df.select_dtypes(include=['float64', 'int64']).columns.tolist()
    
    if len(numeric_cols) > 1:
        corr_matrix = filtered_df[numeric_cols].corr()
        sns.set(style="whitegrid")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", cbar=True, linewidths=.5, ax=ax)
        st.pyplot(fig)
        plt.clf()
    else:
        st.write("Not enough numeric columns for a correlation matrix.")

def show_visualizations(df):
    st.markdown('<h1 class="main-header">Visualize the Data</h1>', unsafe_allow_html=True)
    
    plot_type = st.selectbox("Choose a plot type", ["Scatter Plot", "Line Plot", "Bar Plot", "Histogram", "Violin Plot", "3D Scatter Plot"])
    x_axis = st.selectbox("Select X-axis", df.columns)
    y_axis = st.selectbox("Select Y-axis", df.columns)

    # Optionally ask for a Z-axis if a 3D scatter plot is selected
    if plot_type == "3D Scatter Plot":
        z_axis = st.selectbox("Select Z-axis", df.columns)

    fig, ax = plt.subplots(figsize=(10, 6))  # Explicitly create figure and axes

    sns.set(style="darkgrid")
    
    if plot_type == "Scatter Plot":
        sns.scatterplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif plot_type == "Line Plot":
        sns.lineplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif plot_type == "Bar Plot":
        sns.barplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif plot_type == "Histogram":
        sns.histplot(df[x_axis], bins=20, ax=ax)
    elif plot_type == "Violin Plot":
        sns.violinplot(data=df, x=x_axis, y=y_axis, ax=ax)
    elif plot_type == "3D Scatter Plot":
        fig = plt.figure(figsize=(10, 6))
        ax = fig.add_subplot(111, projection='3d')  # Add 3D subplot
        ax.scatter(df[x_axis], df[y_axis], df[z_axis], c='r', marker='o')
        ax.set_xlabel(x_axis)
        ax.set_ylabel(y_axis)
        ax.set_zlabel(z_axis)
        plt.title(f'3D Scatter Plot: {x_axis} vs {y_axis} vs {z_axis}')

    st.pyplot(fig)
    plt.clf()
