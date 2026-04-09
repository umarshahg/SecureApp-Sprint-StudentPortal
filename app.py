from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"  # weak secret

# Fake database
users = {
    "student1": {"password": "123", "role": "student"},
    "admin": {"password": "admin", "role": "admin"}
}

results = {
    "1": {"name": "Ali", "marks": 85},
    "2": {"name": "Umar", "marks": 90}
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username in users and users[username]["password"] == password:
            session['user'] = username
            return redirect('/dashboard')
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    return render_template('dashboard.html', results=results)


# 🚨 IDOR VULNERABILITY
@app.route('/result/<id>')
def view_result(id):
    if 'user' not in session:
        return redirect('/')

    # ❌ No authorization check
    data = results.get(id)
    return render_template('result.html', data=data, id=id)


# 🚨 No CSRF Protection
@app.route('/edit/<id>', methods=['POST'])
def edit_result(id):
    new_marks = request.form['marks']
    results[id]['marks'] = new_marks
    return redirect('/dashboard')


if __name__ == '__main__':
    app.run(debug=True)
