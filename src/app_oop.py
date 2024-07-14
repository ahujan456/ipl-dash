import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

class Batter:
    def __init__(self) -> None:
        self.df = pd.read_csv('data/deliveries_edited.csv')
        self.batter = ''
        self.opt = st.sidebar.selectbox('Select One', ['Batter Analysis', 'Bowler Analysis', 'Team Analysis'])
        self.g_obj = self.df.groupby(['batter', 'match_id'])
        self.df_batter = self.df.groupby('batter')
        self.batter_dashboard()
    
    def batter_dashboard(self):
        st.title('Batter Analysis')
        st.sidebar.title('Batter Analysis')
        self.batter = st.sidebar.selectbox('Select Batter', self.df['batter'].unique())
        st.header(self.batter)

        r1col1, r1col2, r1col3 = st.columns(3)
        with r1col1:
            st.metric('Total Runs in IPL', (self.df_batter['batsman_runs'].sum()[self.batter]))
        with r1col2:
            runs = self.df_batter['batsman_runs'].sum()[self.batter]
            balls_played = self.df_batter['batsman_runs'].count()[self.batter]
            sr = (runs/balls_played)*100
            st.metric('Strike Rate', round(sr, 1))
        with r1col3:
            st.metric('Match Played', self.g_obj.sum()['inning'][self.batter].count())

        r2col1, r2col2, r2col3 = st.columns(3)
        with r2col1:
            st.metric('Highest Score', self.g_obj['batsman_runs'].sum()[self.batter].max())
        with r2col2:
            st.metric('Average', round(runs/self.df[self.df['is_wicket']==1].groupby('batter')['batter'].count()[self.batter], 1))
        with r2col3:
            st.metric('Sixes', self.df[self.df['batsman_runs']==6].groupby('batter')['batter'].count()[self.batter])

        vals = self.df.groupby(['batter', 'batting_team'])['batsman_runs'].sum()[self.batter].to_list()
        lab = self.df.groupby(['batter', 'batting_team'])['batsman_runs'].sum()[self.batter].index
        fig, ax = plt.subplots()
        ax.pie(vals, labels=lab, autopct='%1.1f%%')
        st.pyplot(fig=fig)



Dash = Batter()


