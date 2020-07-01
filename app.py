import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

# import NASA spacewalks .csv: spacewalks_df
spacewalks_df = pd.read_csv('https://gist.githubusercontent.com/scarnyc/5751e46d68a3dcecbe3469982a508763/raw/c2ed7fbc522dba327192a655c2e027b62ff39ff4/spacewalks_eva.csv')

# create plotly express scatter plot: fig
fig = px.scatter(
    spacewalks_df,
    x="Date",
    y="Duration (in Minutes)",
    size="Duration (in Minutes)",
    color="Country",
    hover_name="Vehicle",
    hover_data=["Crew", "Purpose"],
    size_max=12,
    template='plotly_dark',
    opacity=.9,
    render_mode='svg',
    marginal_y='histogram',
    title='U.S. & Russian Spacewalks (1965-2013)',
    color_discrete_map={"Russia": "red", "USA": "blue"}
)

# update custom layout
fig.update_layout(
    yaxis=dict(
        zeroline=False,
        showgrid=False
    ),
    xaxis=dict(
        zeroline=False,
        showgrid=False,
        autorange=True,
        range=[spacewalks_df['Date'].min(), spacewalks_df['Date'].max()],
        rangeslider=dict(
            autorange=True,
            range=[spacewalks_df['Date'].min(), spacewalks_df['Date'].max()]
        ),
        type="date"
    ),
    paper_bgcolor='#222222',  # background color to match Darkly theme
    plot_bgcolor='#222222'    # plot color to match Darkly theme
)

# instantiate Dash app with Darkly theme: app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# set server: server
server = app.server

# create app layout with plotly express scatter plot
app.layout = html.Div(children=[
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run_server()
