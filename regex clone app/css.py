import re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def results_function():
    if request.method == "POST":
        target_string = request.form['text']
        pattern = request.form['regex']
        count = 0
        result = []
        for match in re.finditer(r"{}".format(pattern),target_string):       
            string = ""
            count += 1
            string ="Match found : {} of text \"{}\", starting at index : {} and ending at index : {} ".format( count, match.group(), match.start(), match.end())
            result.append(string)
        return render_template('home.html', regex = pattern, text = target_string, count = count, result = result)

    return render_template('home.html', count = -1)

if __name__ == '__main__':
    app.run(debug=True)