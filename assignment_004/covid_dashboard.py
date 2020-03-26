import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.graph_objs as go
import dash_table as dt
from dash.dependencies import Input, Output

import dash_bootstrap_components as dbc 

import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

df_acc = pd.read_csv('data/us_covid19_daily.csv')
df_per_states = pd.read_csv('data/us_states_covid19_daily.csv')
df_states_abbr = pd.read_csv('data/state_abb.csv')

# casting types..
df_per_states['date'] = [pd.to_datetime(d,  format='%Y%m%d').date() for d in df_per_states['date']]
df_per_states['state'] = df_per_states['state'].astype('category')
df_states_abbr['State'] = df_states_abbr['State'].astype('category')
df_states_abbr['Abbreviation'] = df_states_abbr['Abbreviation'].astype('category')

# drop dateChecked...
df_per_states = df_per_states.drop(columns=['dateChecked'])

print(df_states_abbr.dtypes)

app.layout = dhtml.Div(children=[
    dhtml.H1(children='Covid 19 - USA'),

    dhtml.Div(children='''
      
    '''),
    dhtml.Br(),
    
    dcc.Dropdown(
      id='state_list',
      options = [
        { 'label': row[0], 'value': row[1] }
        for index, row in df_states_abbr.iterrows()
      ],
      placeholder = 'Select a US State'
    ),
    dbc.Container(
      dbc.Row([
        dbc.Col(dhtml.Div(id='chart'), width=6),
        dbc.Col(dhtml.Div(id='table'), width=6)
      ])
    )
])

@app.callback(
  [Output('chart', 'children'),Output('table', 'children')],
  [Input('state_list', 'value')]
)  

def update_chart(selected_state):
  filtered_df = df_per_states[df_per_states['state'] == selected_state]
  table_data = filtered_df.drop(columns=['state', 'total'])
  # print(filtered_df.head(10))
  return [
    dcc.Graph(
      id="dccGraph",
      figure={
        'data': [
          go.Scatter(
            x = filtered_df['date'],
            y = filtered_df['positive'],
            mode = 'lines+markers',
            name = 'Positive'
          ),
          go.Scatter(
            x = filtered_df['date'],
            y = filtered_df['negative'],
            mode = 'lines+markers',
            name = 'Negative'
          ),
          go.Scatter(
            x = filtered_df['date'],
            y = filtered_df['pending'],
            mode = 'lines+markers',
            name = 'Pending'
          )
        ],
        'layout' : go.Layout(
          title = 'Covid 19',
          xaxis = { 'title': 'Date' },
          hovermode='closest'
        )
      }
    ),
    dt.DataTable(
      id='dash_table',
      columns=[{'name': i, 'id': i} for i in table_data.columns],
      data=table_data.to_dict('rows')
    )
  ]

if __name__ == '__main__':
    app.run_server(debug=True)
