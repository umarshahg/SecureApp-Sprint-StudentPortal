from flask import Flask, render_template, request, redirect, session
from flask_wtf import CSRFProtect, FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import sqlite3
import os
 
app = Flask(__name__)
app.secret_key = "supersecretkey123"
 
# Enable CSRF
csrf = CSRFProtect(app)
 
DB_PATH = "portal.db"
 
# ── DATABASE INIT ─────────────────────────────────────────────────────────────
def get_db():
    """Open a database connection."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row   # allows dict-style access
    return conn
 
def init_db():
    """Create tables and seed data — only runs if DB doesn't exist yet."""
    if os.path.exists(DB_PATH):
        return  # already initialised — never overwrite existing data
 
    conn = get_db()
    c = conn.cursor()
 
    # ── USERS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role     TEXT NOT NULL
        )
    ''')
 
    # ── STUDENTS TABLE (result records)
    c.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id   INTEGER PRIMARY KEY,
            name TEXT NOT NULL
        )
    ''')
 
    # ── MARKS TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS marks (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            student_id INTEGER NOT NULL,
            course     TEXT NOT NULL,
            mark       INTEGER NOT NULL,
            FOREIGN KEY (student_id) REFERENCES students(id)
        )
    ''')
 
    # ── USER → RESULT MAPPING TABLE
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_result_map (
            username   TEXT PRIMARY KEY,
            student_id INTEGER,
            FOREIGN KEY (username) REFERENCES users(username)
        )
    ''')
 
    # ── SEED USERS
    seed_users = [
        ("student1",  "pass1",  "student"),
        ("student2",  "pass2",  "student"),
        ("student3",  "pass3",  "student"),
        ("student4",  "pass4",  "student"),
        ("student5",  "pass5",  "student"),
        ("student6",  "pass6",  "student"),
        ("student7",  "pass7",  "student"),
        ("student8",  "pass8",  "student"),
        ("student9",  "pass9",  "student"),
        ("student10", "pass10", "student"),
        ("student11", "pass11", "student"),
        ("student12", "pass12", "student"),
        ("student13", "pass13", "student"),
        ("student14", "pass14", "student"),
        ("student15", "pass15", "student"),
        ("student16", "pass16", "student"),
        ("student17", "pass17", "student"),
        ("student18", "pass18", "student"),
        ("student19", "pass19", "student"),
        ("student20", "pass20", "student"),
        ("admin",     "admin",  "admin"),
    ]
    c.executemany("INSERT INTO users VALUES (?,?,?)", seed_users)
 
    # ── SEED STUDENTS & MARKS
    seed_students = [
        (1,  "Ali"),    (2,  "Umar"),   (3,  "Sara"),   (4,  "Zara"),
        (5,  "Ahmed"),  (6,  "Fatima"), (7,  "Hassan"), (8,  "Ayesha"),
        (9,  "Bilal"),  (10, "Hina"),   (11, "Kamran"), (12, "Nadia"),
        (13, "Omar"),   (14, "Sana"),   (15, "Tariq"),  (16, "Amna"),
        (17, "Rizwan"), (18, "Madiha"), (19, "Faisal"), (20, "Rabia"),
    ]
    c.executemany("INSERT INTO students VALUES (?,?)", seed_students)
 
    seed_marks = [
        (1,  "Math", 85),  (1,  "Physics", 78),  (1,  "Chemistry", 90),  (1,  "English", 88),  (1,  "CS", 92),
        (2,  "Math", 90),  (2,  "Physics", 82),  (2,  "Chemistry", 75),  (2,  "English", 95),  (2,  "CS", 88),
        (3,  "Math", 72),  (3,  "Physics", 68),  (3,  "Chemistry", 80),  (3,  "English", 74),  (3,  "CS", 85),
        (4,  "Math", 88),  (4,  "Physics", 91),  (4,  "Chemistry", 84),  (4,  "English", 79),  (4,  "CS", 93),
        (5,  "Math", 60),  (5,  "Physics", 55),  (5,  "Chemistry", 70),  (5,  "English", 65),  (5,  "CS", 58),
        (6,  "Math", 95),  (6,  "Physics", 89),  (6,  "Chemistry", 92),  (6,  "English", 97),  (6,  "CS", 94),
        (7,  "Math", 77),  (7,  "Physics", 80),  (7,  "Chemistry", 73),  (7,  "English", 81),  (7,  "CS", 76),
        (8,  "Math", 83),  (8,  "Physics", 76),  (8,  "Chemistry", 88),  (8,  "English", 90),  (8,  "CS", 82),
        (9,  "Math", 69),  (9,  "Physics", 72),  (9,  "Chemistry", 65),  (9,  "English", 70),  (9,  "CS", 74),
        (10, "Math", 91),  (10, "Physics", 94),  (10, "Chemistry", 89),  (10, "English", 86),  (10, "CS", 90),
        (11, "Math", 74),  (11, "Physics", 70),  (11, "Chemistry", 77),  (11, "English", 68),  (11, "CS", 72),
        (12, "Math", 86),  (12, "Physics", 83),  (12, "Chemistry", 81),  (12, "English", 92),  (12, "CS", 87),
        (13, "Math", 58),  (13, "Physics", 62),  (13, "Chemistry", 55),  (13, "English", 60),  (13, "CS", 63),
        (14, "Math", 93),  (14, "Physics", 88),  (14, "Chemistry", 95),  (14, "English", 91),  (14, "CS", 96),
        (15, "Math", 67),  (15, "Physics", 71),  (15, "Chemistry", 64),  (15, "English", 73),  (15, "CS", 69),
        (16, "Math", 80),  (16, "Physics", 85),  (16, "Chemistry", 78),  (16, "English", 83),  (16, "CS", 81),
        (17, "Math", 75),  (17, "Physics", 69),  (17, "Chemistry", 82),  (17, "English", 76),  (17, "CS", 78),
        (18, "Math", 89),  (18, "Physics", 92),  (18, "Chemistry", 86),  (18, "English", 94),  (18, "CS", 91),
        (19, "Math", 63),  (19, "Physics", 67),  (19, "Chemistry", 61),  (19, "English", 66),  (19, "CS", 70),
        (20, "Math", 97),  (20, "Physics", 95),  (20, "Chemistry", 98),  (20, "English", 96),  (20, "CS", 99),
    ]
    c.executemany(
        "INSERT INTO marks (student_id, course, mark) VALUES (?,?,?)", seed_marks
    )
 
    # ── SEED USER → RESULT MAP
    seed_map = [(f"student{i}", i) for i in range(1, 21)] + [("admin", None)]
    c.executemany("INSERT INTO user_result_map VALUES (?,?)", seed_map)
 
    conn.commit()
    conn.close()
    print("[DB] Database initialised and seeded.")
 
 
