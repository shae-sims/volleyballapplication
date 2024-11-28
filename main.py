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

data = pd.read_csv("data2023Clean.csv")

st.title('Big 10 Volleyball Ranking Comparions 2023')

tab1, tab2 = st.tabs(['By Rank', 'Individual Players'])

with tab1:

    # # Filter numeric columns
    # df = data.select_dtypes(include='number')
    # correlation_matrix = df.corr().round(2)

    # # Create a heatmap with Seaborn
    # plt.figure(figsize=(8, 6))
    # sns.heatmap(
    #     correlation_matrix, 
    #     annot=True, 
    #     cmap='coolwarm', 
    #     square=True, 
    #     fmt=".2f"
    # )
    # plt.title('Correlation Heatmap')

    # # Display the heatmap in Streamlit
    # st.pyplot(plt)
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

    
    with col2:

        fig1 = rank_comparison(data, y = skill)
        st.plotly_chart(fig1)