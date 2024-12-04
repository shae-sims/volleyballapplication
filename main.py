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
    st.title('Welcome to the Volleyball Data Explorer!')
    st.markdown("""
    ### Introduction
    This is an interactive app designed to help you explore volleyball data and see what you can find. No matter who you are this app can help analyze and compare player performance and outcomes in new ways.""")
    st.markdown("""
    #### What You Will Find
    On the next page, called "Graphics and Exploration" you will find two tabs:
    1. **Correlation**
        This tab allows you to explore the correlations between different variables. One being player rankings! It gives specific insights into what really effects players standings in their division.
    2. **Individual Players**
        This tab allows you to explore individuals and groups of players you can do this by:
        - Selecting whether you want to see the top-ranked players, lowest-ranked players, or a random selection of players.
        - Selecting the number of players you would like to see
        - Selecting which skills you would like to compare
        You will be able to see a graph that shows all this information and it will also be displayed in  an easy to read table.
    """)
    st.markdown("""
    #### Customization & Interactivity
    Most graphs, except the correlation matrix on the first tab, allow you to select specific skills to display. Some charts even provide additional customization options to empower you to uncover unique insights.
    """)
    st.markdown("""
    #### The Data Behind the App
    This application uses data from the Big 10 colliegiate volleyball conference. It has information on players rank based of off important skills
    The information you will find on each player are:
        1. Rank: How th player is ranked in comparison to all other athletes in the Big 10, 1 being the highest rank.
        2. Name: The name of the athlete
        3. Games Played: The number of games played by an athlete each game is made up of 3-5 sets. Teams must win 3 sets to win a game.
        4. Sets Played:	The number of sets played by an athlete. Sets are played to 25 and you must win by 2 points. If a fifth set is necessary it is played to 15.
        5. Kills: An offensive attack on a ball that results in a point to the team that hit it. This is the total amount of kills for that player
        6. Kills per Set: The number of kills per set player
        7. Hitting Percentage: A score given to an athlete from -1 to 1. 1 meaning they always hit kills, -1 meaning they only hit errors (meaning it results in points for the other team)
        8. Assists: An overhand touch on the ball that results in a hitter getting a kill. The total amount for all the games.
        9. Assists per Set: The number of assists per set played
        10.	Blocks: A defensive move that is when a player jumps up at the net to stop an opposing player from hitting the ball over.
        11.	Blocks per Set: The number of blocks per set played.
        12.	Digs: Passing a hard driven ball successfully.
        13.	Digs per Set: The number of Digs per set played
        14.	Service Aces(Aces): When a player serves a ball over the net and it results in a point.
        15.	Service Aces per Set: The number of aces per set player
        16.	Reception Percentage: The percentage of good receptions a player has compared to the total amount of receptions.
    """)
    st.markdown("""
    #### Ready, Set, GO!
    Now that you know a little more about this app. Click on the " Graphics and Exploration" in the sidebar to start your journey!
    """)


    
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
        st.table(sortdata.reset_index(drop=True))

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


