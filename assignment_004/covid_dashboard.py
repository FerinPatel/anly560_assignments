import dash
import dash_core_components as dcc
import dash_html_components as dhtml
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('data/covid_19_data.csv')
print(df)

app.layout = dhtml.Div(children=[
    dhtml.H1(children='Covid 19'),

    dhtml.Div(children='''
        Covid Dashboard....
    '''),
])

if __name__ == '__main__':
    app.run_server(debug=True)
