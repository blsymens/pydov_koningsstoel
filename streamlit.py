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
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 6),
                               sharex=False, sharey=True)

# Plot entire time series in the upper plot
df['peil_mtaw'].plot(ax=ax1, title='Water heads `Hoek Krekelbergstraat nr 2- Ploegsdijk`')
ax1.xaxis.set_major_locator(YearLocator(5))
ax1.xaxis.set_major_formatter(DateFormatter('%Y'))

# Plot the data for 2011 in the lower plot
df = df[df['year'] >= '2010']
df['peil_mtaw'].plot(ax=ax2,  title='Water heads `Hoek Krekelbergstraat nr 2- Ploegsdijk` year 2024')
ax2.xaxis.set_major_locator(MonthLocator(interval=3))
ax2.xaxis.set_major_formatter(DateFormatter('%Y-%m'))

# Adjust configuration of plot
for ax in (ax1, ax2):
    ax.set_xlabel('')
    ax.set_ylabel('head (mTAW)')
    for tick in ax.get_xticklabels():
        tick.set_rotation(0)
        tick.set_horizontalalignment('center')

    # Only draw spine between the y-ticks
    ax.spines['left'].set_position(('outward', 10))
    # Hide the right and top spines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_major_locator(MultipleLocator(0.2))

    # Add the ground surface (provided in the data) on the subplots
    ax.axhline(ground_surface, color = 'brown')
    ax.annotate('Ground surface',
             xy=(0.05, 0.68),
             xycoords='axes fraction',
             xytext=(-25, -15), textcoords='offset points',
             fontsize=12, color='brown')

fig.tight_layout(h_pad=5)
st.pyplot(fig)
