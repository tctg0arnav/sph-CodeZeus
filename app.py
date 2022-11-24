from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 

# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
question = ""
answer = ""
# Database model
class Ques(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(80), nullable=False)
    topic = db.Column(db.String(80), nullable=False)
    question = db.Column(db.String(200), nullable=False)
    answer = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Ques %r>' % self.id

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

#display all questions
@app.route(f'/questions/<int:index>')
def all_questions(index):
    questions = Ques.query.all()
    return questions[index].question