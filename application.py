import os
import path
import pandas as pd
import numpy as np

import dash
# from jupyter_dash import JupyterDash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime

# ##### Download data #####

# from urllib.request import urlopen, Request
# from io import StringIO
# import contextlib

# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
# url = 'https://aemo.com.au/aemo/data/nem/priceanddemand/'
# root_filename = 'PRICE_AND_DEMAND_'
# years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]
# months = ['01','02','03','04','05','06','07','08','09','10','11','12']
# states = ['NSW', 'QLD', 'VIC', 'SA', 'TAS']

# for state in states[:]:
#     files_dir = os.path.join('data',state.lower())

#     completed = 0

#     for year in years[:]:

#         for month in months[:]:
#             file = root_filename + str(year) + month + '_' + state + '1.csv'
#             file_url = url + file
#             destination = os.path.join(files_dir, file)

#             req = Request(url=file_url, headers=headers)

#             try:
#                 html = urlopen(req).read()
#                 data = StringIO(str(html, 'utf-8'))

#                 (
#                     pd.read_csv(StringIO(str(urlopen(req)
#                         .read(), 'utf-8')))
#                         .to_csv(destination)
#                 )

#                 print(file, 'downloaded')

#             except:
#                 print(file, 'NOT available')

#             finally:
#                 if str(year)+month == '202009':
#                     completed = 1
#                     break

#         if completed:
#             break

# print('>>>>> Download completed <<<<<')

# ##### Create warehouse ##### #
#
# def pop_non_csv(_files_list):
#     for i, f in enumerate(_files_list):
#         if _files_list[i][-3:] != 'csv':
#             _files_list.pop(i)
#     return _files_list
#
# def join_files_and_save(state, destination_folder):
#     _files_list = os.listdir(os.path.join('data', state))
#     _files_list.sort()
#
#     _files_list = pop_non_csv(_files_list)
#
#     _df = pd.read_csv( os.path.join('data', state, _files_list[0]), index_col=0 )
#     _df = _df.reset_index(drop=True)
#
#     ##### chage slicer for full datasets #####
#     for f in _files_list[:]:
#         _df = pd.concat([_df, pd.read_csv(os.path.join('data', state, f), index_col=0)])
#
#     _df = _df.reset_index(drop=True)
#     _df['REGION'] = _df['REGION'].str.slice(0,-1,1)
#     _df.to_csv(os.path.join(destination_folder, 'states', state + '.csv'))
#
# states = ['NSW', 'QLD', 'SA', 'TAS', 'VIC']
#
# destination_folder = os.path.join('data', 'warehouse')
#
# for state in states[:]:
#     join_files_and_save(state, destination_folder)
#
#
# ##### Create National dataset ##### #
#
# files_list = os.listdir('data/warehouse/states')
# files_list = pop_non_csv(files_list)
# files_list.sort()
#
# df_nem = pd.read_csv(os.path.join('data/warehouse/states', files_list[0]), index_col=0)
#
# for f in files_list[1:]:
#     df_nem = pd.concat([df_nem, pd.read_csv(os.path.join('data/warehouse/states', f), index_col=0)])
#
# df_nem = df_nem.reset_index(drop=True)
#
# df_nem.to_csv(os.path.join('data/warehouse', 'df_nem.csv'))

# ##### ETL NEM dataset ##### #
#
# df_nem = pd.read_csv('data/warehouse/df_nem.csv', index_col=0)
#
# df_nem_tf = df_nem[:]
# df_nem_tf['SETTLEMENTDATE'] = pd.to_datetime(df_nem_tf['SETTLEMENTDATE'])
# df_nem_tf['date'] = df_nem_tf['SETTLEMENTDATE'].dt.date
# df_nem_tf['year'] = df_nem_tf['SETTLEMENTDATE'].dt.year
# df_nem_tf['month'] = df_nem_tf['SETTLEMENTDATE'].dt.month
# df_nem_tf['date_number'] = df_nem_tf['SETTLEMENTDATE'].dt.day
# df_nem_tf['day'] = df_nem_tf['SETTLEMENTDATE'].dt.day_name().str.slice(0,3,1)
# df_nem_tf['is_weekday'] = df_nem_tf['SETTLEMENTDATE'].dt.weekday.apply(lambda x: True if x <= 4 else False)
# df_nem_tf['time'] = df_nem_tf['SETTLEMENTDATE'].dt.time.apply(lambda t: t.strftime('%H:%M'))
# df_nem_tf['week'] = df_nem_tf['SETTLEMENTDATE'].dt.isocalendar().week
#
# def clean_week(s):
#     if(s[0]==1) & (s[1]==53):
#         return 1
#     elif(s[0]==12) & (s[1]==53):
#         return 52
#     else:
#         return s[1]
#
# df_nem_tf['week'] = df_nem_tf[['month', 'week']].apply(clean_week, axis=1)
# df_nem_tf.drop(columns=['PERIODTYPE'], inplace=True)
#
# # Save dataframes to warehouse
# df_nem_tf.to_csv(os.path.join('data/warehouse', 'df_nem_tf.csv'))

# # Need to split files for Github upload
# df_nem_tf_2020 = df_nem_tf[df_nem_tf['year'] == 2020]
# df_nem_tf_2019 = df_nem_tf[df_nem_tf['year'] == 2019]
# df_nem_tf_2018 = df_nem_tf[df_nem_tf['year'] == 2018]
# df_nem_tf_2017 = df_nem_tf[df_nem_tf['year'] == 2017]
# df_nem_tf_2016 = df_nem_tf[df_nem_tf['year'] == 2016]
# df_nem_tf_2015 = df_nem_tf[df_nem_tf['year'] == 2015]
# df_nem_tf_2014 = df_nem_tf[df_nem_tf['year'] == 2014]
# df_nem_tf_2013 = df_nem_tf[df_nem_tf['year'] == 2013]
# df_nem_tf_2012 = df_nem_tf[df_nem_tf['year'] == 2012]
# df_nem_tf_2011 = df_nem_tf[df_nem_tf['year'] == 2011]
# df_nem_tf_2010 = df_nem_tf[df_nem_tf['year'] == 2010]
#
# df_nem_tf_2020.to_csv('data/df_nem_tf/df_nem_tf_2020.csv')
# df_nem_tf_2019.to_csv('data/df_nem_tf/df_nem_tf_2019.csv')
# df_nem_tf_2018.to_csv('data/df_nem_tf/df_nem_tf_2018.csv')
# df_nem_tf_2017.to_csv('data/df_nem_tf/df_nem_tf_2017.csv')
# df_nem_tf_2016.to_csv('data/df_nem_tf/df_nem_tf_2016.csv')
# df_nem_tf_2015.to_csv('data/df_nem_tf/df_nem_tf_2015.csv')
# df_nem_tf_2014.to_csv('data/df_nem_tf/df_nem_tf_2014.csv')
# df_nem_tf_2013.to_csv('data/df_nem_tf/df_nem_tf_2013.csv')
# df_nem_tf_2012.to_csv('data/df_nem_tf/df_nem_tf_2012.csv')
# df_nem_tf_2011.to_csv('data/df_nem_tf/df_nem_tf_2011.csv')
# df_nem_tf_2010.to_csv('data/df_nem_tf/df_nem_tf_2010.csv')

