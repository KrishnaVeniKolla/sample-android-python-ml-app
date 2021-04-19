from model import *
from flask import Flask, redirect, url_for,jsonify, request,render_template
movie_titles = pd.read_csv("Movie_Id_Titles.csv")
def rcmd(m):
    if m not in movie_titles['title'].unique():
        return 'no'
        #return('This movie is not in our database.\nPlease check if you spelled it correct.')
    else:
        # check if data and sim are already assigned
        try:
            data.head()
            sim.shape
        except:
            data, sim =create_sim(m)
            l=list(sim.index.values)
            return l[1:]
            #return l[1:]
app = Flask(__name__)
@app.route("/")
def home():
    return render_template('home.html')

#@app.route("/recommend",methods=['POST','GET'])
@app.route('/recommend',methods=['POST','GET'])
def recommend():
    movie = request.args.get('movie')
    movie=str(movie)
    print(movie)
    r = rcmd(movie)
    print(r)
    movie = movie.upper()
    if type(r)==type('string'):
        return {"message":"No"}
        #return render_template('recommend.html',movie=movie,r=r,t='s')
    else:
        #return render_template('recommend.html',movie=movie,r=r,t='l')
        return {"message":"Yes"}
    '''if r==0:
        return {"message":"No"}
    else:
        return {"message":"yes"}'''



if __name__ == '__main__':
    app.run()
