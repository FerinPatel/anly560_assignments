from app import app
from dash.dependencies import Output, Input

from components.viewer import update_viewer

@app.callback(
  [
    Output('pos_t', 'children'),
    Output('death_t', 'children'),
    Output('tested_t', 'children'),
    Output('main_graph_div', 'children')
  ], 
  [Input('state_list', 'value')]
)
def selected_state(value):
  return update_viewer(value)