# Load data sets from warehouse


def clean_week(s):
    if (s[0] == 1) & (s[1] == 53):
        return 1
    elif (s[0] == 12) & (s[1] == 53):
        return 52
    else:
        return s[1]


files_list = os.listdir('data/df_nem_tf')
files_list.sort()

df_nem_tf = pd.read_csv('data/df_nem_tf/' + files_list[0], index_col=0)
for f in files_list[1:]:
    df_nem_tf = pd.concat(
        [df_nem_tf, pd.read_csv('data/df_nem_tf/' + f, index_col=0)],
        ignore_index=True)

df_nem_tf.drop(
    df_nem_tf[
        ((df_nem_tf['month'] == 10) & (df_nem_tf['year'] == 2020))
    ].index,
    inplace=True
)
df_nem_tf['date'] = pd.to_datetime(df_nem_tf['date'])

df_cases = pd.read_csv('data/cases_daily_state.csv', index_col=0)
df_cases['year'] = 2020
df_cases['month'] = df_cases.index.str.slice(3, 5, 1)
df_cases['day'] = df_cases.index.str.slice(0, 2, 1)
df_cases['date'] = pd.to_datetime(df_cases[['year', 'month', 'day']])
df_cases.reset_index(inplace=True)
df_cases.drop(columns=['Date', 'year', 'month', 'day'], inplace=True)
df_cases['year'] = df_cases['date'].dt.year
df_cases['month'] = df_cases['date'].dt.month
df_cases['week'] = df_cases['date'].dt.isocalendar().week
df_cases['date_number'] = df_cases['date'].dt.day
df_cases['week'] = df_cases[['month', 'week']].apply(clean_week, axis=1)

df_pv = pd.read_csv('data/states-output-monthly.csv', index_col=0).reset_index()
df_pv['year'] = df_pv['Date'].str.slice(0, 4, 1).astype(int)
df_pv['month'] = df_pv['Date'].str.slice(5, 7, 1).astype(int)
df_pv.rename(
    columns={
        'Output NSW': 'NSW',
        'Output VIC': 'VIC',
        'Output QLD': 'QLD',
        'Output SA': 'SA',
        'Output WA': 'WA',
        'Output TAS': 'TAS',
        'Output NT': 'NT'
    }, inplace=True
)


# ### Dashboard settings ### #
state_color = {
    'VIC': 'royalblue',
    'NSW': 'lightskyblue',
    'QLD': 'maroon',
    'TAS': 'green',
    'SA': 'red'
}

color_palette = px.colors.qualitative.G10

years = np.sort(df_nem_tf['year'].unique())
states = np.sort(df_nem_tf['REGION'].unique())

year_min = 2010
year_max = years.max()

slider_style = {'transform': 'rotate(0deg)'}
year_marks = {str(y): {'label': str(y), 'style': slider_style} for y in years}
years_dropdown_options = [{'label': str(y), 'value': y} for y in years[::-1]]

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
months_dropdown_options = [{'label': m, 'value': i+1} for i, m in enumerate(months)]

months_val = [i for i in range(1, 13)]
month_min = 1
month_max = 12
month_marks = {mv: m for m, mv in zip(months, months_val)}

slider_style = {'transform': 'rotate(45deg)'}
weeks = [1, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48]
week_marks = {str(w): {'label': 'Week ' + str(w), 'style': slider_style} for w in weeks}
weeks_dropdown_options = [{'label': 'Week ' + str(i), 'value': i} for i in range(1, 53)]

calendar = [
    ['Jan', 31], ['Feb', 28], ['Mar', 31], ['Apr', 30], ['May', 31], ['Jun', 30],
    ['Jul', 31], ['Aug', 31], ['Sep', 30], ['Oct', 31], ['Nov', 30], ['Dec', 31]
]

x_ticktext = []
for m in calendar[:]:
    for d in range(int(m[1])):
        x_ticktext.append('{}-{}'.format(str(d + 1), m[0]))

line = ['solid', 'dot', 'dash', 'longdash', 'dashdot', 'longdashdot']
opacity = [0.8, 0.6, 0.4, 0.4, 0.2]
width = [4, 2, 2, 2, 2]

rolling = {'Weekly': 1, 'MA-2': 2, 'MA-4': 4,
           'Monthly': 1, 'MA-3': 3,
           'Daily': 1, 'MA-7': 7, 'MA-14': 14, 'MA-28': 28}

state_and_comparison_graph_height = 500
hourly_graph_height = 500
average_demand_graph_height = 500

