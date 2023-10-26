# streamlit Library to create a website without using flask

import streamlit as st

import pickle

import pandas as pd

import requests


# creating an api fetch function to display the movie image and content
# streamlit run main.py

def fetch_poster(movie_id):
  try:
    url = "https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path
  except Exception as e:
    print(e)
# def fetch_poster(movie_id):
#     url = "https://mdblist.p.rapidapi.com/"
#
#     querystring = {"tm": movie_id}
#
#     headers = {
#         "X-RapidAPI-Key": "1dbe90f177msh6129ff1b21ff884p166020jsn8349ccb9c264",
#         "X-RapidAPI-Host": "mdblist.p.rapidapi.com"
#     }
#
#     response = requests.get(url, headers=headers, params=querystring)
#
#     data=response.json()
#     return data["poster_path"]

# creating a recommend function by taking reference from pkl file
# Creating a function which which will return the top 5 movies which nearest similar to the given data
def recommend(movie):
  try:
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:10]

    recommended_movies=[]
    recommended_movies_posters=[]


    for i in movies_list:
        #print(i[0])
        movie_id=movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from TMDB api
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_posters
    
  except Exception as e:
    print(e)


#creating a variable which will restore the file data in variable to display on web page
movies_dict = pickle.load(open("movie_dict.pkl","rb"))

movies=pd.DataFrame(movies_dict)

similarity=pickle.load(open("similarity.pkl","rb"))


st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Please type or select your movie preference?',
    movies["title"].values)


if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader(names[0])
        st.image(posters[0])

    with col2:
        st.subheader(names[1])
        st.image(posters[1])

    with col3:
        st.subheader(names[2])
        st.image(posters[2])

    st.divider()




    # with col5:
    #     st.text(names[4])
    #     st.image(posters[4])
# if st.button('Recommend'):
    names,posters=recommend(selected_movie_name)

    col4, col5, col6 = st.columns(3)

    with col4:
        st.subheader(names[3])
        st.image(posters[3])

    with col5:
        st.subheader(names[4])
        st.image(posters[4])

    with col6:
        st.subheader(names[5])
        st.image(posters[5])

    st.divider()

    names, posters = recommend(selected_movie_name)

    col7, col8, col9 = st.columns(3)

    with col7:
        st.subheader(names[6])
        st.image(posters[6])

    with col8:
        st.subheader(names[7])
        st.image(posters[7])

    with col9:
        st.subheader(names[8])
        st.image(posters[8])


