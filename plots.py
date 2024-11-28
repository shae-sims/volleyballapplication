import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def get_right_name(var):
    if var == 'Blocks per Set':
        return 'Blocks_Per_Set'
        
    elif var == 'Games Played':
        return 'Games_Played'

    elif var == 'Sets Played':
        return 'Sets_Played'
    
    elif var == 'Kills per Set':
        return 'Kills_Per_Set'
    
    elif var == 'Hitting Percentage':
        return 'Hitting_Percentage'
    
    elif var == 'Assists per Set':
        return 'Assists_Per_set'
    
    elif var == 'Blocks per Set':
        return 'Blocks_Per_Set'

    elif var == 'Digs per Set':
        return'Digs_Per_Set'
    
    elif var == 'Service Aces':
        return 'Service_Aces'

    elif var == 'Aces per Set':
        return 'Service_Aces_Per_Set'

    elif var == 'Reception Percentage':
        return 'Reception_Percentage'
    
    else:
        return var


def rank_comparison(data, x = "Rank", y = "Kills"):
    z = get_right_name(y)
    d = get_right_name(x)
        
    fig = px.scatter(data, d, z, title=f"{x} Compared to {y}")
    return fig
