import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd


def rank_comparison(data, x = "Rank", y = "Kills"):
    if y == 'Blocks per Set':
        z = 'Blocks_Per_Set'
    
    elif y == 'Games Played':
        z = 'Games_Played'

    elif y == 'Sets Played':
        z = 'Sets_Played'
    
    elif y == 'Kills per Set':
        z = 'Kills_Per_Set'
    
    elif y == 'Hitting Percentage':
       z = 'Hitting_Percentage'
    
    elif y == 'Assists per Set':
        z ='Assists_Per_set'
    
    elif y == 'Blocks per Set':
        z = 'Blocks_Per_Set'

    elif y == 'Digs per Set':
        z = 'Digs_Per_Set'
    
    elif y == 'Service Aces':
        z = 'Service_Aces'

    elif y == 'Aces per Set':
        z = 'Service_Aces_Per_Set'

    elif y == 'Reception Percentage':
        z ='Reception_Percentage'
    
    else:
        z = y
        
    fig = px.scatter(data, x, z, title=f"Rank Compared to {y}")
    return fig


def correlation_plot(data):
    data = data.select_dtypes(include='number')
    correlation_matrix = data.corr().round(2)
    correlation_matrix = correlation_matrix.fillna(0)

    fig2 = px.imshow(
        correlation_matrix,
        text_auto=True,
        color_continuous_scale="RdBu",
        title="Correlation of Skills by Rank",
        labels=dict(color="Correlation")
    )
    return fig2