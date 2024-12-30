import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

base_url = 'https://raw.githubusercontent.com/practical-jupyter/sample-data/master/anime/'
anime_genre_top10_csv = os.path.join(base_url, 'anime_genre_top10.csv')
top10_df = pd.read_csv(anime_genre_top10_csv)

st.title("Anime Genre Members Visualization")
types = st.selectbox('Select Type', top10_df['type'].unique())

if st.button('Display Chart'):
    filter_by_type = top10_df[top10_df['type'] == types]
    plot_data = filter_by_type.groupby('genre').sum()['members']
    st.bar_chart(plot_data)
