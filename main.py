import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

def categorize(row):
    if row['category'] == 'video' and not row['shorts']:
        return 'movie'
    elif row['category'] == 'video' and row['shorts']:
        return 'short'
    else:
        return 'ad'

file = st.file_uploader("Upload a JSON")

if file != None:

    file = pd.read_json(file)

    file = file[file['time'].str[:4] == '2024']
    file = file.drop(['header', 'details', 'description', 'products'], axis='columns')
    file['category'] = file['activityControls'].apply(len)
    file['category'] = file['category'].map({1: 'video', 2: 'ads', 3: 'ads'})
    file['shorts'] = file['title'].str.contains('#shorts')
    file['type'] = file.apply(categorize, axis=1)

    movies = file[file['type'] == 'movie']
    movies['channel'] = movies['subtitles'].str[0].str['name']
    movies['date'] = pd.to_datetime(movies['time'].str[:10])
    movies['title'] = movies['title'].str[8:]

    movies['weekday'] = movies['date'].dt.day_name()
    weekday_amount = movies[['date', 'weekday']].drop_duplicates()
    weekday_amount = weekday_amount['weekday'].value_counts()
    weekday_counter = movies['weekday'].value_counts()
    weekwatch = weekday_counter / weekday_amount
    weekwatch.name = 'video per day'

    movies['months'] = movies['date'].dt.month_name()
    movies['days_in_month'] = movies['date'].dt.to_period('M').dt.days_in_month
    month_amount = movies[['months', 'days_in_month']].drop_duplicates()
    month_amount = month_amount.set_index('months')
    month_counter = movies['months'].value_counts()
    month_amount = month_amount['days_in_month']
    month_amount = month_amount.sort_index()
    month_counter = month_counter.sort_index()
    monthwatch = month_counter / month_amount
    monthwatch.name = 'video per day'
    month_amount.name = 'amount'

    type_counter = file['type'].value_counts()
    videos_counter = movies['title'].value_counts()
    top_days = movies['date'].value_counts()
    channel_counter = movies['channel'].value_counts()

    movies['hours'] = movies['time'].str[11:13]
    hourwatch = movies['hours'].value_counts() / 365
    hourwatch.name = 'video per hour'

    date_watch = movies['date'].drop_duplicates()

    st.title("📊 Your YouTube Wrapped 2024")
    st.markdown("---")

    st.header("✨ Key Numbers")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("📅 Days without YouTube", 365 - len(date_watch))
    col2.metric("🎥 Movies per day", round(type_counter.loc['movie'] / 365, 2))
    col3.metric("🔥 Movies on active days", round(type_counter.loc['movie'] / len(date_watch), 2))
    col4.metric("🎬 Total movies", type_counter.loc['movie'])

    st.subheader("📊 Content Breakdown")
    st.dataframe(type_counter.to_frame(name="Count"))

    st.markdown("---")

    st.header("🏆 Your Highlights")
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📅 Top 3 Days")
        st.dataframe(top_days.head(3))
    with c2:
        st.subheader("🎥 Top 3 Videos")
        st.dataframe(videos_counter.head(3))

    st.subheader("📺 Top 5 Channels")
    st.dataframe(channel_counter.head(5))

    st.markdown("---")

    st.header("⏰ When Do You Watch the Most?")
    c3, c4 = st.columns(2)
    with c3:
        st.subheader("🕒 Hours")
        st.bar_chart(hourwatch)
    with c4:
        st.subheader("📆 Days of the Week")
        st.bar_chart(weekwatch)

    st.markdown("---")

    st.header("📈 Watching Trends Over the Year")
    st.bar_chart(monthwatch)
    st.bar_chart(month_counter)

    st.markdown("---")

    st.header("📜 Summary")
    st.markdown(f"""
    - You watched **{type_counter.loc['movie']}** movies 🎬
    - You watched **{type_counter.loc['short']}** shorts 🎞
    - You saw **{type_counter.loc['ad']}** ads 📢
    - Your peak watching hour: **{hourwatch.idxmax()}**
    - Your most active day: **{top_days.idxmax().strftime('%Y-%m-%d')}** 📅
    - Your most watched channel: **{channel_counter.index[0]}**
    """)