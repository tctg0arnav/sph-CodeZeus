from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    return render_template('login.html', username=username, password=password)

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    return render_template('register.html', username=username, password=password)

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/exam')
def exam():
    return render_template('exam.html')

@app.route('/practice')
def practice():
    return render_template('practice.html')

@app.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/proctor')
def proctor():
    return render_template('proctor.html')

@app.route('/analysis')
def analysis():
    return render_template('analysis.html')

