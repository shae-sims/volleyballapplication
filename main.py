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

if "current_page" not in st.session_state:
    st.session_state.current_page = "Introduction"

st.sidebar.title("Navigation")
if st.sidebar.button("Introduction"):
    st.session_state.current_page = "Introduction"
if st.sidebar.button("Graphics and Exploration"):
    st.session_state.current_page = "Graphics and Exploration"

if st.session_state.current_page == "Introduction":
    st.header("Introduction")
    st.subheader('This App')
    st.write('This app is designed to help you explore volleyball data. It looks into how player rankings are decided and compares different players to each other')
    st.write('The next page of this application has two tabs. The first looks at the correlation of different skills in the game of volleyball compared to rank, and compared to each other.')
    st.write('The other tab has players stats that you can compare. The graph will display the highest ranked players, the lowest ranked players, and random list of players to compare their skills. There is also a table displaying all the players names in order of ranking.')
    st.write('For each graph, except the correlation matrix on the bottom of the first tab, the user can pick which skills are being displayed. Some graphs allow more user input to see what you can discover.')
    st.subheader("The Data")
    st.write('This application is made using data found from the Big 10 collegiate volleyball conference. They are ranked based off of different skills that they perform throughout volleyball games')
    
elif st.session_state.current_page == "Graphics and Exploration":
    tab1, tab2 = st.tabs(['Correlation', 'Individual Players'])

    with tab1:
        st.header('Comparision of Different Variables and Rank')
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

        col1, col2 = st.columns(2)
        with col1:
            skill = st.selectbox(
        "Select a Skill to Compare with Rank",
        ('Games Played', 'Sets Played', 'Kills', 'Kills per Set',
        'Hitting Percentage', 'Assists', 'Assists per Set', 'Blocks',
        'Blocks per Set', 'Digs', 'Digs per Set', 'Service Aces',
        'Aces per Set', 'Reception Percentage'))
            skill1 = get_right_name(skill)
            cor = data['Rank'].corr(data[skill1]).round(2)
            st.write()
            st.write()
            st.write(f"The correlation between Rank and **{skill}** is **{cor}**.")
            st.write()
            st.write(f"The highest value for **{skill}** is **{data[skill1].max()}**")
            highest = data[data[skill1] == data[skill1].max()]
            ranks = highest['Rank'].tolist()
            name = highest['Name'].tolist()
            st.write(f"At rank(s): {', '.join(map(str, ranks))}")  # Convert rank list to a comma-separated string
            st.write(f"By player(s): {', '.join(name)}")
            st.write()
            st.write(f"The lowest value for **{skill}** is **{data[skill1].min()}**")
            lowest = data[data[skill1] == data[skill1].min()]
            ranks = lowest['Rank'].tolist()
            st.write(f"At rank(s): {', '.join(map(str, ranks))}")


        
        with col2:

            fig1 = rank_comparison(data, y = skill)
            st.plotly_chart(fig1)

        st.header('Comparison of Different Numerical Values')

        col3, col4 = st.columns(2)
        with col3:
            x = st.selectbox(
        "Select two Variables to Compare to Each Other",
        ('Games Played', 'Sets Played', 'Kills', 'Kills per Set',
        'Hitting Percentage', 'Assists', 'Assists per Set', 'Blocks',
        'Blocks per Set', 'Digs', 'Digs per Set', 'Service Aces',
        'Aces per Set', 'Reception Percentage'))
            
            y = st.selectbox("",
        ('Games Played', 'Sets Played', 'Kills', 'Kills per Set',
        'Hitting Percentage', 'Assists', 'Assists per Set', 'Blocks',
        'Blocks per Set', 'Digs', 'Digs per Set', 'Service Aces',
        'Aces per Set', 'Reception Percentage'))
            
            x1 = get_right_name(x)
            y1 = get_right_name(y)
            
            cor = data[x1].corr(data[y1]).round(2)
            st.write()
            st.write()
            st.write(f"The correlation between **{x}** and **{y}** is **{cor}**.")
            st.write()
            st.write(f"The highest value for **{x}** is **{data[x1].max()}**")
            st.write()
            st.write(f"The highest value for **{y}** is **{data[y1].max()}**")
            st.write()
            st.write(f"The lowest value for **{x}** is **{data[x1].min()}**")
            st.write()
            st.write(f"The lowest value for **{y}** is **{data[y1].min()}**")
        with col4:

            fig3 = rank_comparison(data, x = x, y = y)
            st.plotly_chart(fig3)

        st.header("Complete Correlation Matrix")

        #Filter numeric columns
        df = data.select_dtypes(include='number')
        correlation_matrix = df.corr().round(1)

        # Create a heatmap with Seaborn
        plt.figure(figsize=(8, 6))
        sns.heatmap(
            correlation_matrix, 
            annot=True, 
            cmap='coolwarm', 
            square=True
        )
        plt.title('Correlation Heatmap')

        # Display the heatmap in Streamlit
        st.pyplot(plt)
    
    with tab2:
        st.header('Individual Player Statistics')

        col5, col6 = st.columns(2)
        with col5:
            try:
                number = int(st.text_input('Enter the number of Athletes you want to see: ', value="5"))  # Default to 5
                if number <= 0 or number > 205:
                    st.error("Please enter a number between 1 and 205.")
                    st.stop()
            except ValueError:
                st.error("Please enter a valid number.")
                st.stop()
            st.write('*Between 1 and 205*')
            direct = st.radio('Select if you want to see Highest Ranked, Lowest Ranked, or Random', ['Highest','Lowest','Random'])
            var = st.selectbox(
        "Which skill do you want to see?",
        ('Games Played', 'Sets Played', 'Kills', 'Kills per Set',
        'Hitting Percentage', 'Assists', 'Assists per Set', 'Blocks',
        'Blocks per Set', 'Digs', 'Digs per Set', 'Service Aces',
        'Aces per Set', 'Reception Percentage'))
        
        with col6:
            fig5, sortdata = barplot(data, 'Name', var, number, direct)
            st.plotly_chart(fig5)

        st.table(sortdata)

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


