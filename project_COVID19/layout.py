import dash_html_components as html

import dash_bootstrap_components as dbc

from components.us_state_map import us_map
from components.side_panel import tab_about, tab_userSelection

# -- App layout ----------------------------------

def app_layout(data, geo_states):

  return dbc.Container([
    
    dbc.Row([
      # for map...
      dbc.Col(us_map(data, geo_states))
    ]),

    dbc.Row([
      dbc.Col(
        # for side panel... ie Tabs
        dbc.Tabs([
          dbc.Tab(
            tab_about(),
            label='About'
          ),
          dbc.Tab(
            tab_userSelection(data),
            label='User Selection'
          )
        ])
      ),

      dbc.Col([
        # for various components of viewer...
        dbc.Row([
          # 1st row for numeric data...
          dbc.Col(
            html.Div(
              # Positive/State
              id='pos_t'
            )
          ),

          dbc.Col([
            dbc.Row(
              dbc.Col(
                html.Div(
                  # Deaths/State
                  id='death_t'
                )
              ), no_gutters=True
            ),

            dbc.Row(
              dbc.Col(
                html.Div( 
                  # TotalTested/State
                  id='tested_t'
                )
              ), no_gutters=True
            )
          ])
        ], align='center', no_gutters=True),

        dbc.Row([
          # 2nd row for chart...
          dbc.Col(html.Div(id='main_graph_div'))
        ]),

        dbc.Row([
          # 3rd row for chart...
          dbc.Col()
        ])
      ])
    ])
  ])

import callbacks