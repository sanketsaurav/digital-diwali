from flask import Flask, redirect, render_template
import re

app = Flask(__name__)

NAME_REGEX = r'[a-zA-Z0-9-]+'

@app.route('/')
def homepage():
	return render_template('index.html')

@app.route('/<sender>/<receiver>')
def greeting(sender, receiver):
	
	# sanitize, accept only first name
	sender = sender.split('-')[0]
	receiver = receiver.split('-')[0]

	# check if name is fishy
	if not (re.match(NAME_REGEX, sender) and re.match(NAME_REGEX, receiver)):
		return redirect('/')
	
	return render_template('index.html', sender=sender.upper(), receiver=receiver.upper())

@app.route('/<path:dummy>')
def dummy(dummy):
	return redirect('/')

if __name__ == '__main__':
	app.run(debug=True)