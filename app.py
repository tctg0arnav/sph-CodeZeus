from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import PyPDF2
app = Flask(__name__) 

pdfFileObj = open('tut.pdf', 'rb') 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
pageObj = pdfReader.getPage(0) 
pdf_0 = pageObj.extractText()
lines = pdf_0.splitlines()
final = []
for i in lines:
    try:
    #if i starts with a digit then print line
        if i[0].isdigit():
            if i[1] == '.':
                final.append(i)
        elif len(final) != 0 and i[0].isalpha():
            final[-1] += ' ' + i
        elif i[0] == ' ':
            if i[1].isdigit():
                if i[2] == '.':
                    final.append(i)
            elif len(final) != 0 and i[1].isalpha():
                final[-1] += ' ' + i
        else:
            pass
    except:
        pass

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
@app.route('/questions/<int:index>')
def all_questions(index):
    questions = Ques.query.all()
    return questions[index].question

@app.route('/ques/')
def quest():
    return lines

@app.route('/ques/<int:index>')
def ques(index):
    try:
        return final[index] 
    except:
        return "No more questions"