import pandas as pd
import numpy as np
import os

print(os.getcwd())

data_ratings = pd.read_csv('data_files/ratings.csv')
data_movies = pd.read_csv('data_files/movies.csv')

L = int(input())
N = int(input())

for _ in range(N):
    W, H = map(int, input().split())
    
    if W < L or H < L:
        print("UPLOAD ANOTHER")
    elif W == H:
        print("ACCEPTED")
    else:
        print("CROP IT")
