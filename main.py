import numpy as np
import pandas as pd
import zipfile
import plotly.express as px
import matplotlib.pyplot as plt
import requests
from io import BytesIO
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from plots import *
import streamlit as st

data = pd.read_csv("data2023Clean.csv")

st.title('Big 10 Volleyball Ranking Comparions 2023')

fig1 = rank_comparison(data, y = "Blocks per Set")
st.plotly_chart(fig1)