from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
 
app = Flask(__name__) 
"""The only required argument to the Flask class constructor is the name of the main
module or package of the application."""
 
@app.route('/') #Define your route
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return "Outra vez!  <a href='/logout'>Logout</a>"
 
@app.route('/login', methods=['POST'])
def do_admin_login():# Here we can check the password and login to access the index.html
    if request.form['password'] == 'password' and request.form['username'] == 'admin':
        session['logged_in'] = True
    else:
        flash('wrong password!') #If the wrong password is insert
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

 
if __name__ == "__main__":
    app.secret_key = os.urandom(12) #for create one secret key for your app
    app.run(debug=True,host='0.0.0.0', port=4000) #Define your debug, host and port
