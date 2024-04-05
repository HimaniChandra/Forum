from flask import Flask, redirect, render_template, jsonify,request, url_for


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/homepage')
def homepage():
    return render_template('frame-11.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/discuss')
def discuss():
    return render_template('frame-9.html')
@app.route("/announce")
def announce():
    return render_template("anouncements.html")

if __name__ == '__main__':
    app.run(debug=True)