# ### Dashboard ### #
external_stylesheets = [dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
application = app.server
app.layout = html.Div(children=[

    html.Div(  # Navbar
        children=[
            dbc.Navbar(
                children=[
                    dbc.Col(
                        html.Center(
                            html.H1(
                                children='NEM Demand Dashboard',
                                style={'textAlign': 'center'}
                            ),
                            className='ml-5 mt-3 mb-1',
                        ),
                        width={'size': 12, 'offset': 0},
                    ),
                ],
            ),

            dbc.Navbar(
                children=[
                    dbc.Col(
                        html.Label(
                            [
                                'Select state to compare',
                                dcc.Dropdown(
                                    id='state-dropdown',
                                    options=[{'label': s, 'value': s} for s in states],
                                    multi=True,
                                    placeholder='Select state to compare',
                                    value=states
                                ),
                            ],
                            style=dict(
                                width='100%',
                                verticalAlign="middle"
                            ),
                            className='ml-3'
                        ),
                        width={'size': 10, 'offset': 0},
                        className='container'
                    ),
                    dbc.Col(
                        html.Label(
                            [
                                'Previous years:',
                                dcc.Dropdown(
                                    id='yrs-dropdown',
                                    options=[{'label': str(i), 'value': i} for i in range(1, 4)],
                                    value=3,
                                ),
                            ],
                            style=dict(
                                width='100%',
                                verticalAlign="middle",
                            ),
                            className='ml-3'
                        ),
                        width={'size': 2, 'offset': 0},
                        className='container'
                    ),
                ],
            ),

            # 'year-dropdown', 'data-dropdown', 'start-period-dropdown'
            # 'end-period-dropdown', 'date-picker-range'
            dbc.Navbar(
                children=[

                    dbc.Col(
                        html.Label(
                            [
                                'Year selected',
                                dcc.Dropdown(
                                    id='year-dropdown',
                                    options=years_dropdown_options,
                                    value=2020,
                                    clearable=False,
                                )
                            ],
                            style=dict(
                                width='100%',
                                verticalAlign="middle"
                            ),
                            className='ml-3'
                        ),
                        width={'size': 2, 'offset': 0},
                        className='container'
                    ),

                    dbc.Col(
                        html.Label(
                            [
                                'Aggregated:',
                                dcc.Dropdown(
                                    id='data-dropdown',
                                    options=[
                                        {'label': 'Monthly', 'value': 'Monthly'},
                                        {'label': 'Weekly', 'value': 'Weekly'},
                                        {'label': 'Daily', 'value': 'Daily'},
                                    ],
                                    value='Monthly',
                                    clearable=False,
                                ),
                            ],
                            style=dict(
                                width='100%',
                                verticalAlign="middle"
                            ),
                            className='ml-3'
                        ),
                        width={'size': 2, 'offset': 0},
                        className='container'
                    ),

                    dbc.Col(
                        html.Label(  # Start Period'
                            [
                                'Start Period',
                                dcc.Dropdown(
                                    id='start-period-dropdown',
                                    options=years_dropdown_options,
                                    value=1,
                                    clearable=False
                                )
                            ],
                            style=dict(
                                width='100%',
                                verticalAlign="middle"
                            ),
                            className='ml-3'
                        ),
                        width={'size': 2, 'offset': 0},
                        className='container'
                    ),

                    dbc.Col(
                        html.Label(  # 'End Period'
                            [
                                'End Period',
                                dcc.Dropdown(
                                    id='end-period-dropdown',
                                    options=years_dropdown_options,
                                    value=1,
                                    clearable=False
                                )
                            ],
                            style=dict(
                                width='100%',
                                verticalAlign="middle"
                            ),
                            className='ml-3'
                        ),
                        width={'size': 2, 'offset': 0},
                        className='container'
                    ),

                    dbc.Col(
                        dcc.DatePickerRange(
                            id='date-picker-range',
                            minimum_nights=0,
                            display_format='D/M/Y',
                            disabled=False
                        ),
                        width={'size': 4, 'offset': 0},
                        className='container ml-5'
                    )

                ],
            ),

        ],
        className='fixed-top block'
    ),
    html.Div(  # Spacer
        children=[
            html.Center(
                html.H1(
                    id='hidden-div',
                    children=[0, "This is a spacer"],
                    style={'fontSize': 150, 'color': 'white'},
                    className='my-5'
                ),
            ),
        ],
        # hidden=True
    ),
    html.Div(
        dbc.Row(  # State graph and Compare graph
            children=[
                dbc.Col(
                    dcc.Graph(
                        id='demand-state-graph',
                        style={"height": state_and_comparison_graph_height},
                    ),
                    width={'size': 12, 'offset': 0},
                    lg=12, xl=6
                ),
                dbc.Col(
                    dcc.Graph(
                        id='demand-compare-graph',
                        style={"height": state_and_comparison_graph_height},
                    ),
                    width={'size': 12, 'offset': 0},
                    lg=12, xl=6
                )
            ],
            className='mb-5',
        ),
        # hidden=True
    ),
    dbc.Row(
        children=[
            dbc.Col(  # Hour graph, PV graph
                children=[
                    dbc.Row(
                        html.Center(
                            children=[
                                html.Span(
                                    children=['Average Demand by Hour (MW) in'],
                                    style={'fontSize': 30},
                                ),
                                html.Span(
                                    id='hr-graph-title',
                                    children=[''],
                                    style={'fontSize': 30, 'font-weight': 'bold'},
                                ),
                            ],
                            className='container ml-5 mb-0 mt-0',
                        ),
                    ),
                    dbc.Row(
                        dbc.Col(
                            dcc.Graph(
                                id='demand-hourly-graph',
                                style={"height": hourly_graph_height},
                            ),
                            # width={'size': 12, 'offset': 0},
                            className='container mb-5',
                            lg=12, xl=11
                        ),
                    ),
                    dbc.Row(
                        html.Center(
                            children=[
                                html.Span(
                                    children=['Total Solar PV Monthly Output (MWh) in'],
                                    style={'fontSize': 30},
                                ),
                                html.Span(
                                    id='pv-graph-title',
                                    children=[''],
                                    style={'fontSize': 30, 'font-weight': 'bold'},
                                ),
                            ],
                            className='container ml-5 mb-0 mt-0',
                        ),
                    ),
                    dbc.Row(  # PV graph
                        dbc.Col(
                            dcc.Graph(
                                id='pv-graph',
                                style={"height": hourly_graph_height},
                            ),
                            # width={'size': 6, 'offset': 0},
                            className='container mb-5',
                            lg=12, xl=11
                        ),
                        className='mb-5'
                    ),
                ],
                className='container mt-0',
                lg=12, xl=7
            ),
            dbc.Col(  # Write up
                children=[
                    dbc.Row(
                        dbc.Col(
                            dbc.Card(
                                dbc.CardBody(
                                    [
                                        html.H4(
                                            "Does Covid-19 have a direct impact on Electricity consumption?",
                                            className="card-title"),
                                        # html.H6("Card subtitle", className="card-subtitle"),
                                        html.P(
                                            children=[
                                                "First, let us have a look at electricity demand of NEM network in ",
                                                dbc.Badge("2019", id='y2019-badge', color="secondary", className="mr-1"),
                                                "and 3 previous years. ",
                                                "We could see that the demand is gradually decreasing during work hours ",
                                                "but slightly increasing in the evening year by year. ",
                                                "There could be various factors ie, the use of more energy efficient ",
                                                "appliances, or more adoption to solar cell both in residential and ",
                                                "commercial buildings. The latter is confirmed by the graph below which shows ",
                                                "total monthly output in Solar PV generators which increases year by year. ",
                                            ],
                                            className="card-text",
                                            style={'text-align': 'justify'}
                                        ),
                                        html.P(
                                            children=[
                                                "So where does Covid-19 come into the equation?"
                                            ],
                                            className="card-text",
                                            style={'font-weight': 'bold'}
                                        ),
                                        html.P(
                                            children=[
                                                "If we look at ",
                                                dbc.Badge(
                                                    "pre-Covid",
                                                    id='pre-covid-badge',
                                                    color="success",
                                                    className="mr-1"
                                                ),
                                                "period which is the first 2 months of the year 2020, ",
                                                "the average demand overall is already below previous years. ",
                                                "And if we have a look during ",
                                                dbc.Badge("Covid", id='covid1-badge', color="danger", className="mr-1"),
                                                "period, which if from week 11 to week 39 which is at the end of ",
                                                "September 2020, (the most recent period in this dataset) we could ",
                                                "also see a decrease in demand in comparison to previous years. "
                                            ],
                                            className="card-text",
                                            style={'text-align': 'justify'}
                                        ),
                                        html.P(
                                            children=[
                                                "There is a slight decrease in demand in the morning during ",
                                                dbc.Badge("Covid", id='covid2-badge', color="danger", className="mr-1"),
                                                "period which could be due to business closure and employees working from home. "
                                            ],
                                            className="card-text",
                                            style={'text-align': 'justify'}
                                        ),
                                        html.P(
                                            children=[
                                                "What is interesting however, is in ",
                                                dbc.Badge("week 16", id='w16-badge', color="secondary", className="mr-1"),
                                                "which is the week after Easter that we could ",
                                                "see a hugh drop in demand during weekdays and pushing towards weekend demand.",
                                                "I have absolutely no idea what caused this phenomenal given that the number of ",
                                                "new cases is lower than previous weeks."
                                            ],
                                            className="card-text",
                                            style={'text-align': 'justify'}
                                        ),
                                        html.P(
                                            children=[
                                                "Conclusion"
                                            ],
                                            className="card-text",
                                            style={'font-weight': 'bold'}
                                        ),
                                        html.P(
                                            children=[
                                                "Covid 19 pandemic certainly impacts human being all over the world. People have ",
                                                'to adjust for the "new normal" way of life which includes social distancing, ',
                                                "being more hygienic, adoption of working from home for businesses, etc. ",
                                                "However, energy consumption is vital to modern society and still remains very ",
                                                "little affected by this pandemic."
                                            ],
                                            className="card-text",
                                            style={'text-align': 'justify'}
                                        ),
                                        dbc.Tooltip(
                                            "click to display 2019 and previous years",
                                            target="y2019-badge"
                                        ),
                                        dbc.Tooltip(
                                            "click to display pre-covid period",
                                            target="pre-covid-badge"
                                        ),
                                        dbc.Tooltip(
                                            "click to display covid period",
                                            target="covid1-badge"
                                        ),
                                        dbc.Tooltip(
                                            "click to display covid period",
                                            target="covid2-badge"
                                        ),
                                        dbc.Tooltip(
                                            "click to display week 16 graphs",
                                            target="w16-badge"
                                        ),
                                    ]
                                ),
                                outline=False
                            ),
                            lg=11, xl=11
                        ),
                    ),
                ],
                className='container mx-5 align-self-center',
                lg=12, xl=4
            )
        ],
        className='mb-5'
    ),
    dbc.Row(  # Average graph title and dropdown
        children=[
            dbc.Col(
                html.Label(
                    [
                        dcc.Dropdown(
                            id='avg-data-dropdown',
                            clearable=False
                        ),
                    ],
                    style=dict(
                        width='60%',
                        verticalAlign="middle",
                    ),
                ),
                className='container mt-0',
                width={'size': 2, 'offset': 1},
            ),
            dbc.Col(
                children=[
                    html.Span(
                        children=['Average Demand (MW) in'],
                        style={'fontSize': 30},
                    ),
                    html.Span(
                        id='avg-graph-title',
                        children=[''],
                        style={'fontSize': 30, 'font-weight': 'bold'},
                    ),
                ],
                className='container mt-0',
                width={'size': 9, 'offset': 0},
            ),
        ],
        justify='around',
        className='mt-5'
    ),

    dbc.Row(  # Average graph
        children=[
            dbc.Col(
                dcc.Graph(
                    id='avg-graph',
                    style={"height": average_demand_graph_height},
                ),
                width={'size': 11, 'offset': 0},
                className='ml-5'
            ),
        ],
        className='mt-0'
    ),

])


@app.callback(
    Output('state-dropdown', 'value'),
    Output('yrs-dropdown', 'value'),
    Output('year-dropdown', 'value'),
    Output('data-dropdown', 'value'),
    [
        Input('y2019-badge', 'n_clicks'),
        Input('pre-covid-badge', 'n_clicks'),
        Input('covid1-badge', 'n_clicks'),
        Input('covid2-badge', 'n_clicks'),
        Input('w16-badge', 'n_clicks'),
    ],
    [
        State('state-dropdown', 'value'),
        State('yrs-dropdown', 'value'),
        State('year-dropdown', 'value'),
        State('data-dropdown', 'value')
    ]
)
def update_state_yrs_year_data_dropdown(
        y2019, pre_covid, covid1, covid2, w16,
        current_state, current_yrs, current_year, current_data
):
    trigger = dash.callback_context.triggered[0]['prop_id']
    if trigger == 'y2019-badge.n_clicks':
        selected_state = states
        selected_yrs = 3
        selected_year = 2019
        selected_data = 'Monthly'
    elif trigger == 'pre-covid-badge.n_clicks':
        selected_state = states
        selected_yrs = 3
        selected_year = 2020
        selected_data = 'Monthly'
    elif (
            (trigger == 'covid1-badge.n_clicks') |
            (trigger == 'covid2-badge.n_clicks') |
            (trigger == 'w16.n_clicks')
    ):
        selected_state = states
        selected_yrs = 3
        selected_year = 2020
        selected_data = 'Weekly'
    else:
        selected_state = current_state
        selected_yrs = current_yrs
        selected_year = current_year
        selected_data = current_data
    print(trigger)
    return selected_state, selected_yrs, selected_year, selected_data


@app.callback(
    Output('start-period-dropdown', 'options'),
    Output('start-period-dropdown', 'value'),
    Output('start-period-dropdown', 'disabled'),
    [
        Input('data-dropdown', 'value'),
        Input('y2019-badge', 'n_clicks'),
        Input('pre-covid-badge', 'n_clicks'),
        Input('covid1-badge', 'n_clicks'),
        Input('covid2-badge', 'n_clicks'),
        Input('w16-badge', 'n_clicks'),
    ]
)
def update_start_period_dropdown(
        selected_data,
        y2019, pre_covid, covid1, covid2, w16
):
    trigger = dash.callback_context.triggered[0]['prop_id']

    if selected_data == 'Monthly':
        options = months_dropdown_options
        value = 1
        disabled = False
    elif selected_data == 'Weekly':
        options = weeks_dropdown_options
        if (trigger == 'covid1-badge.n_clicks') | (trigger == 'covid2-badge.n_clicks'):
            value = 11
        elif trigger == 'w16-badge.n_clicks':
            value = 16
        else:
            value = 1
        disabled = False
    else:
        options = months_dropdown_options
        value = ''
        disabled = True
    return options, value, disabled


@app.callback(
    Output('end-period-dropdown', 'options'),
    Output('end-period-dropdown', 'value'),
    Output('end-period-dropdown', 'disabled'),
    Output('hidden-div', 'children'),
    [
        Input('data-dropdown', 'value'),
        Input('start-period-dropdown', 'value'),
        Input('y2019-badge', 'n_clicks'),
        Input('pre-covid-badge', 'n_clicks'),
        Input('covid1-badge', 'n_clicks'),
        Input('covid2-badge', 'n_clicks'),
        Input('w16-badge', 'n_clicks'),
    ],
    [State('end-period-dropdown', 'value'),
     State('hidden-div', 'children'),
     State('data-dropdown', 'value')]
)
def update_end_period_dropdown(
        selected_data, start_value,
        y2019, pre_covid, covid1, covid2, w16,
        current_value, hidden_div, current_selected_data
):
    trigger = dash.callback_context.triggered[0]['prop_id']
    if selected_data == 'Monthly':
        options = months_dropdown_options[start_value-1:]
        hidden_div[0] = 0 if hidden_div[1] != 'Monthly' else hidden_div[0]
        current_value = 12 if hidden_div[0] == 0 else current_value
        if trigger == 'y2019-badge.n_clicks':
            value = 12
        elif trigger == 'pre-covid-badge.n_clicks':
            value = 2
        else:
            value = current_value if start_value <= current_value else start_value
        disabled = False
    elif selected_data == 'Weekly':
        options = weeks_dropdown_options[start_value-1:]
        hidden_div[0] = 0 if hidden_div[1] != 'Weekly' else hidden_div[0]
        current_value = 52 if hidden_div[0] == 0 else current_value
        if (trigger == 'covid1-badge.n_clicks') | (trigger == 'covid2-badge.n_clicks'):
            value = 39
        elif trigger == 'w16-badge.n_clicks':
            value = 16
        else:
            value = current_value if start_value <= current_value else start_value
        disabled = False
    else:
        options = months_dropdown_options
        value = ''
        disabled = True
    hidden_div[0] += 1
    hidden_div[1] = current_selected_data
    return options, value, disabled, hidden_div


@app.callback(
    Output('date-picker-range', 'min_date_allowed'),
    Output('date-picker-range', 'max_date_allowed'),
    Output('date-picker-range', 'disabled'),
    Output('date-picker-range', 'start_date'),
    Output('date-picker-range', 'end_date'),
    Output('date-picker-range', 'start_date_placeholder_text'),
    Output('date-picker-range', 'end_date_placeholder_text'),
    [Input('data-dropdown', 'value'),
     Input('year-dropdown', 'value')]
)
def update_date_picker(selected_data, selected_year):
    if selected_data == 'Daily':
        min_date_allowed = str(selected_year) + '-01-01'
        max_date_allowed = str(selected_year) + '-12-31'
        start_date = str(selected_year) + '-01-01'
        end_date = str(selected_year) + '-12-31'
        disabled = False
    else:
        min_date_allowed = ''
        max_date_allowed = ''
        disabled = True
        start_date = None
        end_date = None
    start_date_placeholder_text = ''
    end_date_placeholder_text = ''
    return (min_date_allowed, max_date_allowed, disabled, start_date, end_date,
            start_date_placeholder_text, end_date_placeholder_text)


@app.callback(
    Output('demand-state-graph', 'figure'),
    [
        Input('year-dropdown', 'value'),
        Input('data-dropdown', 'value'),
        Input('start-period-dropdown', 'value'),
        Input('end-period-dropdown', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
    ]
)
def update_state_graph(
        selected_year, selected_data, selected_start, selected_end,
        start_date, end_date
):
    fig_state = go.Figure()

    if selected_data == 'Monthly':
        df_state = (df_nem_tf[
                        (df_nem_tf['year'] == selected_year) &
                        (df_nem_tf['month'].between(selected_start, selected_end))
                        ].groupby('REGION').sum()
                    .reset_index()
                    )
    elif selected_data == 'Weekly':
        df_state = (df_nem_tf[
                        (df_nem_tf['year'] == selected_year) &
                        (df_nem_tf['week'].between(selected_start, selected_end))
                        ].groupby('REGION').sum()
                    .reset_index()
                    )
    else:
        df_state = (df_nem_tf[
                        (df_nem_tf['date'].between(
                            datetime.strptime(start_date, '%Y-%m-%d'),
                            datetime.strptime(end_date, '%Y-%m-%d')
                        ))
                        ].groupby('REGION').sum()
                    .reset_index()
                    )

    # Join latitude & longitude to states
    df_region_geo = pd.DataFrame({
        'REGION': ['NSW', 'QLD', 'SA', 'TAS', 'VIC'],
        'Lat': [-33.868, -27.468, -34.927, -42.879, -37.814],
        'Lon': [151.207, 153.028, 138.599, 147.329, 144.963]
    })
    df_state = pd.merge(df_state, df_region_geo, how='left', on=['REGION'])

    bubble_scale = 100 / df_state['TOTALDEMAND'].max()
    for s in df_state['REGION']:
        df_s = df_state[df_state['REGION'] == s]
        fig_state.add_trace(go.Scattergeo(
            lon=df_s['Lon'],
            lat=df_s['Lat'],
            text=f"{int(df_s['TOTALDEMAND']):,}",
            name=df_s['REGION'].values[0],
            marker=dict(
                size=df_s['TOTALDEMAND'] * bubble_scale,
                color=state_color[s],
                line_width=0,
                opacity=0.4
            ),
            hovertemplate=(
                    '<b>' + df_s['REGION'].values[0] + '</b><br><br>' +
                    '<b>Demand</b>:<br>' +
                    f"<b>{int(df_s['TOTALDEMAND']):,} MW</b><br>" +
                    '<extra></extra>'
            ),
        ))

        fig_state.add_trace(go.Scattergeo(
            lon=df_s['Lon'],
            lat=df_s['Lat'],
            text=f"{int(df_s['TOTALDEMAND']):,}",
            textfont={'size': 20, 'color': 'black'},
            mode='text',
            hoverinfo='skip',
            showlegend=False,
        ))

    fig_state.update_geos(
        fitbounds="locations",
        visible=True, resolution=50,
        showcoastlines=True, coastlinecolor="lightgrey",
    )

    fig_state.update_layout(
        title_text='<b>NEM</b> Total Demand by State (MW)',
        titlefont={'size': 25},
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=0.8
        )
    )

    return fig_state


@app.callback(
    Output('demand-compare-graph', 'figure'),
    [
        Input('year-dropdown', 'value'),
        Input('data-dropdown', 'value'),
        Input('start-period-dropdown', 'value'),
        Input('end-period-dropdown', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
        Input('state-dropdown', 'value'),
        Input('yrs-dropdown', 'value')
    ]
)
def update_compare_graph(
        selected_year, selected_data, selected_start, selected_end,
        start_date, end_date, selected_state, yrs
):
    fig_compare = make_subplots(specs=[[{"secondary_y": True}]])

    yrs = 0 if yrs is None else yrs

    if selected_data == 'Monthly':
        df_compare = (df_nem_tf[
                          (df_nem_tf['year'].between(selected_year - yrs, selected_year)) &
                          (df_nem_tf['month'].between(selected_start, selected_end))
                          ].groupby(['REGION', 'year', 'month']).sum()
                      .reset_index()
                      )
        df_nem_compare = df_compare.groupby(['year', 'month']).sum().reset_index()
    elif selected_data == 'Weekly':
        df_compare = (df_nem_tf[
                          (df_nem_tf['year'].between(selected_year - yrs, selected_year)) &
                          (df_nem_tf['week'].between(selected_start, selected_end))
                          ].groupby(['REGION', 'year', 'week']).sum()
                      .reset_index()
                      )
        df_nem_compare = df_compare.groupby(['year', 'week']).sum().reset_index()
    else:
        df_compare = (df_nem_tf[
                          (df_nem_tf['year'].between(selected_year - yrs, selected_year))
                          & ~((df_nem_tf['month'] == 2) & (df_nem_tf['date_number'] == 29))
                          ].groupby(['REGION', 'year', 'month', 'date_number', 'date']).sum()
                      .reset_index()
                      )
        df_nem_compare = df_compare.groupby(['year', 'month', 'date_number', 'date']).sum().reset_index()

    all_max = df_nem_compare['TOTALDEMAND'].max()
    all_min = df_nem_compare['TOTALDEMAND'].min()

    # ### Scatter plot ###
    if selected_data == 'Monthly':
        for i, y in enumerate(df_compare['year'].unique()[::-1]):
            df = df_nem_compare[df_nem_compare['year'] == y]

            fig_compare.add_trace(
                go.Scatter(
                    x=df['month'],
                    y=df['TOTALDEMAND'],
                    opacity=opacity[i],
                    line={
                        'color': 'black',
                        'width': width[i],
                        'dash': line[i],
                    },
                    hovertemplate=(
                            '<b>NEM Network</b><br><br>' +
                            '<i>%{x} ' + str(y) + '</i><br>' +
                            '<b>Demand</b>:<br>' +
                            '<b>%{y:,.0f} MW</b>' +
                            '<extra></extra>'
                    ),
                    hoverlabel=dict(
                        bgcolor='lightgrey'
                    ),
                    name='NEM {}<br>'.format(str(y)),
                ),
            )
    elif selected_data == 'Weekly':
        for i, y in enumerate(df_compare['year'].unique()[::-1]):
            df = df_nem_compare[df_nem_compare['year'] == y]

            fig_compare.add_trace(
                go.Scatter(
                    x=df['week'],
                    y=df['TOTALDEMAND'],
                    opacity=opacity[i],
                    line={
                        'color': 'black',
                        'width': width[i],
                        'dash': line[i],
                    },
                    hovertemplate=(
                            '<b>NEM Network</b><br><br>' +
                            '<i>Week %{x} - ' + str(y) + '</i><br>' +
                            '<b>Demand</b>:<br>' +
                            '<b>%{y:,.0f} MW</b>' +
                            '<extra></extra>'
                    ),
                    hoverlabel=dict(
                        bgcolor='lightgrey'
                    ),
                    name='NEM {}<br>'.format(str(y)),
                ),
            )
    else:
        for i, y in enumerate(df_compare['year'].unique()[::-1]):
            df = df_nem_compare[df_nem_compare['year'] == y]
            df['x'] = x_ticktext[:df.shape[0]]
            _start_date = str(y) + start_date[4:]
            _end_date = str(y) + end_date[4:]
            _df = df[df['date']
                .between(
                datetime.strptime(_start_date, '%Y-%m-%d'),
                datetime.strptime(_end_date, '%Y-%m-%d')
            )]
            fig_compare.add_trace(
                go.Scatter(
                    x=_df['x'],
                    y=_df['TOTALDEMAND'],
                    opacity=opacity[i],
                    line={
                        'color': 'black',
                        'width': width[i],
                        'dash': line[i],
                    },
                    hovertemplate=(
                            '<b>NEM Network</b><br><br>' +
                            '<i>%{x} ' + str(y) + '</i><br>' +
                            '<b>Demand</b>:<br>' +
                            '<b>%{y:,.0f} MW</b>' +
                            '<extra></extra>'
                    ),
                    hoverlabel=dict(
                        bgcolor='lightgrey'
                    ),
                    name='NEM {}<br>'.format(str(y)),
                ),
            )

    fig_compare.update_yaxes(range=[all_min * 0.90, all_max * 1.02], secondary_y=False)

    df_compare = df_compare[df_compare['year'] == selected_year]

    # ### Bar graph ###
    if selected_state is not None:
        if len(selected_state) == 0:
            fig_compare.update_yaxes(showgrid=True)
        else:
            fig_compare.update_yaxes(showgrid=False)

        if selected_data == 'Monthly':
            for s in selected_state:
                fig_compare.add_trace(
                    go.Bar(
                        x=df_compare[df_compare['REGION'] == s]['month'],
                        y=df_compare[df_compare['REGION'] == s]['TOTALDEMAND'],
                        marker={'color': state_color[s]},
                        opacity=0.4,
                        hovertemplate=(
                                '<b>' + s + '</b><br><br>' +
                                '<i>%{x}</i><br>' +
                                '<b>Demand</b>:<br>' +
                                '<b>%{y:,.0f} MW</b>' +
                                '<extra></extra>'
                        ),
                        name=s,
                    ),
                    secondary_y=True,
                )
        elif selected_data == 'Weekly':
            for s in selected_state:
                fig_compare.add_trace(
                    go.Bar(
                        x=df_compare[df_compare['REGION'] == s]['week'],
                        y=df_compare[df_compare['REGION'] == s]['TOTALDEMAND'],
                        marker={'color': state_color[s]},
                        opacity=0.4,
                        hovertemplate=(
                                '<b>' + s + '</b><br><br>' +
                                '<i>Week %{x} - ' +
                                str(selected_year) + '</i><br>' +
                                '<b>Demand</b>:<br>' +
                                '<b>%{y:,.0f} MW</b>' +
                                '<extra></extra>'
                        ),
                        name=s,
                    ),
                    secondary_y=True,
                )
        else:
            for s in selected_state:
                df = df_compare[df_compare['REGION'] == s]
                df['x'] = x_ticktext[:df.shape[0]]
                _df = df[df['date']
                    .between(
                    datetime.strptime(start_date, '%Y-%m-%d'),
                    datetime.strptime(end_date, '%Y-%m-%d')
                )]
                fig_compare.add_trace(
                    go.Bar(
                        x=_df['x'],
                        y=_df['TOTALDEMAND'],
                        marker={'color': state_color[s]},
                        opacity=0.4,
                        hovertemplate=(
                                '<b>' + s + '</b><br><br>' +
                                '<i>%{x}</i><br>' +
                                '<b>Demand</b>:<br>' +
                                '<b>%{y:,.0f} MW</b>' +
                                '<extra></extra>'
                        ),
                        name=s,
                    ),
                    secondary_y=True,
                )

    fig_compare.update_layout(
        title_text='<b>NEM</b> Total Demand Comparison (MW)',
        titlefont={'size': 25},
        yaxis_title="Total Demand (MW)",
        barmode='stack',
        legend_traceorder="grouped"
    )

    if selected_data == 'Monthly':
        fig_compare.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=months_val,
                ticktext=months
            ),
        )
    elif selected_data == 'Weekly':
        fig_compare.update_xaxes(tickmode='array', tickprefix='Week ', tickangle=90)

    return fig_compare


