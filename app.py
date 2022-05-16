import streamlit as st
import pandas as pd

st.header('Training Application')
players = pd.read_csv('players.csv',index_col=0)

name = st.text_input('Player Name')

tac = st.number_input('Tactical Score',step=.5,min_value=1.0,max_value=5.0)

tech = st.number_input('Techincal Score',step=.5,min_value=1.0,max_value=5.0)

phys = st.number_input('Physicality Score',step=.5,min_value=1.0,max_value=5.0)

ment = st.number_input('Mentality Score',step=.5,min_value=1.0,max_value=5.0)


overall = ((26*tac + 16*tech + 30*ment + 28*phys) / 5)

st.text('Weighted Average: ' + str(overall))
                  
    
if(st.button('Add Player')):
    players.loc[len(players.index)] = [name,tac,tech,phys,ment,overall]
    players.to_csv('players.csv')
    
st.dataframe(players)

if st.button('Clear Players'):
    dat = pd.DataFrame(columns = ['name','tactical','technical','physical','mental','overall'])
    dat.to_csv('players.csv')