# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache_data)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)









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

