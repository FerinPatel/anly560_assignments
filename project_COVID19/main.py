import dash
import dash_bootstrap_components as dbc

import pandas as pd
import json
import requests

import layout

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

#-- fetch COVID data -----------------------------------------------------------------------------
response_coivd = requests.get('https://covidtracking.com/api/states/daily')
data = json.loads(response_coivd.text)
data = response_coivd.json()

#-- fetch geoJSON for map -----------------------------------------------------------------------------
response_geoData = requests.get('https://raw.githubusercontent.com/mapbox/geojson-vt/master/test/fixtures/us-states.json')
geo_states = json.loads(response_geoData.text)
geo_states = response_geoData.json()

#-- app layout ----------------------------------------------------------------
app.layout = layout.app_layout(data, geo_states)
  
if __name__ == '__main__':
  app.run_server(debug=True)