import numpy as np
import pandas as pd
from flask import Flask, render_template, request
import pickle
# libraries for making count matrix and similarity matrix

# define a function that creates similarity matrix
# if it doesn't exist
movie_titles = pd.read_csv("Movie_Id_Titles.csv")
def create_sim(movie):
    try:
        column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        df = pd.read_csv('user.csv', names=column_names)
        df = pd.merge(df,movie_titles,on='item_id')
        df.groupby('title')['rating'].mean().sort_values(ascending=False).head()
        df.groupby('title')['rating'].count().sort_values(ascending=False).head()
        ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
        ratings['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
        moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
        user_ratings = moviemat[movie]
        corr=pd.DataFrame(moviemat.corrwith(user_ratings),columns=['Correlation'])
        corr.dropna(inplace=True)
        corr.sort_values('Correlation',ascending=False)
        corr=corr.join(ratings['num of ratings'])
        sim=corr[corr['num of ratings']>100].sort_values('Correlation',ascending=False).head(10)
        sim.drop(['Correlation'],axis=1,inplace=True)
        sim['num of ratings'] = pd.DataFrame(df.groupby('title')['rating'].count())
        sim['ratings']=pd.DataFrame(df.groupby('title')['rating'].mean())
        return movie_titles,sim
    except:
        return

'''# defining a function that recommends 10 most similar movies
def rcmd(m):
    if m not in movie_titles['title'].unique():
        return('This movie is not in our database.\nPlease check if you spelled it correct.')
    else:
        # check if data and sim are already assigned
        try:
            data.head()
            sim.shape
        except:
            data, sim = create_sim(m)
            l=list(sim.index.values)
            s='\n'.join(l[1:])
            return s
'''
