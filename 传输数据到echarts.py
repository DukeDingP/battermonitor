from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def login():

    return render_template('echartsdynamic.html')

if __name__ == '__main__':

    app.run(debug=True)