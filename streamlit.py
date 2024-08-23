from pydov.search.grondwaterfilter import GrondwaterFilterSearch
gwfilter = GrondwaterFilterSearch()
from owslib.fes2 import PropertyIsEqualTo

query = PropertyIsEqualTo(
            propertyname='pkey_filter',
            literal='https://www.dov.vlaanderen.be/data/filter/1979-006377')


df = gwfilter.search(query=query)
df['year'] = df['datum'].apply(lambda x: str(x.year))
from matplotlib.dates import MonthLocator, YearLocator, DateFormatter
from matplotlib.ticker import MaxNLocator, MultipleLocator
import streamlit as st
import matplotlib.pyplot as plt

# Get height of ground surface
ground_surface = df["mv_mtaw"][0]

# create a plot with 2 subplots
fig = plt.figure(figsize=(12, 6))

# Plot entire time series in the upper plot
df['peil_mtaw'].plot()

st.pyplot(fig)
