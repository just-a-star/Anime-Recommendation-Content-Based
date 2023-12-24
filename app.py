import pickle
import streamlit as st

def recommend(anime):
    index = animes[animes['Name'] == anime].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_anime_names = []
    recommended_anime_posters = []


    for i in distances[1:6]:  # Fetch the top 5 recommendations
        recommended_anime_id = animes.iloc[i[0]]['anime_id']  # Get the anime_id of the recommended anime
        recommended_anime_poster = animes[animes['anime_id'] == recommended_anime_id]['Image URL'].iloc[0]
        
        recommended_anime_names.append(animes.iloc[i[0]].Name)
        recommended_anime_posters.append(recommended_anime_poster)

    return recommended_anime_names, recommended_anime_posters


st.header('Rekomendasi Anime Menggunakan Content Based Recommendation')

# Load 'animes' using pickle
animes = pickle.load(open('anime.list.pkl', 'rb'))

# Load 'similarity' using pickle
similarity = pickle.load(open('similarity.pkl', 'rb'))

anime_list = animes['Name'].values
selected_anime = st.selectbox(
    "Tulis Judul Anime",
    anime_list
)

if st.button('Show Recommendation'):
    recommended_anime_names, recommended_anime_posters = recommend(selected_anime)
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.text(recommended_anime_names[i])
            st.image(recommended_anime_posters[i])
