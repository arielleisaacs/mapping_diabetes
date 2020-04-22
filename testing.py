import plotly.graph_objects as go
import csv
import pandas as pd

import plotly.express as px

df = pd.read_csv('DiabetesAtlasCountyData.csv', usecols=['County', 'Percentage'])

counties = df['County'].tolist()
percents= df['Percentage'].tolist()



from urllib.request import urlopen
import json
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)


# fig = go.Figure(data=go.Choropleth(
#     locations=counties, # Spatial coordinates
#     z = percents, # Data to be color-coded
#     locationmode = 'USA-states', # set of locations match entries in `locations`
#     colorscale = 'Reds',
#     colorbar_title = "Population diagnosed with diabetes (%)",
# ))

fig = px.choropleth(df, geojson=counties, locations='County', color='Percentage',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           scope="usa",
                           labels={'Percentage':'percentage of people with diabetes'}
                          )
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# Metadata
# fig.update_layout(
#     title_text = 'Diabetes Frequency by County',
#     geo_scope='usa', # limite map scope to USA
# )

# fig.show()