#this is the flask app as backend for the sudoku app

#here we manage the leaderboard, a table of user, start time,end time and code
#we also manage the puzzle states, a table of code, and puzzle. 

import flask
#do import for database
from flask_sqlalchemy import sqalchemy
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.postgresql import ARRAY

from sqlalchemy.orm import DeclarativeBase

db = sqalchemy()
app=flask.Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)
#make table leaderboard 
class LeaderBoard(db.Model):  #here we manage the leaderboard, a table of user, start time,end time and code
    __tablename__="leaderBoard"
    user=db.Column(db.String)
    endTime=db.Column(db.DateTime)
    startTime=db.Column(db.DateTime)
    code=db.Column(db.String)
#make table PuzzleStates
class PuzzleStates(db.Model):  #here we manage the puzzle states, a table of code, and puzzle.
    __tablename_="puzzleStates"
    code=db.Column(db.String)
    #puzzle is a column of 81 digits in the puzzle state table.
    puzzle=db.Column(db.ARRAY(db.Integer))

@app.route("/leaderboard",methods=["GET"])
def get_leaderboard():  #this is the function that gets called when a get request to /leaderboard comes in from the front end app. #here we manage the leaderboard, a table of user, start time,end time and code
    #get the local db connection and return top 10 ordered by shortest time to endtime-startime
    leaderboard=db.session.query(leaderboard).order_by(db.func.abs(leaderboard.endtime-leaderboard.starttime))[:10]  #here we manage the leaderboard, a table of user, start time,end time and code
    return flask.jsonify(leaderboard)

if __name__=="__main__":  #here we manage the leaderboard, a table of user, start time,end time and code
    



















if __name__=="__main__":    
    print("Backend Running")
    app.run()