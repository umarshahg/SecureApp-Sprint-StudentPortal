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
    "student1": {"password": "123", "role": "student"},
    "admin": {"password": "admin", "role": "admin"}
}

results = {
    "1": {"name": "Ali", "marks": 85},
    "2": {"name": "Umar", "marks": 90}
}

user_result_map = {
    "student1": "1",
    "admin": "all"
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
    return render_template('dashboard.html', results=results, user=session['user'])


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

        results[id]['marks'] = form.marks.data
        return redirect('/dashboard')



    return render_template('result.html', data=results[id], form=form)


@app.after_request
def security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
    return response


if __name__ == '__main__':
    app.run(debug=True)
