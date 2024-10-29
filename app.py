import pickle
import streamlit as st
import numpy as np
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url(https://images2.alphacoders.com/261/26102.jpg);
background-size: cover;

}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.header("Book Recommendation System Using Machine Learning")
model = pickle.load(open('Artifacts/model.pkl','rb'))
books_name = pickle.load(open('Artifacts/books_name.pkl','rb'))
final_rating = pickle.load(open('Artifacts/final_rating.pkl','rb'))
book_pivot = pickle.load(open('Artifacts/book_pivot.pkl','rb'))
def fetch_poster(suggestion):
    book_name=[]
    ids_index=[]
    poster_url=[]
    for book_id in suggestion:
        book_name.append(book_pivot.index[book_id])
    for name in book_name[0]:
        ids = np.where(final_rating['title']== name)[0][0]
        ids_index.append(ids)
    for ids in ids_index:
        url= final_rating.iloc[ids]['image']
        poster_url.append(url)
    return poster_url
def recommend_books(book_name):
    book_list=[]
    book_id = np.where(book_pivot.index==book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id].values.reshape(1,-1),n_neighbors=6)
    poster_url = fetch_poster(suggestion)
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for i in books:
            book_list.append(i)
    return book_list, poster_url
selected_books = st.selectbox("Type or select a book",books_name)
if st.button('Show Similar Books'):
    recommendation_books, poster_url = recommend_books(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(recommendation_books[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_books[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_books[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_books[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_books[5])
        st.image(poster_url[5])