from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

error_name = ""
error_pass = ""
error_pass2 = ""
error_email = ""

@app.route("/welcome", methods=['POST'])
def user_signup():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    local_name_error = False
    local_pass_error = False
    local_pass2_error = False
    local_email_error = False

    if username == "":
        local_name_error = True
    elif len(username) < 3:
        local_name_error = True
    elif len(username) >20:
        local_name_error = True
    elif " " in username:
        local_name_error = True
    else:
        local_name_error = False

    if password == "":
        local_pass_error = True
    elif len(password) < 3:
        local_pass_error = True
    elif len(password) >20:
        local_pass_error = True
    elif " " in password:
        local_pass_error = True
    else:
        local_pass_error = False

    if password != password2:
        local_pass2_error = True
    elif " " in password2:
        local_pass2_error = True
    else:
        local_pass2_error = False

    if "@" not in email:
        local_email_error = True
    elif "." not in email:
        local_email_error = True
    elif len(email) < 3:
        local_email_error = True
    elif len(email) > 20:
        local_email_error = True
    else:
        local_email_error = False

    if local_name_error == True:
        global error_name
        error_name = "That's not a valid username"
    else:
        error_name = ""

    if local_pass_error == True:
        global  error_pass
        error_pass = "That's not a valid password"
    else:
        error_pass = ""

    if local_pass2_error == True:
        global  error_pass2
        error_pass2 = "Passwords don't match"
    else: 
        error_pass2 = ""

    if local_email_error == True:
        global  error_email
        error_email = "That's not a valid email"
    else:
        error_email = ""
    
    if local_name_error == True:
        return redirect("/")
    elif local_pass_error == True:
        return redirect("/")
    elif local_pass2_error == True:
        return redirect("/")
    elif local_email_error == True:
        return redirect("/")

    return render_template('welcome.html', name = username)
    

@app.route("/", methods=['GET'])
def index():
    
    return render_template('base.html', name_error = error_name, pass_error = error_pass, pass2_error = error_pass2, email_error = error_email)

app.run()