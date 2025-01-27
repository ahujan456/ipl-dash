import streamlit as st
import pandas as pd
df = pd.read_csv('data/deliveries_edited.csv')
opt = st.sidebar.selectbox('Select One', ['Batter Analysis', 'Bowler Analysis', 'Team Analysis'])

if opt == 'Batter Analysis':
    g_obj = df.groupby(['batter', 'match_id'])
    st.title('Batter Analysis')
    st.sidebar.title('Batter Analysis')
    batter = st.sidebar.selectbox('Select Batter', df['batter'].unique())
    st.header(batter)
    df_batter = df.groupby('batter')
    # st.subheader(f"Total Runs in IPL:{(df_batter['batsman_runs'][batter])}")
    r1col1, r1col2, r1col3 = st.columns(3)

    with r1col1:
        st.metric('Total Runs in IPL', (df_batter['batsman_runs'].sum()[batter]))

    with r1col2:
        runs = df_batter['batsman_runs'].sum()[batter]
        balls_played = df_batter['batsman_runs'].count()[batter]
        sr = (runs/balls_played)*100
        st.metric('Strike Rate', round(sr, 1))
    
    with r1col3:
        
        st.metric('Match Played', g_obj.sum()['inning'][batter].count())

    
    r2col1, r2col2, r2col3 = st.columns(3)

    with r2col1:
        g_obj.sum()['batsman_runs'][batter].max()

    

    
    


elif opt == 'Bowler Analysis':
    st.title('Bowler Anlaysis')

else:
    st.title('Team Analysis')