from flask import Flask

app = Flask(__name__)

###########################################

@app.route('/')
def index():
    return "Welcome to this Application!"

@app.route('/about')
def about_us():
    return "This is About us page"

###########################################

if __name__ == '__main__' :
    app.run(debug=True)         # whatever changes you make it will reflect on your applications 