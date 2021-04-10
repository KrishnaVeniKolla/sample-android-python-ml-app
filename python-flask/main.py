import numpy as np
import pandas as pd
from flask import Flask, render_template, request
# libraries for making count matrix and similarity matrix

# define a function that creates similarity matrix
# if it doesn't exist
movie_titles = pd.read_csv("Movie_Id_Titles")
def create_sim(movie):
    try:
        column_names = ['user_id', 'item_id', 'rating', 'timestamp']
        df = pd.read_csv('u.data', sep='\t', names=column_names)
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
        '''data = pd.read_csv('data.csv')
        # creating a count matrix
        cv = CountVectorizer()
        count_matrix = cv.fit_transform(data['comb'])
        # creating a similarity score matrix
        sim = cosine_similarity(count_matrix)
        return data,sim'''
    except:
        return

# defining a function that recommends 10 most similar movies
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

    
    # check if the movie is in our database or not
    
   
        ''' # getting the index of the movie in the dataframe
        i = data.loc[data['movie_title']==m].index[0]

        # fetching the row containing similarity scores of the movie
        # from similarity matrix and enumerate it
        lst = list(enumerate(sim[i]))

        # sorting this list in decreasing order based on the similarity score
        lst = sorted(lst, key = lambda x:x[1] ,reverse=True)

        # taking top 1- movie scores
        # not taking the first index since it is the same movie
        lst = lst[1:11]'''
        
        
        '''l = []
        for i in range(len(lst)):
            a = lst[i][0]
            l.append(data['movie_title'][a])
        return l'''
        # making an empty list that will containg all 10 movie recommendations

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/recommend",methods=['POST','GET'])
def recommend():
    movie = request.json('movie')
    
    r = rcmd(movie)
    movie = movie.upper()
    if type(r)==type('string'):
        return {"message":"Yes"}
        #return render_template('recommend.html',movie=movie,r=r,t='s')
    else:
        #return render_template('recommend.html',movie=movie,r=r,t='l')
        return {"message":"No"}



if __name__ == '__main__':
    app.run()
