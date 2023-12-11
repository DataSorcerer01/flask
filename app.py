from flask import Flask,render_template,request,redirect,url_for,session
import os

app=Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template("home.html",logged_in=session.get('logged_in'))

@app.route('/index')
def index():
    return render_template("index.html",logged_in=session.get('logged_in'))

@app.route('/signup' , methods=['GET','POST'])
def signup():
    if request.method=='POST':
        return redirect(url_for('index'))
    return render_template("signup.html",logged_in=session.get('logged_in'))

@app.route('/login' , methods=['GET','POST'])
def login():
    if request.method=='POST':
        username=request.form['username']
        if username:
            session['logged_in']=True
            return redirect(url_for('index.html'))
    return render_template("login.html",logged_in=session.get('logged_in'))

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('logout'))


if __name__ == '__main__':
    app.run(debug=True)