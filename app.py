from flask import Flask, render_template, request, redirect, session
from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "supersecretkey123"

# Enable CSRF
csrf = CSRFProtect(app)

# Fake database
users = {
    "student1":  {"password": "pass1",  "role": "student"},
    "student2":  {"password": "pass2",  "role": "student"},
    "student3":  {"password": "pass3",  "role": "student"},
    "student4":  {"password": "pass4",  "role": "student"},
    "student5":  {"password": "pass5",  "role": "student"},
    "student6":  {"password": "pass6",  "role": "student"},
    "student7":  {"password": "pass7",  "role": "student"},
    "student8":  {"password": "pass8",  "role": "student"},
    "student9":  {"password": "pass9",  "role": "student"},
    "student10": {"password": "pass10", "role": "student"},
    "student11": {"password": "pass11", "role": "student"},
    "student12": {"password": "pass12", "role": "student"},
    "student13": {"password": "pass13", "role": "student"},
    "student14": {"password": "pass14", "role": "student"},
    "student15": {"password": "pass15", "role": "student"},
    "student16": {"password": "pass16", "role": "student"},
    "student17": {"password": "pass17", "role": "student"},
    "student18": {"password": "pass18", "role": "student"},
    "student19": {"password": "pass19", "role": "student"},
    "student20": {"password": "pass20", "role": "student"},
    "admin":     {"password": "admin",  "role": "admin"},
}

# Results: each student has 5 courses
results = {
    "1":  {"name": "Ali",    "courses": {"Math": 85, "Physics": 78, "Chemistry": 90, "English": 88, "CS": 92}},
    "2":  {"name": "Umar",   "courses": {"Math": 90, "Physics": 82, "Chemistry": 75, "English": 95, "CS": 88}},
    "3":  {"name": "Sara",   "courses": {"Math": 72, "Physics": 68, "Chemistry": 80, "English": 74, "CS": 85}},
    "4":  {"name": "Zara",   "courses": {"Math": 88, "Physics": 91, "Chemistry": 84, "English": 79, "CS": 93}},
    "5":  {"name": "Ahmed",  "courses": {"Math": 60, "Physics": 55, "Chemistry": 70, "English": 65, "CS": 58}},
    "6":  {"name": "Fatima", "courses": {"Math": 95, "Physics": 89, "Chemistry": 92, "English": 97, "CS": 94}},
    "7":  {"name": "Hassan", "courses": {"Math": 77, "Physics": 80, "Chemistry": 73, "English": 81, "CS": 76}},
    "8":  {"name": "Ayesha", "courses": {"Math": 83, "Physics": 76, "Chemistry": 88, "English": 90, "CS": 82}},
    "9":  {"name": "Bilal",  "courses": {"Math": 69, "Physics": 72, "Chemistry": 65, "English": 70, "CS": 74}},
    "10": {"name": "Hina",   "courses": {"Math": 91, "Physics": 94, "Chemistry": 89, "English": 86, "CS": 90}},
    "11": {"name": "Kamran", "courses": {"Math": 74, "Physics": 70, "Chemistry": 77, "English": 68, "CS": 72}},
    "12": {"name": "Nadia",  "courses": {"Math": 86, "Physics": 83, "Chemistry": 81, "English": 92, "CS": 87}},
    "13": {"name": "Omar",   "courses": {"Math": 58, "Physics": 62, "Chemistry": 55, "English": 60, "CS": 63}},
    "14": {"name": "Sana",   "courses": {"Math": 93, "Physics": 88, "Chemistry": 95, "English": 91, "CS": 96}},
    "15": {"name": "Tariq",  "courses": {"Math": 67, "Physics": 71, "Chemistry": 64, "English": 73, "CS": 69}},
    "16": {"name": "Amna",   "courses": {"Math": 80, "Physics": 85, "Chemistry": 78, "English": 83, "CS": 81}},
    "17": {"name": "Rizwan", "courses": {"Math": 75, "Physics": 69, "Chemistry": 82, "English": 76, "CS": 78}},
    "18": {"name": "Madiha", "courses": {"Math": 89, "Physics": 92, "Chemistry": 86, "English": 94, "CS": 91}},
    "19": {"name": "Faisal", "courses": {"Math": 63, "Physics": 67, "Chemistry": 61, "English": 66, "CS": 70}},
    "20": {"name": "Rabia",  "courses": {"Math": 97, "Physics": 95, "Chemistry": 98, "English": 96, "CS": 99}},
}

# Map each student to their result ID
user_result_map = {
    "student1":  "1",  "student2":  "2",  "student3":  "3",  "student4":  "4",
    "student5":  "5",  "student6":  "6",  "student7":  "7",  "student8":  "8",
    "student9":  "9",  "student10": "10", "student11": "11", "student12": "12",
    "student13": "13", "student14": "14", "student15": "15", "student16": "16",
    "student17": "17", "student18": "18", "student19": "19", "student20": "20",
    "admin": "all",
}

# Form
class EditForm(FlaskForm):
    marks = StringField('Marks', validators=[DataRequired()])
    submit = SubmitField('Update')

@app.route('/', methods=['GET', 'POST'])
@csrf.exempt
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username]["password"] == password:
            session['user'] = username
            return redirect('/dashboard')
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', results=results, user=session['user'], user_result_map=user_result_map)

@app.route('/result/<id>', methods=['GET', 'POST'])
def view_result(id):
    if 'user' not in session:
        return redirect('/')
    username = session['user']

    # IDOR FIX
    if username != "admin" and user_result_map.get(username) != id:
        return "Unauthorized Access", 403

    form = EditForm()

    # Only admin can edit
    if form.validate_on_submit():
        if username != "admin":
            return "Unauthorized Action", 403
        course, mark = form.marks.data.split(":")
        results[id]['courses'][course.strip()] = int(mark.strip())
        return redirect('/dashboard')

    return render_template('result.html', data=results[id], form=form, user=username)

@app.after_request
def security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
    return response

if __name__ == '__main__':
    app.run(debug=True , port=5001)
