# app.py -> for NASA Spacewalks Dash App deployed to <https://spacewalksrussiausevasdash.herokuapp.com/>
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
    # marginal_y='histogram',
    title='U.S. & Russian EVAs, according to NASA (1965-2013)',
    color_discrete_map={"Russia": "red", "USA": "blue"}
)

# create the annotation for the subtitle: subtitle_annotation
subtitle_annotation = {
    'x': '1970-01-01',
    'y': 560,
    'showarrow': False,
    'align': 'center',
    'font': {'color': 'white', 'size': 15},
    'text': "Extravehicular activity (EVA) related to space flight.<br>"
            "Hover over the data points to learn more about the "
            "crews and spaceshuttles for each EVA.<br>Use the slider "
            "below the x-axis to select custom date ranges. <br>Double-click on "
            "one of the colors on the legend to isolate a country on the plot.<br>"
}

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
    yaxis=dict(
        zeroline=False,
        showgrid=False
    ),
    xaxis=dict(
        title='Date',
        zeroline=False,
        showgrid=False,
        autorange=True,
        range=[spacewalksDF['Date'].min(), spacewalksDF['Date'].max()],
        rangeslider=dict(
            autorange=True,
            range=[spacewalksDF['Date'].min(), spacewalksDF['Date'].max()]
        ),
        type="date"
    ),
    paper_bgcolor='#222222',  # background color to match Darkly theme
    plot_bgcolor='#222222',  # plot color to match Darkly theme
    height=700,
    font=dict(size=20),
    annotations=[
        subtitle_annotation,
        first_annotation,
        moon_annotation,
        long_annotation],  # add annotations to the figure
    template='plotly_dark'
)

# instantiate Dash app with Darkly theme: app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# set Heroku server integration: server
server = app.server

# create app layout with plotly express scatter plot
app.layout = html.Div(children=[
    dcc.Graph(figure=fig),
    html.A(
        "Git Repo",
        href='https://github.com/scarnyc/space-walking-russian-and-us-evas',
        target="_blank",
        style={
            'font-family': 'sans-serif',
            'font-size': '24px',
            'color': '#2c70e6',
            'x': '688.5',
            'y': '666',
            'text-anchor': 'middle',
            'opacity': '1',
            'font-weight': 'normal',
            'white-space': 'pre',
            'pointer-events': 'all'}
    )
])

if __name__ == '__main__':
    app.run_server(
        debug=True,
        use_reloader=False
    )
