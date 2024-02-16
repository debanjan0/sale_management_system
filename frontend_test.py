
from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		print(username, password)
		if username=="test" and password=="test":
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
	return redirect(url_for('login'))






if __name__ == '__main__':
    app.run(debug=True)







