# app.py -> for NASA Spacewalks Dash App deployed to <https://us-russian-evas-dash.herokuapp.com/>
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html

# import NASA spacewalks .csv: spacewalks_df
spacewalksDF = pd.read_csv(
    'https://gist.githubusercontent.com/scarnyc/5751e46d68a3dcecbe3469982a508763/raw'
    '/c2ed7fbc522dba327192a655c2e027b62ff39ff4/spacewalks_eva.csv')

# create plotly.express scatter: fig
fig = px.scatter(
    spacewalksDF,
    x="Date",
    y="Duration (in Minutes)",
    size="Duration (in Minutes)",
    color="Country",
    hover_name="Vehicle",
    hover_data=["Crew", "Purpose"],
    size_max=20,
    template='plotly_dark',
    opacity=.9,
    render_mode='svg',
    marginal_y='histogram',
    title="Extravehicular Activity (EVA) refers a spacewalk done outside a spacecraft beyond Earth's appreciable " 
          "atmosphere.<br>Hover over the points for more info about each EVA. Use the slider to select custom date "
          "ranges. <br>Double-click the colors on the legend to isolate points for a country on the plot.<br><br>",
    color_discrete_map={"Russia": "red", "USA": "blue"}
)

# create the annotation for the world's first EVA: first_annotation
first_annotation = {'x': '1965-03-15', 'y': 20, 'showarrow': True,
                    'arrowhead': 4, 'font': {'color': 'white'},
                    'text': "World's 1st EVA"}

# create the annotation for the first solid ground EVA: moon_annotation
moon_annotation = {'x': '1969-07-15', 'y': 170, 'showarrow': True,
                   'arrowhead': 4, 'font': {'color': 'white'},
                   'text': "World's 1st Moonwalk"}

# create the annotation for the longest recorded EVA: long_annotation
long_annotation = {'x': '2001-03-15', 'y': 560, 'showarrow': True,
                   'arrowhead': 4, 'font': {'color': 'white'},
                   'text': 'Longest EVA on Record'}

# customize layout
fig.update_layout(
    title={'font': {'size': 18}},
    yaxis={'zeroline': False, 'showgrid': False},
    xaxis={
        'title': 'Date',
        'zeroline': False,
        'showgrid': False,
        'autorange': True,
        'range': [spacewalksDF['Date'].min(), spacewalksDF['Date'].max()],
        'rangeslider': {
            'autorange': True,
            'range': [spacewalksDF['Date'].min(), spacewalksDF['Date'].max()]},
        'type': "date"
    },
    paper_bgcolor='#222222',  # background color to match Darkly theme
    plot_bgcolor='#222222',  # plot color to match Darkly theme
    height=550,
    font={'size': 20},
    annotations=[
        first_annotation,
        moon_annotation,
        long_annotation]  # add annotations to the figure
)

# instantiate Dash app with Darkly theme: app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# set Heroku server integration: server
server = app.server

# create app layout with plotly express scatter plot
app.layout = html.Div(children=[
    html.H1('<br>',
            style={'color': '#222222'}),
    html.Center(children=[
        html.H2('U.S. & Russian EVAs (1965-2013)',
                style={'font-size': '50px'})
    ]),
    dcc.Graph(figure=fig),
    dbc.Button(
        "Git Repo",
        id="link-centered",
        className="ml-auto",
        href='https://github.com/scarnyc/NASA_Spacewalks_Dash'
    )
])

if __name__ == '__main__':
    app.run_server(
        debug=True,
        use_reloader=False
    )
