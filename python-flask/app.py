import pickle

from flask import Flask, redirect, url_for,jsonify, request,render_template
model = pickle.load(open('model.pkl', 'rb'))
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