# ── HELPER: fetch all results (for dashboard) ─────────────────────────────────
def get_all_results():
    conn = get_db()
    c = conn.cursor()
    students = c.execute("SELECT id, name FROM students ORDER BY id").fetchall()
    all_results = {}
    for s in students:
        sid = str(s["id"])
        courses_rows = c.execute(
            "SELECT course, mark FROM marks WHERE student_id = ?", (s["id"],)
        ).fetchall()
        courses = {row["course"]: row["mark"] for row in courses_rows}
        all_results[sid] = {"name": s["name"], "courses": courses}
    conn.close()
    return all_results
 
 
# ── HELPER: fetch one student's result ───────────────────────────────────────
def get_result(student_id):
    conn = get_db()
    c = conn.cursor()
    student = c.execute(
        "SELECT id, name FROM students WHERE id = ?", (student_id,)
    ).fetchone()
    if not student:
        conn.close()
        return None
    courses_rows = c.execute(
        "SELECT course, mark FROM marks WHERE student_id = ?", (student_id,)
    ).fetchall()
    courses = {row["course"]: row["mark"] for row in courses_rows}
    conn.close()
    return {"name": student["name"], "courses": courses}
 
 
# ── HELPER: update a mark in DB ───────────────────────────────────────────────
def update_mark(student_id, course, mark):
    conn = get_db()
    c = conn.cursor()
    c.execute(
        "UPDATE marks SET mark = ? WHERE student_id = ? AND course = ?",
        (mark, student_id, course)
    )
    conn.commit()
    conn.close()
 
 
# ── HELPER: get student_id for a username ────────────────────────────────────
def get_student_id(username):
    conn = get_db()
    c = conn.cursor()
    row = c.execute(
        "SELECT student_id FROM user_result_map WHERE username = ?", (username,)
    ).fetchone()
    conn.close()
    return str(row["student_id"]) if row and row["student_id"] else None
 
 
# ── FORM ──────────────────────────────────────────────────────────────────────
class EditForm(FlaskForm):
    marks  = StringField('Marks', validators=[DataRequired()])
    submit = SubmitField('Update')
 
 
# ── ROUTES ───────────────────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
@csrf.exempt
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE username = ? AND password = ?",
            (username, password)
        ).fetchone()
        conn.close()
        if user:
            session['user'] = username
            return redirect('/dashboard')
        else:
            error = "Invalid Credentials"
    return render_template('login.html', error=error)
 
 
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')
    results = get_all_results()
    # build user_result_map for template compatibility
    user_result_map = {f"student{i}": str(i) for i in range(1, 21)}
    user_result_map["admin"] = "all"
    return render_template(
        'dashboard.html',
        results=results,
        user=session['user'],
        user_result_map=user_result_map
    )
 
 
@app.route('/result/<id>', methods=['GET', 'POST'])
def view_result(id):
    if 'user' not in session:
        return redirect('/')
    username = session['user']
 
    # IDOR FIX — students can only see their own result
    if username != "admin" and get_student_id(username) != id:
        return "Unauthorized Access", 403
 
    data = get_result(int(id))
    if not data:
        return "Result not found", 404
 
    form = EditForm()
 
    if form.validate_on_submit():
        if username != "admin":
            return "Unauthorized Action", 403
        try:
            course, mark = form.marks.data.split(":")
            update_mark(int(id), course.strip(), int(mark.strip()))
        except ValueError:
            return "Invalid format. Use  CourseName: Mark", 400
        return redirect('/dashboard')
 
    return render_template('result.html', data=data, form=form, user=username)
 
 
@app.after_request
def security_headers(response):
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['Content-Security-Policy'] = "frame-ancestors 'none'"
    return response
 
 
# ── ENTRY POINT ───────────────────────────────────────────────────────────────
if __name__ == '__main__':
    init_db()   # safe — skips if DB already exists
    app.run(debug=True, port=5001)
