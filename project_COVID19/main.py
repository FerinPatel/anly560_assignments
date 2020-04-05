import dash 
import dash_core_components as dcc
import dash_html_components as html 
import dash_table as dt
from dash.dependencies import Input, Output 

import plotly.graph_objs as go 

import dash_bootstrap_components as dbc 

import pandas as pd
import json
import requests

import tmapkey

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#-- fetch COVID data -----------------------------------------------------------------------------
response_coivd = requests.get('https://covidtracking.com/api/states/daily')
data = json.loads(response_coivd.text)
data = response_coivd.json()

#-- fetch geoJSON for map -----------------------------------------------------------------------------
response_geoData = requests.get('https://raw.githubusercontent.com/mapbox/geojson-vt/master/test/fixtures/us-states.json')
geo_states = json.loads(response_geoData.text)
geo_states = response_geoData.json()

#-- create map ---------------------------------------------
filtered_dt = data
filtered_dt = pd.DataFrame(filtered_dt)
final_dt = (filtered_dt.loc[:, ['fips', 'totalTestResults']]).groupby('fips').sum()
  
fig = go.Figure(
  go.Choroplethmapbox( 
    geojson=geo_states, 
    locations=final_dt.index, 
    z=final_dt['totalTestResults'], 
    colorscale="Viridis",
    zmin=0, zmax=final_dt['totalTestResults'].max(),marker_opacity=0.5, marker_line_width=0
  )
)
fig.update_layout(
  mapbox_style="dark", mapbox_accesstoken=tmapkey.my_token(), mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129}
)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

#-- app layout ----------------------------------------------------------------
app.layout = dbc.Container([

  dbc.Row([
    dbc.Col(dcc.Graph(figure=fig))
  ]),

  dbc.Row([
    dbc.Col(dcc.Dropdown(
      id='state_list',
      options = [
        { 'label': dt['state'], 'value': dt['state'] }
        for dt in data
      ],
      placeholder = 'Select a state'
    ))
  ])

])

# @app.callback(
#   [Input('state_list', 'value')]
# )

#def update_map(selected_state):
  
if __name__ == '__main__':
  app.run_server(debug=True)