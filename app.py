import streamlit as st
import joblib
import difflib
from sklearn.metrics.pairwise import cosine_similarity

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="🎬 Movie Recommendation System",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- CUSTOM CSS ---------------- #

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

h1 {
    text-align: center;
    color: white;
}

.movie-card{
    background:#262730;
    padding:18px;
    border-radius:12px;
    margin-bottom:15px;
    border-left:6px solid #FF4B4B;
}

.similarity{
    color:#00FF99;
    font-weight:bold;
}

.footer{
    text-align:center;
    color:gray;
    padding-top:30px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #

@st.cache_resource
def load_model():

    df = joblib.load("movies_df.pkl")

    feature_vectors = joblib.load("feature_vectors.pkl")

    similarity = cosine_similarity(feature_vectors)

    return df, similarity


df, similarity = load_model()

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🎬 Movie Recommendation")

st.sidebar.markdown("---")

st.sidebar.subheader("About")

st.sidebar.info(
"""
This project recommends movies using:

✅ Content-Based Filtering

✅ TF-IDF Vectorization

✅ Cosine Similarity

Dataset:
TMDB 5000 Movies Dataset
"""
)

st.sidebar.markdown("---")

st.sidebar.subheader("Developer")

st.sidebar.write("Mohammad Zaid Khan")

# ---------------- MAIN PAGE ---------------- #

st.title("🎬 Movie Recommendation System")

st.write(
"""
Discover movies similar to your favourite movie using Machine Learning.
"""
)

movie_name = st.text_input(
    "Enter Movie Name",
    placeholder="Example: Avatar"
)

recommend = st.button("🔍 Recommend Movies")

# ---------------- RECOMMENDATION ---------------- #

if recommend:

    if movie_name.strip() == "":

        st.warning("Please enter a movie name.")

    else:

        list_of_titles = df["title"].tolist()

        close_matches = difflib.get_close_matches(
            movie_name,
            list_of_titles,
            n=1,
            cutoff=0.5
        )

        if len(close_matches) == 0:

            st.error("❌ Movie not found.")

        else:

            close_match = close_matches[0]

            movie_index = df[df["title"] == close_match]["index"].values[0]

            similarity_score = list(
                enumerate(similarity[movie_index])
            )

            sorted_movies = sorted(
                similarity_score,
                key=lambda x: x[1],
                reverse=True
            )

            st.success(f"Showing recommendations for **{close_match}**")

            st.markdown("---")

            count = 1

            for movie in sorted_movies:

                index = movie[0]

                score = movie[1]

                title = df[df["index"] == index]["title"].values[0]

                if count <= 10:

                    st.markdown(
                        f"""
                        <div class="movie-card">

                        <h3>{count}. {title}</h3>

                        <p class="similarity">
                        Similarity Score: {score:.2f}
                        </p>

                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                    count += 1

# ---------------- DATASET PREVIEW ---------------- #

with st.expander("📄 Preview Dataset"):

    st.dataframe(
        df[["title", "genres", "director"]].head(20),
        width="stretch"
    )

# ---------------- FOOTER ---------------- #

st.markdown("---")

st.markdown(
"""
<div class="footer">

Made with ❤️ using Streamlit

<br>

Movie Recommendation System

</div>
""",
unsafe_allow_html=True
)