#!/usr/bin/env python
# coding: utf-8

# Classify numerical values of ratings
def ratings_to_appreciation(ratings):
    if ratings < 3 :
        return 'poor rating'
    elif ratings < 4 :
        return 'good rating'
    else : 
        return 'high rating'

# Get the year of the publication date in a numerical format
def getyear(publication_date):
    return int(publication_date.rpartition('/')[2])

# Get the number of occurence of its genre and its position in the top genre (according to our actual DB)
def get_num_occ_genre(genre, list_genres):
    return list_genres.count(genre)
    
def is_top_genre(genre, list_top_genre):
    if genre in list_top_genre :
        return 1
    else :
        return 0
    
# Get the number of occurence of the authors
def get_num_occ_authors(authors, list_authors):
    num_occ_authors = 0;
    selected_authors = authors.split('/');
    for author in selected_authors :
        num_occ_authors += list_authors.count(author)
    return num_occ_authors

# Get the number of occurence of the title
def get_num_occ_title(title, list_titles):
    return list_titles.count(title)