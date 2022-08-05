from flask import Flask, render_template, request

app = Flask(__name__)

##########################################

@app.route('/' , mathods= ['GET', 'POST'])
def fun_1():
    if request.method == 'POST':
        email = request.form['in_1']
        return "Welcome {}".format(email)

    return render_template("index.html")

@app.route('/search', methods = ['GET'])
def search_function():
    return "Welcone to the Search page"
###########################################

if __name__ == '__main__' :
    app.run(debug=True)