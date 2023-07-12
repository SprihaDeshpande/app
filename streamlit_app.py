import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title('Spreadsheet Analysis')

# Upload the spreadsheet file
uploaded_file = st.file_uploader('Upload a spreadsheet (Excel or CSV)', type=['xlsx', 'csv'])

if uploaded_file is not None:
    try:
        # Read the uploaded file
        df = pd.read_excel(uploaded_file)  # For Excel files
        # df = pd.read_csv(uploaded_file)  # For CSV files

        # Display the raw data if requested
        if st.checkbox('Show raw data'):
            st.subheader('Raw data')
            st.write(df)

        # Plot a graph
        st.subheader('Graph')
        x_column = st.selectbox('Select the X-axis column', df.columns)
        y_column = st.selectbox('Select the Y-axis column', df.columns)
        graph_type = st.selectbox('Select the graph type', ['line', 'bar', 'scatter'])

        plt.figure()
        if graph_type == 'line':
            plt.plot(df[x_column], df[y_column])
        elif graph_type == 'bar':
            plt.bar(df[x_column], df[y_column])
        elif graph_type == 'scatter':
            plt.scatter(df[x_column], df[y_column])

        plt.xlabel(x_column)
        plt.ylabel(y_column)
        plt.title(f'{graph_type.capitalize()} plot of {x_column} vs {y_column}')
        plt.xticks(rotation=45)
        st.pyplot(plt)

    except Exception as e:
        st.error(f'Error: {e}')

