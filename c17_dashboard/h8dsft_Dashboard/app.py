import dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.FLATLY]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.title = "NGC 17"

server = app.server
app.config.suppress_callback_exceptions = True