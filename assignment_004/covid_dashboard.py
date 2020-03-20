import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('data/covid_19_data.csv')

def cleanData(data):

  # casting types.. 
  df['ObservationDate'] = pd.to_datetime(df['ObservationDate'])
  df['Province/State'] = df['Province/State'].astype('category')
  df['Country/Region'] = df['Country/Region'].astype('category')
  df['Last Update'] = pd.to_datetime(df['Last Update'])
  df['Confirmed'] = df['Confirmed'].astype('int64')
  df['Deaths'] = df['Deaths'].astype('int64')
  df['Recovered'] = df['Recovered'].astype('int64')

  # split last update into date n time...
  df['last_update_date'] = df['Last Update'].dt.date
  df['last_update_time'] = df['Last Update'].dt.time

  # drop 'sNo', 'Last Update' column....
  return df.drop(columns=['SNo', 'Last Update'])

df = cleanData(df)

dropdown_values = { country_region for country_region in df['Country/Region'] }

app.layout = dhtml.Div(children=[
    dhtml.H1(children='Covid 19'),

    dhtml.Div(children='''
        Covid Dashboard....
    '''),
    dhtml.Br(),
    
    dcc.Dropdown(
      id='country_dropdown',
      options = [
        { 'label': cr, 'value': cr }
        for cr in dropdown_values
      ],
      placeholder = 'Select a Country/Region'
    ),
    dhtml.Div(id='chart_by_region')
])

@app.callback(
  Output('chart_by_region', 'children'),
  [Input('country_dropdown', 'value')]
)  

def update_figure(selected_country_region):
  filtered_df = df[df['Country/Region'] == selected_country_region]
  filtered_df = filtered_df.drop(columns=['ObservationDate', 'Province/State', 'Country/Region', 'last_update_time'])
  filtered_df = filtered_df.groupby('last_update_date').sum()
  print(filtered_df.head(10))
  return dcc.Graph(
      id="chart",
      figure={
        'data': [
          go.Scatter(
            x = filtered_df.index,
            y = filtered_df['Confirmed'],
            mode = 'lines+markers'
          )
        ],
        'layout' : go.Layout(
          title = 'Covid 19',
          xaxis = { 'title': 'Date' },
          yaxis = { 'title': 'Confirmed' },
          hovermode='closest'
        )
      }
    )

if __name__ == '__main__':
    app.run_server(debug=True)
