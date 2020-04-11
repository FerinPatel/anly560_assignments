from app import app
from dash.dependencies import Output, Input

from components.viewer import pos_total

@app.callback(
  Output('pos_t', 'children'), 
  [Input('state_list', 'value')]
)
def selected_state(value):
  return pos_total(value)