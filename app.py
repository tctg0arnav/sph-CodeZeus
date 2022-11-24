from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return "render_template('index.html')"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_post():
    email = request.form['email']
    password = request.form['password']
    if email == 'iam@teacher.com' and password == 'teacher':
        return 'Welcome to teacher dashboard'
    elif email == 'iam@student.com' and password == 'student':
        return 'Welcome to student dashboard'
    else:
        return 'Incorrect username or password.'