@app.callback(
    Output('demand-hourly-graph', 'figure'),
    [
        Input('year-dropdown', 'value'),
        Input('data-dropdown', 'value'),
        Input('start-period-dropdown', 'value'),
        Input('end-period-dropdown', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
        Input('state-dropdown', 'value'),
        Input('yrs-dropdown', 'value')
    ]
)
def update_hourly_graph(
        selected_year, selected_data, selected_start, selected_end,
        start_date, end_date, selected_state, yrs
):
    fig_hour = go.Figure()

    # col = 'RRP'
    col = 'TOTALDEMAND'

    if selected_state is None:
        selected_state = df_nem_tf['REGION'].unique()
    elif len(selected_state) == 0:
        selected_state = df_nem_tf['REGION'].unique()
    else:
        selected_state = selected_state

    yrs = 0 if yrs is None else yrs

    if selected_data == 'Monthly':
        df_hour = (df_nem_tf[
                       (df_nem_tf['year'].between(selected_year - yrs, selected_year)) &
                       (df_nem_tf['REGION'].isin(selected_state)) &
                       (df_nem_tf['month'].between(selected_start, selected_end))
                       ].groupby(['year', 'time', 'is_weekday']).mean()
                   .reset_index()
                   )

    elif selected_data == 'Weekly':
        df_hour = (df_nem_tf[
                       (df_nem_tf['year'].between(selected_year - yrs, selected_year)) &
                       (df_nem_tf['REGION'].isin(selected_state)) &
                       (df_nem_tf['week'].between(selected_start, selected_end))
                       ].groupby(['year', 'time', 'is_weekday']).mean()
                   .reset_index()
                   )

    else:
        _df = df_nem_tf[
            (df_nem_tf['REGION'].isin(selected_state)) &
            (df_nem_tf['date']
                .between(
                datetime.strptime(start_date, '%Y-%m-%d'),
                datetime.strptime(end_date, '%Y-%m-%d')
            )
            )
        ]

        for y in range(yrs):
            _start_date = str(selected_year - y - 1) + start_date[4:]
            _end_date = str(selected_year - y - 1) + end_date[4:]
            _df = pd.concat([_df,
                             df_nem_tf[
                                 (df_nem_tf['REGION'].isin(selected_state)) &
                                 (df_nem_tf['date']
                                    .between(
                                    datetime.strptime(_start_date, '%Y-%m-%d'),
                                    datetime.strptime(_end_date, '%Y-%m-%d')
                                 ))
                             ]])

        df_hour = (_df.groupby(['year', 'time', 'is_weekday']).mean()
                   .reset_index()
                   )

    title_text = 'Average Demand by Hour (MW) in '
    for i, s in enumerate(selected_state):
        if i == 0:
            title_text += f'<b> {s}</b>'
        else:
            title_text += f',<b> {s}</b>'

    max_demand = df_hour[col].max()
    min_demand = df_hour[col].min()

    weekday_obj = [
        {'name': 'weekday', 'is_weekday': True, 'color': 'rgba(255, 0, 0, 0.4)'},
        {'name': 'weekend', 'is_weekday': False, 'color': 'rgba(0, 0, 255, 0.4)'}
    ]

    for i, y in enumerate(df_hour['year'].unique()[::-1]):
        df = df_hour[df_hour['year'] == y]

        for o in weekday_obj:
            _df = df[df['is_weekday'] == o['is_weekday']]
            hoverlabel = {'bgcolor': o['color'], 'font': {'color': 'black'}}
            name = str(y) + ' - ' + o['name'].upper()

            fig_hour.add_trace(
                go.Scatter(
                    x=_df['time'], y=_df[col], name=name,
                    opacity=opacity[i],
                    line={
                        'color': o['color'],
                        'width': width[i],
                        'dash': line[i],
                    },
                    hovertemplate=(
                            '<b>' + name + '</b><br><br>' +
                            '<i>Time</i>: %{x}' +
                            '<br><b>Demand</b>: <b>%{y:.0f} MW<br>' +
                            '<extra></extra>'
                    ),
                    hoverlabel=hoverlabel,
                )
            )

    fig_hour.update_layout(
        # title_text=title_text,
        # titlefont={'size': 25},
        yaxis_title="Average Demand (MW)",
        legend=dict(
            yanchor="top",
            y=0.95,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(255, 255, 255, 0.5)'
        ),
        margin=dict(
            l=120, r=0, b=0, t=0, pad=0
        ),
    )
    fig_hour.update_yaxes(range=[min_demand * 0.98, max_demand * 1.02])
    fig_hour.update_xaxes(tickangle=45)

    return fig_hour


@app.callback(
    Output('avg-data-dropdown', 'options'),
    Output('avg-data-dropdown', 'value'),
    [Input('data-dropdown', 'value')]
)
def update_avg_data_dropdown(selected_data):
    if selected_data == 'Monthly':
        options = [
            {'label': 'Monthly', 'value': 'Monthly'},
            {'label': 'MA-2', 'value': 'MA-2'},
            {'label': 'MA-3', 'value': 'MA-3'},
        ]
        value = 'Monthly'
    elif selected_data == 'Weekly':
        options = [
            {'label': 'Weekly', 'value': 'Weekly'},
            {'label': 'MA-2', 'value': 'MA-2'},
            {'label': 'MA-4', 'value': 'MA-4'},
        ]
        value = 'Weekly'
    else:
        options = [
            {'label': 'Daily', 'value': 'Daily'},
            {'label': 'MA-7', 'value': 'MA-7'},
            {'label': 'MA-14', 'value': 'MA-14'},
            {'label': 'MA-28', 'value': 'MA-28'},
        ]
        value = 'MA-7'
    return options, value


@app.callback(
    Output('avg-graph', 'figure'),
    [
        Input('year-dropdown', 'value'),
        Input('data-dropdown', 'value'),
        Input('start-period-dropdown', 'value'),
        Input('end-period-dropdown', 'value'),
        Input('date-picker-range', 'start_date'),
        Input('date-picker-range', 'end_date'),
        Input('state-dropdown', 'value'),
        Input('yrs-dropdown', 'value'),
        Input('avg-data-dropdown', 'value')
    ]
)
def update_avg_graph_and_title(
        selected_year, selected_data, start_period, end_period,
        start_date, end_date, selected_state, yrs, data_value
):
    fig_avg = make_subplots(specs=[[{"secondary_y": True}]])

    if selected_state is None:
        selected_state = df_nem_tf['REGION'].unique()
    elif len(selected_state) == 0:
        selected_state = df_nem_tf['REGION'].unique()
    else:
        selected_state = selected_state

    yrs = 0 if yrs is None else yrs

    if selected_data == 'Monthly':
        df_avg = (df_nem_tf[
                      (df_nem_tf['year'].between(selected_year - yrs, selected_year))
                      & (df_nem_tf['REGION'].isin(selected_state))
                      & (df_nem_tf['month'].between(start_period, end_period))
                  ].groupby(['year', 'month']).mean()
                  .reset_index()
                  .drop(columns=['RRP', 'date_number', 'is_weekday', 'week'])
                  )

    elif selected_data == 'Weekly':
        df_avg = (df_nem_tf[
                      (df_nem_tf['year'].between(selected_year - yrs, selected_year))
                      & (df_nem_tf['REGION'].isin(selected_state))
                      & (df_nem_tf['week'].between(start_period, end_period))
                  ].groupby(['year', 'week']).mean()
                  .reset_index()
                  .drop(columns=['RRP', 'month', 'date_number', 'is_weekday'])
                  )

    else:
        df_avg = (df_nem_tf[
                      (df_nem_tf['year'].between(selected_year - yrs, selected_year))
                      & (df_nem_tf['REGION'].isin(selected_state))
                      & ~(
                              (df_nem_tf['month'] == 2) & (df_nem_tf['date_number'] == 29)
                      )
                  ].groupby(['year', 'date']).mean()
                  .drop(columns=['RRP', 'week', 'is_weekday'])
                  .reset_index()
                  )

    _df_cases = df_cases
    _df_cases['total_cases'] = 0

    for s in selected_state:
        _df_cases['total_cases'] = _df_cases['total_cases'] + _df_cases[s]

    if selected_data == 'Monthly':
        _df_cases = (_df_cases.groupby(['year', 'month']).sum()
                     .reset_index())
        df_avg = pd.merge(df_avg, _df_cases, how='left', on=['year', 'month'])

    elif selected_data == 'Weekly':
        _df_cases = (_df_cases.groupby(['year', 'week']).sum()
                     .reset_index())
        df_avg = pd.merge(df_avg, _df_cases, how='left', on=['year', 'week'])

    else:
        _df_cases = (_df_cases.groupby(['date']).sum()
                     .reset_index())
        df_avg = pd.merge(df_avg, _df_cases, how='left', on=['year', 'date'])

    df_avg['demand'] = (df_avg['TOTALDEMAND']
                        .rolling(rolling[data_value], win_type='triang')
                        .mean())

    for i, y in enumerate(df_avg['year'].unique()[::-1]):
        df = df_avg[df_avg['year'] == y]
        if selected_data == 'Monthly':
            selected_col = 'month'
        elif selected_data == 'Weekly':
            selected_col = 'week'
        else:
            df['x'] = x_ticktext[:df.shape[0]]

            _start_date = str(y) + start_date[4:]
            _end_date = str(y) + end_date[4:]
            df = df[df['date']
                .between(
                datetime.strptime(_start_date, '%Y-%m-%d'),
                datetime.strptime(_end_date, '%Y-%m-%d')
            )]

            selected_col = 'x'
        fig_avg.add_trace(
            go.Scatter(
                x=df[selected_col],
                y=df['demand'],
                name=str(y),
                opacity=opacity[i],
                line={
                    'dash': line[i],
                    'width': width[i],
                    'color': color_palette[i]
                },
                hovertemplate=(
                        '<b>' + str(y) +
                        ' %{x}</b><br><br>' +
                        '<b>Demand</b>: ' +
                        '<b>%{y:.0f} MW</b>' +
                        '<extra></extra>'
                ),
            )
        )

        if y == 2020:
            for s in selected_state:
                fig_avg.add_trace(
                    go.Bar(
                        x=df[selected_col],
                        y=df[s],
                        opacity=0.8,
                        marker_color=state_color[s],
                        showlegend=False,
                        name=s,
                        hovertemplate=(
                                '<b>' + s + '</b><br>' +
                                '<i>%{x}</i><br><br>' +
                                '<b>New cases</b>: ' +
                                '<b>%{y:.0f}</b>' +
                                '<extra></extra>'
                        ),
                    ),
                    secondary_y=True
                )

            max_cases = df['total_cases'].max()
            fig_avg.update_yaxes(
                range=[0, max_cases * 4],
                showgrid=False,
                showticklabels=False,
                secondary_y=True,
                autorange=False,
            )

    all_min = df_avg['demand'].min()
    all_max = df_avg['demand'].max()
    fig_avg.update_yaxes(range=[all_min * 0.95, all_max * 1.02], secondary_y=False)

    fig_avg.update_layout(
        yaxis_title="Average Demand (MW)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=0.9
        ),
        margin=dict(
            l=80, r=0, b=150, t=50, pad=0
        ),
        barmode='stack'
    )

    if selected_data == 'Monthly':
        fig_avg.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=months_val,
                ticktext=months
            ),
        )
    elif selected_data == 'Weekly':
        fig_avg.update_xaxes(tickmode='linear', tickprefix='Week ', tickangle=90)

    return fig_avg


