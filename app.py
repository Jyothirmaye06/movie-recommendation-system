import streamlit as st
import pickle
import pandas as pd

movies = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]

    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x:x[1])[1:6]

    recommended = []

    for i in movies_list:
        recommended.append(movies.iloc[i[0]].title)

    return recommended


st.title("Movie Recommendation System")

selected_movie = st.selectbox(
    "Select Movie",
    movies['title'].values
)

if st.button("Recommend"):

    recommendations = recommend(selected_movie)

    for i in recommendations:
        st.write(i)