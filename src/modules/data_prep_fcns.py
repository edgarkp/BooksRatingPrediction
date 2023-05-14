# Create a function that will get the genre by isbn
def get_genre_by_isbn(isbn: str) : 
    
    import numpy as np
    import requests
    
    resp = np.nan #initialize the response
    api = "https://www.googleapis.com/books/v1/volumes?q=isbn:"
    isbn = isbn.strip() # remove unnecessary white spaces

    try:
        resp = requests.get(api + isbn) # send a request and get a JSON response
        resp.raise_for_status()
    except requests.exceptions.Timeout as err_to:
        print('The url is taking too much to respond') # Maybe set up for a retry, or continue in a retry loop
    except requests.exceptions.TooManyRedirects as err_tmd:
        print('Too many redirects. The url is not good enough') # Tell the user their URL was bad and try a different one 
    except requests.exceptions.HTTPError as err_http: 
        print(err_http) # error on the 404 on the http 
        raise SystemExit(err_http)
    
    if resp == np.nan : # Check if the response is still nan
        return resp
    else:
        info_book = resp.json() # parse JSON response into a Python dictionary      
        if 'items' in  info_book :
            volumeInfo = info_book['items'][0]['volumeInfo'] 
            if 'categories' in volumeInfo :
                return volumeInfo['categories'][0]
            else : return np.nan
        else : return np.nan
 
 
# Create a function that will transform the vector containing the isbn into multiple batches
def create_batch(vec, num_batch_el) : 

    num_batch = int(np.ceil(len(vec)/num_batch_el))

    batch = []
    vec_batch = [0]*num_batch

    for i in range(num_batch) : 

        for j in range(num_batch_el) :
            index = num_batch_el * i + j
            if index < len(vec):
                batch.append(vec[index]) 
        vec_batch[i] = batch  
        batch = []

    return vec_batch

