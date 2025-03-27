from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Dummy user credentials
USER_CREDENTIALS = {"username": "testuser", "password": "password123"}

# Home page redirects to login
@app.route("/")
def home():
    return redirect(url_for('login'))

# Login page
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == USER_CREDENTIALS["username"] and password == USER_CREDENTIALS["password"]:
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials", "error")
    return render_template("login.html")

# Dashboard page with navigation
@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

# Data entry form page
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # For simplicity, just echo the submitted data
        data = request.form.get("data")
        flash(f"Form submitted with: {data}", "success")
        return redirect(url_for('dashboard'))
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)