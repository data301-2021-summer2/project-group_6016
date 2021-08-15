{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a82b5b8f-b126-45a5-9392-e44d09513d0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(path_to_csv):\n",
    "    def1 = (\n",
    "    pd.read_csv('day.csv')\n",
    "    .dropna(axis=0)\n",
    "    .rest_index(drop=True)\n",
    "    .drop(columns = ['yr', 'season', 'mnth', 'weekday', 'weathersit', 'atemp'])\n",
    "    )"
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
   "version": "3.8.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
