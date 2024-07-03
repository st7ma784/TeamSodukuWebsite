#This is a python file containing a flask app.
#the app is used to serve the frontend of this project.
#The main page is a login page, which allows users to log in and access their saved soduku puzzles
#the leaderboard also lets a new puzzle be started and offers a QR code to it.

import flask
import qrcode

#main function that runs the app.
def run(): #this is the main function of this file, which will start running the app.
    app = flask.Flask(__name__)
    return app

@app.route('/leaderboard', methods=['GET']) #this route serves up the leaderboard page for users to view their saved soduku puzzles that they have already solved.
def leaderboard(): #this function serves up the leaderboard page for users to view their saved soduku puzzles that they have already solved.
    #This function serves up the leaderboard page for users to view their saved soduku puzzles that they have already solved.

    return flask.render_template('pages/leaderboard.html') #this function serves up the leaderboard page for users to view their saved soduku puzzles that they have already solved.

#the app also has an admin page which allows admins to add new users or edit existing user profiles.
@app.route('/admin', methods=['GET']) #this route serves up the admin page for admins to add new users or edit existing user profiles.
def admin(): #this function serves up the admin page for admins to add new users or edit existing user profiles.
    return flask.render_template('pages/admin.html') #this function serves up the admin page for admins to add new users or edit existing user profiles.

#we need to dynamically have a sudoku puzzles based on the POST request data from users who are logged in to their accounts.
@app.route('/soduku', methods=['GET']) # the post includes a code to lookup soduku by
def soduku():
    #this function serves up the soduku page for users to view their saved sod
    #return the soduku page for users to view their saved sod
    return flask.render_template('pages/soduku.html') #this function serves up the soduku page for users to view their saved sod

@app.route('/api/generatepuzzle', methods=['POST'])
def generatepuzzle(name): #this function serves up the soduku and logs the code against the user.

    #make new sudoku and generate random code that is not in database 
    #enter name, starttime and code in database
    #enter code and sudoku in the database. 
    return code 
    
#create function for     fetch('/api/sudokuretrieve', { method:'POST', body:JSON.stringify({ "code": code })}).then(function(response){
@app.route('/api/sudokuretrieve', methods=['POST'])
def retrieve(code:str):
    #code is a string to the database to a puzzle state
    #lookup the database for a code:puzzle combination and return the puzzle
    puzzle=[-1]*81
    #lookup puzzle in database. 

    #return an jsonified array of the puzzle state
    return jsonify({ "code": code, "puzzle": puzzle }), 200 #this function serves up a soduku puzzle based on the POST request data from users who are logged in to their accounts.


if __name__ == '__main__': #This if statement checks to see whether or not the current python file being run is the main python file in the project. If it is, then this code will be executed and the frontend of this project will start running on your computer.
    app = run() #this variable stores a reference to the flask app that was just created by calling the function 'run' which we defined above. This allows us to use the variable 'app' as an argument in the function 'flask.Flask(__name__)
    if __package__ == None: #This if statement checks to see whether or not this current python file being run is a module that was imported into another python file using the 'import' keyword. If it is, then this code will be executed and the frontend of this project will start running on your computer.
        #serve up the webpage
        app.run(debug=True) #this function starts the flask app that was just created by calling the function 'run' which we defined above. This allows us to use the variable 'app' as an argument in the function 'flask.Flask(__name__)
