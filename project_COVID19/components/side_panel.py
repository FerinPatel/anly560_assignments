import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

def tab_about():
  pass

def tab_userSelection(data):
  return dbc.Card(
    dbc.CardBody(
        [
          html.Label('State :'),
          state_dropdown(data)
        ]
    ),
    className="mt-3",
  )

def state_dropdown(data):
  return dcc.Dropdown(
      id='state_list',
      options = [
        { 'label': dt['state'], 'value': dt['state'] }
        for dt in data
      ],
      placeholder = 'Select a state'
    )