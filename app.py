#!/usr/bin/python 

from flask import * 

app = Flask(__name__) 

@app.route('/')
def home(): 
	return render_template('index.html')

@app.route('/login')
def login():
	return render_template('login2.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0', debug=True)
