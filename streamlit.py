from matplotlib.dates import MonthLocator, YearLocator, DateFormatter
from matplotlib.ticker import MaxNLocator, MultipleLocator
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go
from pydov.search.grondwaterfilter import GrondwaterFilterSearch
from owslib.fes2 import PropertyIsEqualTo
import streamlit as st

gwfilter = GrondwaterFilterSearch()
query = PropertyIsEqualTo(
            propertyname='pkey_filter',
            literal='https://www.dov.vlaanderen.be/data/filter/1979-006377')

df = gwfilter.search(query=query)
df['year'] = df['datum'].apply(lambda x: str(x.year))
df.set_index('datum',inplace=True)

# Create a Plotly figure
fig = go.Figure()

# Plot entire time series
fig.add_trace(
    go.Scatter(x=df.index, y=df['peil_mtaw'], mode='lines', name='peil_mtaw')
)

maaiveld = df['mv_mtaw'].mean().round(1)

# Add a horizontal line at a given value
hline_value = maaiveld  # Replace with your desired value
fig.add_hline(
    y=hline_value,
    line_width=2,
    line_color="black",
    annotation_text=f"Maaiveld (mTAW) Line at {hline_value}",
    annotation_position="top left"
)

# Update layout
fig.update_layout(
    title='Time Series Plot of peil_mtaw',
    xaxis_title='Date',
    yaxis_title='peil_mtaw'
)

# Display the figure in Streamlit
st.plotly_chart(fig, use_container_width=True)
