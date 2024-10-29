Book Recommendation System-
This repository contains a Book Recommendation System developed using Machine Learning and Collaborative Filtering techniques. It leverages a trained model to recommend books based on user preferences and uses Streamlit to provide a user-friendly web interface for generating recommendations.

Project Overview
The primary goal of this project is to create a recommendation engine that suggests books to users based on their reading history. The model uses collaborative filtering, a popular approach in recommendation systems that makes predictions about a user's interests by collecting preferences from many users.

Key Features
Collaborative Filtering: Utilizes user-item interactions to recommend books with similar characteristics.
Streamlit Web Application: A simple and interactive interface where users can input a book title and receive personalized recommendations.
Setup Instructions
Clone the Repository:
git clone https://github.com/Advitiyyaaa/Book-recommender-system.git
cd Book-recommender-system

Create a Virtual Environment:
conda create --prefix ./env python=3.7 -y
conda activate ./env

Install Required Packages:
pip install -r requirements.txt

Run the Streamlit App:
streamlit run app.py

Navigate to Localhost: Open http://localhost:8501 in your browser to interact with the application.

Project Structure
Artifacts/: Directory containing pre-trained model and data files for recommendations.
app.py: Main Streamlit application code.
requirements.txt: Lists dependencies needed to run the application.
README.md: Project documentation.
Usage
Select or type the name of a book in the search box.
Click "Show Similar Books" to see recommended books based on the selected title.
View each recommended book with its cover image, providing an intuitive preview.
Technical Details
Collaborative Filtering: Used to predict books similar to the user’s past selections.
K-Nearest Neighbors: Implements collaborative filtering by finding similar books based on user ratings.
Data Storage: Preprocessed data and models are saved in the Artifacts directory and loaded at runtime.
Streamlit: Provides an interactive web interface for an easy-to-use experience.
Future Enhancements
Content-Based Filtering: Incorporate book metadata (genres, author, etc.) to enhance recommendation quality.
Hybrid Model: Combine collaborative and content-based filtering for improved accuracy.
License
This project is open-source and available under the MIT License.
