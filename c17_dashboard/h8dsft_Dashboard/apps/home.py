import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import numpy as np

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

from app import app

df = pd.read_csv('data_cleaned.csv')

layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(
                html.H1(
                    "FIFA 19",
                    className = "text-center",
                ),
                className = "mb-2 mt-5"
            ),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Label("Select Position:"),
                dbc.Select(
                    id="selected_position",
                    options=[
                        {"label": position_input, "value": position_input} for position_input in df.Position.unique()
                    ],
                    value='ST',
                )
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart1'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart2'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart3'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart4'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart5'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart6'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Spinner([
                    dcc.Graph(
                        id='chart7'
                    )
                ])
            ],
            className = "mb-4"),
        ]),
    ])
])

@app.callback(
    Output('chart1', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    viz1 = df[df['Position']==position_input].groupby(['Work Rate']).median()[['ID']].rename(columns={'ID':'median'}).reset_index()
    fig = px.bar(
        viz1, x = 'Work Rate', y = 'median', color ='Work Rate', title=str(position_input) + ' Position Work Rate median'
        )
    return fig

@app.callback(
    Output('chart2', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    fig = px.histogram(
        df[df['Position']==position_input], x="Wage", nbins=10, title=str(position_input) + ' Position Wage Distribution'
        )
    return fig

@app.callback(
    Output('chart3', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    fig = px.histogram(
        df[df['Position']==position_input], x="Wage", marginal="rug", nbins=50, title=str(position_input) + ' Position Wage Distribution'
        )
    return fig

@app.callback(
    Output('chart4', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    fig = px.pie(
        df[df['Position']==position_input], values ='Release Clause', names = 'Work Rate',
        title=str(position_input) + ' Position Release Clause by Work Rate'
        )
    return fig

@app.callback(
    Output('chart5', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    fig = px.sunburst(
        df[df['Position']==position_input], path = ['Preferred Foot', 'Work Rate'], values ='Wage',
        title=str(position_input) + ' Position Wage based on Preferred Foot & Work Rate'
        )
    return fig

@app.callback(
    Output('chart6', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    fig = px.violin(
        df[df['Position']==position_input], x="Stamina",
        title=str(position_input) + ' Position Stamina Distribution'
        )
    return fig

@app.callback(
    Output('chart7', 'figure'),
    Input('selected_position', 'value'))
def update_chart(position_input):
    fig = px.scatter_matrix(
        df[df['Position']==position_input], dimensions = ['Potential', 'Value', 'Wage'], color = 'Preferred Foot',
        title=str(position_input) + ' Position Pairplot of Potential, Value, and Wage'
        )
    return fig