import pandas as pd
import json
import requests

from  app import app
from layout import app_layout

#-- fetch COVID data -----------------------------------------------------------------------------
response_coivd = requests.get('https://covidtracking.com/api/states/daily')
data = json.loads(response_coivd.text)
data = response_coivd.json()

#-- fetch geoJSON for map -----------------------------------------------------------------------------
response_geoData = requests.get('https://raw.githubusercontent.com/mapbox/geojson-vt/master/test/fixtures/us-states.json')
geo_states = json.loads(response_geoData.text)
geo_states = response_geoData.json()

#-- app layout ----------------------------------------------------------------
app.layout = app_layout(data, geo_states)

#-- export data func ----------------------------------------------------------
def retreive_data():
  return data

if __name__ == '__main__':
  app.run_server(debug=True)