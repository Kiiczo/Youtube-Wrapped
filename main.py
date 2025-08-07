import pandas as pd
import streamlit as st
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

movies['date'] = pd.to_datetime(file['time'].str[:10])

movies['weekday'] = movies['date'].dt.day_name()
weekday_amount = movies[['date','weekday']].drop_duplicates()
weekday_amount = weekday_amount['weekday'].value_counts()
weekday_counter = movies['weekday'].value_counts()
weekwatch = weekday_counter / weekday_amount

movies['months'] = movies['date'].dt.month_name()
movies['days_in_month'] = movies['date'].dt.to_period('M').dt.days_in_month
month_amount = movies[['months', 'days_in_month']].drop_duplicates()
month_amount = month_amount.set_index('months')
month_counter = movies['months'].value_counts()
month_amount = month_amount['days_in_month']
month_amount = month_amount.sort_index()
month_counter = month_counter.sort_index()
monthwatch = month_counter / month_amount

videos_counter = movies['title'].value_counts()

type_counter = file['type'].value_counts()

movies['hours'] = movies['time'].str[11:13]
hourwatch = movies['hours'].value_counts() / 365

days = movies['date'].value_counts()

date_watch = movies['date'].drop_duplicates()

st.write("Days without YT:")
st.write(365 - len(date_watch))

st.write("Top 3 days")
st.dataframe(days.head(3))

st.write("Top 3 videos")
st.dataframe(videos_counter.head(3))


st.write("Type counter")
st.dataframe(type_counter)

st.write("Watch per day")
st.write(type_counter.loc['movie'] / 365)

st.write("Real watch per day")
st.write(type_counter.loc['movie'] / len(date_watch))

st.write("Watch per month")
st.bar_chart(monthwatch)

st.write("Watch per hour")
st.bar_chart(hourwatch, horizontal=True)

st.write("Watch per week")
st.bar_chart(weekwatch)