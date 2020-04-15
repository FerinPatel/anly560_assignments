import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.graph_objs as go

import pandas as pd

from main import retreive_data

data = pd.DataFrame(retreive_data())

def update_viewer(value):
  
  # -- filter data -------------------------
  data_per_state = data[data['state'] == value]
  data_per_state['date'] = [pd.to_datetime(d,  format='%Y%m%d').date() for d in data_per_state['date']]
  pos_value = 0 if len(data_per_state) == 0 else data_per_state.at[data_per_state.index[0],'positive']
  tested_value = 0 if len(data_per_state) == 0 else data_per_state.at[data_per_state.index[0],'totalTestResults']
  death_value = 0 if len(data_per_state) == 0 else data_per_state.at[data_per_state.index[0],'death']

  def pos_total():
    return dbc.Card(
      dbc.CardBody(
        [
          html.H4('Total Positive', className='card-title'),
          html.P(pos_value)
        ]
      ),
      style={"height": "8rem"}
    )

  def tested_total():
    return dbc.Card(
      dbc.CardBody(
        [
          html.P(f'Total Tested : {int(tested_value)}')
        ]
      ),
      style={"height": "4rem"}
    )

  def death_total():
    return dbc.Card(
      dbc.CardBody(
        [
          html.P(f'Total Deaths : {int(death_value)}')
        ]
      ),
      style={"height": "4rem"}
    )

  def state_graph():
    return dcc.Graph(
      id="graph_main",
      figure={
        'data': [
          go.Scatter(
            x = data_per_state['date'],
            y = data_per_state['positive'],
            mode = 'lines+markers',
            name = 'Positive'
          ),
          go.Scatter(
            x = data_per_state['date'],
            y = data_per_state['hospitalized'],
            mode = 'lines+markers',
            name = 'Hospitalized'
          ),
          go.Scatter(
            x = data_per_state['date'],
            y = data_per_state['death'],
            mode = 'lines+markers',
            name = 'Death'
          )
        ],
        'layout' : go.Layout(
          title = 'Positive | Hospitalized | Death',
          xaxis = { 'title': 'Date' },
          hovermode='closest'
        )
      }
    )

  def state_change_graph():
    pass

  pos_t = pos_total()
  death_t = death_total()
  tested_t = tested_total()
  graph_main = state_graph()

  return [pos_t, death_t, tested_t, graph_main]
  