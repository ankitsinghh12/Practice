# Code for only those users who are there in the list

from flask import Flask

app = Flask(__name__)

users = ['dhruv-dixit','azhaku',]

###########################################

@app.route('/')
def index():
    return "Welcome to this Application!"

@app.route('/about')
def about_us():
    return "This is About us page"

# Code for only those users who are there in the list

@app.route('/user/<user_name>')
def user_profile(user_name):
    return "Welcome {}!".format(user_name)
    if user_name in users:
        return "Welcome {}!".format(user_name)

    return "Please Register."

###########################################

if __name__ == '__main__' :
    app.run(debug=True)