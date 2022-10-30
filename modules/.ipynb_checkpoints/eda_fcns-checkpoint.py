{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7edcd75",
   "metadata": {},
   "outputs": [],
   "source": [
    "def ratings_to_appreciation(ratings):\n",
    "    if ratings < 3 :\n",
    "        return 'poor rating'\n",
    "    elif ratings < 4 :\n",
    "        return 'good rating'\n",
    "    else : \n",
    "        return 'high rating'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3758b0b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a function to get the year of the publication date\n",
    "def getyear(publication_date):\n",
    "    return int(publication_date.rpartition('/')[2])"
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
