import pandas as pd
import dash_core_components as dcc
import plotly.graph_objs as go

from tmapkey import my_token 

#-- create map ---------------------------------------------

def us_map(data, geo_states):

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
    mapbox_style="dark", mapbox_accesstoken=my_token(), mapbox_zoom=3, mapbox_center = {"lat": 37.0902, "lon": -95.7129}
  )
  fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

  return dcc.Graph(figure=fig)