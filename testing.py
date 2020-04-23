import plotly.graph_objects as go
import pandas as pd
import json
import plotly.express as px

df = pd.read_excel('DiabetesAtlasCountyData_excel.xlsx', usecols=['Fips', 'Percentage'], dtype={'Fips': str})

with open('counties_locations.json') as response:
    counties = json.load(response)

# counties = df['CountyFIPS'].tolist()
# percents= df['Percentage'].tolist()


fig = go.Figure(data=go.Choropleth(
    locations=df['Fips'], # Spatial coordinates
    z = df['Percentage'], # Data to be color-coded
    geojson = counties, # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Diabetes %"
))

fig.update_layout(
    title_text = "USA by Diabetes %", 
    geo_scope = 'usa'
)

# fig = px.choropleth(df, geojson=counties, locations='Fips', color='Percentage',
#                            color_continuous_scale="Viridis",
#                            range_color=(0, 80),
#                            scope="usa", 
#                            labels={'Percentage':'percent with diabetes'}
                        #   ) 
# fig = px.choropleth(df, geojson=counties, locations='Fips', z='Percentage')
# fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()

# # Metadata
# fig.update_layout(
#     title_text = 'Diabetes Frequency by County',
#     geo_scope='usa', # limite map scope to USA
# )

# fig.show()

#https://plotly.com/python/choropleth-maps/