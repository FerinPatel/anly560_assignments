import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

import pandas as pd

from main import retreive_data

data = pd.DataFrame(retreive_data())

def pos_total(value):
  print(value)
  print(data.head())

def tested_total():
  pass

def death_total():
  pass

def state_graph():
  pass

def state_change_graph():
  pass
  