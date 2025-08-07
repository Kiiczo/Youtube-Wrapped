import pandas as pd
import streamlit as st
import datetime

with open('watch-history.json') as f:
    file = pd.read_json(f)

def categorize(row):
    if row['category'] == 'video' and not row['shorts']:
        return 'movie'
    elif row['category'] == 'video' and row['shorts']:
        return 'short'
    else:
        return 'ad'

file = file[file['time'].str[:4] == '2024']

file = file.drop(['header','details','description','products','subtitles'],axis='columns')

file['category'] = file['activityControls'].apply(len)
file['category'] = file['category'].map({1: 'video', 2: 'ads', 3: 'ads'})
file['shorts'] = file['title'].str.contains('#shorts')

file['type'] = file.apply(categorize, axis=1)

movies = file[file['type'] == 'movie']
movies['months'] = file['time'].str[5:7]
movies['hours'] = file['time'].str[11:13]
movies['date'] = file['time'].str[5:10]

counter = file['type'].value_counts()

monthwatch = movies.groupby('months').size().to_frame(name='movie_count')
hourwatch = movies.groupby('hours').size().to_frame(name='per_day') / 365

days = movies['date'].value_counts()
st.dataframe(days)

st.dataframe(movies)
st.dataframe(counter)
st.bar_chart(monthwatch)
st.bar_chart(hourwatch, horizontal=True)