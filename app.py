import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_table
import pandas as pd

df = px.data.tips()
days = df.day.unique()

app = dash.Dash(__name__)
server = app.server

df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
fig = px.scatter(df2, x="gdp per capita", y="life expectancy",
                 size="population", color="continent", hover_name="country",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Dropdown(
        id="dropdown",
        options=[{"label": x, "value": x} for x in days],
        value=days[0],
        clearable=False,
    ),
    dcc.Graph(id="bar-chart"),
    dcc.Graph(figure = fig)
])

@app.callback(
    Output("bar-chart", "figure"),
    [Input("dropdown", "value")])
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill",
                 color="smoker", barmode="group")
    return fig



if __name__ == "__main__":
    app.run_server(debug=True)
