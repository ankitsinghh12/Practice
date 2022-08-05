from flask import Flask, render_template

app = Flask(__name__)

##########################################

@app.route('/')
def fun_1():
    return render_template("index.html")

@app.route('/', method=['POST'])
def fun_2():
    return "POST REQUEST PAGE"


###########################################

if __name__ == '__main__' :
    app.run(debug=True)
