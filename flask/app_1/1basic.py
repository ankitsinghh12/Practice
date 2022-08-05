#step 1 - import 
from flask import Flask

#step 2 - Create the object
app = Flask(__name__)

#Step 3 - Define the Routes and bind it with functions
@app.route('/')
def index():
    return "Welcome to this Application!"

#Step 4 - Run the app
if __name__ == '__main__' :
    app.run()