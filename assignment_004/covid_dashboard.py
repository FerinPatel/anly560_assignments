import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.graph_objs as go
from dash.dependencies import Input, Output

import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df_acc = pd.read_csv('data/us_covid19_daily.csv')
df_per_states = pd.read_csv('data/us_states_covid19_daily.csv')
df_states_abbr = pd.read_csv('data/state_abb.csv')

# casting types..
df_per_states['date'] = pd.to_datetime(df_per_states['date'],  format='%Y%m%d')
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
    dhtml.Div(id='chart')
])

@app.callback(
  Output('chart', 'children'),
  [Input('state_list', 'value')]
)  

def update_chart(selected_state):
  filtered_df = df_per_states[df_per_states['state'] == selected_state]
  print(filtered_df.head(10))
  return dcc.Graph(
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
    )

if __name__ == '__main__':
    app.run_server(debug=True)
