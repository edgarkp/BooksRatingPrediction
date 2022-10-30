{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5d8da0c9",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function that will get the genre by isbn\n",
    "def get_genre_by_isbn(isbn: str) : \n",
    "    \n",
    "    resp = np.nan #initialize the response\n",
    "    api = \"https://www.googleapis.com/books/v1/volumes?q=isbn:\"\n",
    "    isbn = isbn.strip() # remove unnecessary white spaces\n",
    "\n",
    "    try:\n",
    "        resp = requests.get(api + isbn) # send a request and get a JSON response\n",
    "        resp.raise_for_status()\n",
    "    except requests.exceptions.Timeout as err_to:\n",
    "        print('The url is taking too much to respond') # Maybe set up for a retry, or continue in a retry loop\n",
    "    except requests.exceptions.TooManyRedirects as err_tmd:\n",
    "        print('Too many redirects. The url is not good enough') # Tell the user their URL was bad and try a different one \n",
    "    except requests.exceptions.HTTPError as err_http: \n",
    "        print(err_http) # error on the 404 on the http \n",
    "        raise SystemExit(err_http)\n",
    "    \n",
    "    if resp == np.nan : # Check if the response is still nan\n",
    "        return resp\n",
    "    else:\n",
    "        info_book = resp.json() # parse JSON response into a Python dictionary      \n",
    "        if 'items' in  info_book :\n",
    "            volumeInfo = info_book['items'][0]['volumeInfo'] \n",
    "            if 'categories' in volumeInfo :\n",
    "                return volumeInfo['categories'][0]\n",
    "            else : return np.nan\n",
    "        else : return np.nan"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7f291814",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function that will transform the vector containing the isbn into multiple batches\n",
    "def create_batch(vec, num_batch_el) : \n",
    "\n",
    "    num_batch = int(np.ceil(len(vec)/num_batch_el))\n",
    "\n",
    "    batch = []\n",
    "    vec_batch = [0]*num_batch\n",
    "\n",
    "    for i in range(num_batch) : \n",
    "\n",
    "        for j in range(num_batch_el) :\n",
    "            index = num_batch_el * i + j\n",
    "            if index < len(vec):\n",
    "                batch.append(vec[index]) \n",
    "        vec_batch[i] = batch  \n",
    "        batch = []\n",
    "           \n",
    "    \n",
    "    return vec_batch"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
