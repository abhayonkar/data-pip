import streamlit as st
import requests as req
import altair as alt

resp = req.get('https://data.nasa.gov/resource/y77d-th95.json')
product_data = resp.json()

groceries = []

for product in product_data:
    if product.get('fall') == 'Fell':
        groceries.append(product)

# Convert the data to pandas DataFrame
import pandas as pd

df = pd.DataFrame(groceries)

# Start the Streamlit app
st.title('Meteorite Data')
st.write('This app displays a bar chart of the name and mass (g) of the meteorites that fell.')

# Create a bar chart
chart = alt.Chart(df).mark_bar().encode(
    x='name:N',
    y='mass (g):Q'
)

st.altair_chart(chart, use_container_width=True)
