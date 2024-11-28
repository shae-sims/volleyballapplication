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

    input_skill = st.radio('Select a Skill',[3,5,10])

    fig1 = rank_comparison(data, y = "Blocks per Set")
    st.plotly_chart(fig1)