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

@app.route('/user/<user_name>')
def user_profile(user_name):
    return "Welcome {}!".format(user_name)

###########################################

if __name__ == '__main__' :
    app.run(debug=True)