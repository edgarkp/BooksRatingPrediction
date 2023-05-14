import joblib
import streamlit as st
import csv
import sklearn 
import os

project_path = os.getcwd()
data_output_path = project_path+"/data/outputs"
model_path = project_path+"/src"
    
# Import the created functions
from modules.eda_fcns import get_num_occ_genre, is_top_genre, get_num_occ_authors, get_num_occ_title

# Import the necessary data for preprocessing 
list_genres = []
list_authors = []
list_top_genre = []
list_titles = []


#with open('.\data\outputs\list_genres.csv', encoding='utf-8', newline='') as inputfile:
with open(data_output_path+'/list_genres.csv', encoding='utf-8', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_genres.append(row[0])

#with open('.\data\outputs\list_authors.csv', encoding='utf-8', newline='') as inputfile:
with open(data_output_path+'/list_authors.csv', encoding='utf-8', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_authors.append(row[0])

#with open('.\data\outputs\list_top_genre.csv', encoding='utf-8', newline='') as inputfile:
with open(data_output_path+'/list_top_genre.csv', encoding='utf-8', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_top_genre.append(row[0])

#with open('.\data\outputs\list_titles.csv', encoding='utf-8', newline='') as inputfile:
with open(data_output_path+'/list_titles.csv', encoding='utf-8', newline='') as inputfile:
    for row in csv.reader(inputfile):
        list_titles.append(row[0])
        
model = joblib.load(model_path +'/model.bin') # run the model as a pipeline

# GUI interface
def web_app():
    st.write("""
    # Books rating application
    ## This app predicts the ratings of a book 
    """)
    st.header("User details")
    st.subheader("Enter the following inputs related to your book")
    title = st.text_input("Title")
    genre = st.text_input("Genre")
    names_authors = st.text_input("Name of the authors (separated the author by a /)")
    publication_year = st.number_input("Publication year",0,None)
    num_pages = st.number_input("Number of pages",0,None)
    
    # Preprocessing
    num_occ_genre = get_num_occ_genre(genre, list_genres)
    num_occ_authors = get_num_occ_authors(names_authors, list_authors)
    top_genre = is_top_genre(genre, list_top_genre)
    num_occ_title = get_num_occ_title(title, list_titles)
    
    X = [num_pages, num_occ_title, num_occ_authors,num_occ_genre, publication_year, top_genre]
    
    # Run the app when the button is pressed
    if st.button("Press here to make Prediction"):
        # Run the model
        result = model.predict([X])
    
        # Print the result
        st.text_area(label='The predicted rating is : ', value=round(result[0],2), height= 100)
        
run = web_app()