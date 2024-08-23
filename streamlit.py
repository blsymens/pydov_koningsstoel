from matplotlib.dates import MonthLocator, YearLocator, DateFormatter
from matplotlib.ticker import MaxNLocator, MultipleLocator
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

# Create a Plotly figure
fig = go.Figure()

# Plot entire time series
fig.add_trace(
    go.Scatter(x=df.index, y=df['peil_mtaw'], mode='lines', name='peil_mtaw')
)

# Update layout
fig.update_layout(
    title='Time Series Plot of peil_mtaw',
    xaxis_title='Date',
    yaxis_title='peil_mtaw',
    height=600,
    width=800
)

st.pyplot(fig)
