import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import json


st.markdown("<h1 style='text-align: center'>NOC Wage Finder</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center'>Wages in Canadian dollar</h6>", unsafe_allow_html=True)

merged = pd.read_csv('wage_noc_2016_2021.csv')

merged['noc_2016'] = merged['noc_2016'].astype(str)
# Fill string values with leading zeros
merged['noc_2016'] = merged['noc_2016'].str.zfill(4)
# Convert to integer to get rid of decimal. Use Int64 to transform null values
merged['noc_2021'] = merged['noc_2021'].astype('Int64')
merged['noc_2021'] = merged['noc_2021'].astype(str)


# Select NOC version
noc_versions = ('2016', '2021')
selected_noc_version = st.selectbox('Select NOC version', noc_versions)

# Find NOC Title
def load_noc_titles(selected_noc_version):
    if selected_noc_version == '2016':
        noc_titles = sorted([''] + list(merged[(merged['noc_version'] == '2016') | (merged['noc_version'] == '2016, 2021')]['noc_title_2016'].unique()))
    else:
        noc_titles = sorted([''] + list(merged[merged['noc_version'] == '2016, 2021']['noc_title_2021'].unique()))
    return noc_titles

# Select NOC Title (after selecting NOC version)
noc_titles = load_noc_titles(selected_noc_version)
selected_noc_title = st.selectbox('Select NOC title', noc_titles)


#Choropleth Map Plotly
with open("canada_provinces.geojson", 'r') as f:
    geojson = json.load(f)


if selected_noc_version == '2016':

    fig = go.Figure(data=go.Choropleth(
    locations= merged[merged['noc_title_2016'] == selected_noc_title]['prov'],
    geojson= geojson,
    z= merged[merged['noc_title_2016'] == selected_noc_title]['median_wage'],
    locationmode = 'geojson-id',
    featureidkey= 'properties.name',
    colorscale = 'Teal',
    colorbar_title = "Median Wage",
    hovertext= merged[merged['noc_title_2016'] == selected_noc_title]['text']))

else:

    fig = go.Figure(data=go.Choropleth(
    locations= merged[merged['noc_title_2021'] == selected_noc_title]['prov'],
    geojson= geojson,
    z= merged[merged['noc_title_2021'] == selected_noc_title]['median_wage'],
    locationmode = 'geojson-id',
    featureidkey= 'properties.name',
    colorscale = 'Teal',
    colorbar_title = "Median Wage",
    hovertext= merged[merged['noc_title_2021'] == selected_noc_title]['text']))

fig.update_layout(geo_scope='north america',
margin={"r":0,"t":0,"l":0,"b":0})

fig.update_geos(fitbounds='locations', visible=True)

# Output Skill Level or Teer Category
col1, col2, col3, col4 = st.columns(4)

if selected_noc_version == '2016':
    skill_level = merged.loc[merged['noc_title_2016'] == selected_noc_title, 'skill_level']
    if not skill_level.empty:
        col1.metric("Skill level",  skill_level.iloc[0])
    elif selected_noc_title != '':
        col1.write("No skill level found for this NOC title")

else:
    teer_category = merged.loc[merged['noc_title_2021'] == selected_noc_title, 'teer_category']
    teer_category = teer_category.astype(int)
    if not teer_category.empty:
        col1.metric("Teer Category", teer_category.iloc[0])
    elif selected_noc_title != '':
        col1.write("No teer category found for this NOC title")

# Display plotly Choropleth map
st.plotly_chart(fig, use_container_width=True)



# # Output Dataframe of data selected

# merged.rename(columns={'noc_title_2016': 'NOC Title 2016', \
#     'noc_title_2021': 'NOC Title 2021', 'prov': 'Province'})

# # data = pd.DataFrame()
# if selected_noc_title != '':
#     # Output Dataframe of data selected
#     if selected_noc_version == '2016':
#         data = merged[merged['noc_title_2016'] == selected_noc_title]
#     else:
#         data = merged[merged['noc_title_2021'] == selected_noc_title]
#     st.dataframe(data.head())