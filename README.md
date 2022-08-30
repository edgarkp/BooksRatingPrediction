# Implementation of book's rating prediction model
This project contains implementation of a machine learning-based model used to predict books ratings. The implementation is preceeded by a dataset preparation, thorough Explanatory Data Analysis (EDA) and feature selection.

### The dataset

![](readme-images/goodreads.PNG)

The dataset provided is a curation of Goodreads books based on real user information. It is contained in a csv file called *books.csv* and gives the following book's attributes:
1) *bookID:* A unique identification number for each book.
2) *title:* The name under which the book was published.
3) *authors:* The names of the authors of the book. Multiple authors are delimited by
“/”.
4) *average_rating:* The average rating of the book received in total.
5) *isbn:* Another unique number to identify the book, known as the International
Standard Book Number.
6) *isbn13:* A 13-digit ISBN to identify the book, instead of the standard 11-digit ISBN.
7) *language_code:* Indicates the primary language of the book. For instance, “eng” is
standard for English.
8) *num_pages:* The number of pages the book contains.
9) *ratings_count:* The total number of ratings the book received.
10) *text_reviews_count:* The total number of written text reviews the book received.
11) *publication_date:* The date the book was published.
12) *publisher:* The name of the book publisher.

The genre was added as the 13th attribute and obtained from one of google's API. 

**NB:** It is possible through the variable *choice* to either fetch the genre from the API or directly load the results from the csv file I saved under the name *genres.csv*. I suggest you to take the 2nd option. Otherwise, it would take a much longer time to run all the notebook.

### Feature Selection
It is mainly based on what I obtain from my EDA and the dependencies + correlations found between the target variables and the features.

### Machine Learning Model
I propose two approaches to the machine learning:
* A regression approach that allows to predict an average rating
* A classification approach that allows to predict if a book will have good ratings (average rating between 3 and 4 stars) or high ratings (average rating above 4 stars)

### To run the project
* Create an environment from the requirements.txt file 
* Run the notebook *Books rating prediction*

### Closing
Feel free to comment and add any constructive critics that could help me better my solution :) 



