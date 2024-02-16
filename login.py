import flask 

app = flask.Flask(__name__)

@app.route('/')
def log_in_page():
    
    return flask.render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
