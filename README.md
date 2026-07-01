# 🎬 Movie Recommendation System

A **Content-Based Movie Recommendation System** built with **Python, Scikit-learn, and Streamlit** that recommends movies similar to a user's favorite movie using **TF-IDF Vectorization** and **Cosine Similarity**.

---

## 📌 Project Overview

This application recommends movies based on their content rather than user ratings. It analyzes movie attributes such as genres, keywords, cast, director, and tagline to find similar movies.

If the user enters a movie name with a spelling mistake (for example, **"Avatr"**), the system automatically finds the closest matching title and displays relevant recommendations.

---

## 🚀 Features

* 🎬 Content-Based Movie Recommendation
* 🔍 Automatic Movie Name Correction
* 📊 TF-IDF Vectorization
* 🤖 Cosine Similarity Matching
* ⚡ Fast Recommendation using Precomputed Similarity Matrix
* 🌐 Interactive Web Application using Streamlit
* 🎨 Clean and Responsive User Interface
* 📄 Dataset Preview

---

## 🛠️ Technologies Used

* Python
* Streamlit
* Pandas
* Scikit-learn
* NumPy
* Joblib

---

## 📂 Dataset

This project uses the **TMDB 5000 Movies Dataset**.

The dataset contains information such as:

* Movie Title
* Genres
* Keywords
* Cast
* Director
* Tagline
* Popularity
* Ratings

---

## 🧠 Machine Learning Workflow

1. Load the movie dataset.
2. Fill missing values in important features.
3. Combine textual features:

   * Genres
   * Keywords
   * Tagline
   * Cast
   * Director
4. Convert text into numerical vectors using **TF-IDF Vectorization**.
5. Compute similarity between movies using **Cosine Similarity**.
6. Save the trained artifacts (`movies_df.pkl`, `similarity.pkl`, `tfidf_vectorizer.pkl`) using Joblib.
7. Build a Streamlit web application that loads the saved files and provides movie recommendations.

---

## 📁 Project Structure

```text
Movie-Recommendation-System/
│
├── app.py
├── movies_df.pkl
├── similarity.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md

```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Movie-Recommendation-System.git
```

```bash
cd Movie-Recommendation-System
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## 📈 Example

**Input**

```text
Avatar
```

**Closest Match**

```text
Avatar
```

**Recommended Movies**

* Avatar
* Alien
* Aliens
* Guardians of the Galaxy
* Star Trek Beyond
* Star Trek Into Darkness
* Galaxy Quest
* Alien³
* Cargo
* Gravity

---

## 📊 Machine Learning Concepts Used

* Content-Based Filtering
* Natural Language Processing (NLP)
* TF-IDF (Term Frequency–Inverse Document Frequency)
* Cosine Similarity
* Feature Engineering
* Text Vectorization

---

## 📌 Future Improvements

* Add movie posters using the TMDB API
* Display ratings, genres, and release year
* Show movie overview
* Add trailer links
* Filter recommendations by genre
* Deploy on Streamlit Community Cloud
* Improve UI with animations and cards
* Add fuzzy search suggestions

---

##
