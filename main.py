import numpy as np
import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import requests
import seaborn as sns
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plots import *
import streamlit as st

data = pd.read_csv("data2023Clean.csv").drop(columns = 'Unnamed: 0')

st.title('Big 10 Volleyball Ranking Comparions 2023')

tab1, tab2 = st.tabs(['By Rank', 'Individual Players'])

with tab1:

    col1, col2 = st.columns(2)
    with col1:
        skill = st.selectbox(
    "Select a Skill to Compare with Rank",
    ('Games Played', 'Sets Played', 'Kills', 'Kills per Set',
       'Hitting Percentage', 'Assists', 'Assists per Set', 'Blocks',
       'Blocks per Set', 'Digs', 'Digs per Set', 'Service Aces',
       'Aces per Set', 'Reception Percentage'))
        if skill == 'Blocks per Set':
            skill1 = 'Blocks_Per_Set'
        
        elif skill == 'Games Played':
            skill1 = 'Games_Played'

        elif skill == 'Sets Played':
            skill1 = 'Sets_Played'
        
        elif skill == 'Kills per Set':
            skill1 = 'Kills_Per_Set'
        
        elif skill == 'Hitting Percentage':
            skill1 = 'Hitting_Percentage'
        
        elif skill == 'Assists per Set':
            skill1 ='Assists_Per_set'
        
        elif skill == 'Blocks per Set':
            skill1 = 'Blocks_Per_Set'

        elif skill == 'Digs per Set':
            skill1 = 'Digs_Per_Set'
        
        elif skill == 'Service Aces':
            skill1 = 'Service_Aces'

        elif skill == 'Aces per Set':
            skill1 = 'Service_Aces_Per_Set'

        elif skill == 'Reception Percentage':
            skill1 ='Reception_Percentage'
        
        else:
            skill1 = skill
        
        cor = data['Rank'].corr(data[skill1]).round(2)
        st.write(f"The correlation between Rank and **{skill}** is **{cor}**.")
    
    with st.expander("Explanation of Skills"):
        st.write('''
        Rank: The ranking of the players from 1-168. One being high.
                 
        Games Played: The number of games an athlete competed in (also known as matchs). One game is composed of 3-5 different sets.
                 
        Sets Played: The number os sets played by the athletes. A set goes to 25 and you must win by 2. The fifth set goes to 15 if necessary. 
                 You must win 3 sets to win the game.

        Kills/ Kills per Set: A kill is when a player hits the ball and it results in a point for their team. 
                 Kills is the total number and kills per set is based of each individual set.

        Hitting Percentage: A percentage ranging from 1 to -1. Players are ranked off of kills, hitting errors, and hitting attempts (player hits the ball and it is played by the other team)
                 If they have all kills it will be a 1, if they have all errors it is a -1.

        Assists/ Assists per Set: An offensive move that gives another player an opportunity to hit the ball.
                 
        Digs/ Digs per Set: When a player successfully passes a hard driven ball. 
                 
        Service Aces/ Aces per Set: When a player serves the ball and recieves a point.
                 
        Reception Percentage: The percentage that a player has a good pass when receiving a serve.
        
        ''')

    
    with col2:

        fig1 = rank_comparison(data, y = skill)
        st.plotly_chart(fig1)

    #Filter numeric columns
    df = data.select_dtypes(include='number')
    correlation_matrix = df.corr().round(1)

    # Create a heatmap with Seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap='coolwarm', 
        square=True, 
        fmt=".2f"
    )
    plt.title('Correlation Heatmap')

    # Display the heatmap in Streamlit
    st.pyplot(plt)