@app.callback(
    Output('pv-graph-title', 'children'),
    Output('avg-graph-title', 'children'),
    Output('hr-graph-title', 'children'),
    [Input('state-dropdown', 'value')]
)
def update_graph_title(selected_state):
    title_text = ''
    for i, s in enumerate(selected_state):
        if i == 0:
            title_text += f' {s}'
        else:
            title_text += f', {s}'
    return title_text, title_text, title_text


@app.callback(
    Output('pv-graph', 'figure'),
    [
        Input('year-dropdown', 'value'),
        Input('data-dropdown', 'value'),
        Input('start-period-dropdown', 'value'),
        Input('end-period-dropdown', 'value'),
        Input('state-dropdown', 'value'),
        Input('yrs-dropdown', 'value'),
    ]
)
def update_pv_graph(selected_year, selected_data, start_period, end_period, selected_state, yrs):
    _df_pv = df_pv[
        (df_pv['year'].between(int(selected_year - yrs), int(selected_year)))
        # & (df_pv['month'].between(int(start_period), int(end_period)))
    ]

    _df_pv['total'] = 0
    for s in selected_state:
        _df_pv.loc[:, 'total'] = _df_pv.loc[:, 'total'] + _df_pv[s]

    fig_pv = go.Figure()

    for i, y in enumerate(_df_pv['year'].unique()[::-1]):
        df = _df_pv[_df_pv['year'] == y]

        fig_pv.add_trace(
            go.Scatter(
                x=df['month'],
                y=df['total'],
                name=str(y),
                opacity=opacity[i],
                line={
                    'dash': line[i],
                    'width': width[i],
                    'color': color_palette[i]
                },
                hovertemplate=(
                        '<b>' + str(y) +
                        ' %{x}</b><br><br>' +
                        '<b>PV Output</b>: ' +
                        '<b>%{y:.0f} MWh</b>' +
                        '<extra></extra>'
                ),
            )
        )

    all_min = _df_pv['total'].min()
    all_max = _df_pv['total'].max()
    fig_pv.update_yaxes(range=[all_min * 0.95, all_max * 1.02])

    fig_pv.update_layout(
        yaxis_title="Total Output (MWh)",
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=0.9
        ),
        # margin=dict(
        #     l=80, r=0, b=150, t=50, pad=0
        # ),
        margin=dict(
            l=120, r=20, b=0, t=0, pad=0
        ),
        barmode='stack'
    )

    fig_pv.update_layout(
        xaxis=dict(
            tickmode='array',
            tickvals=months_val,
            ticktext=months
        ),
    )

    return fig_pv


if __name__ == '__main__':
    # app.run_server(debug=True)  # for local dev
    # app.run_server(host='0.0.0.0', port=8050, debug=True)
    application.run(port=8050)
