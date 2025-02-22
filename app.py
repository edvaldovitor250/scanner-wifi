from flask import Flask, render_template, request, redirect, url_for, session, flash
from scanner.network_scanner import NetworkScanner
from functools import wraps

app = Flask(__name__)
app.secret_key = "n3Q,0157}<-"

USERNAME = "admin"
PASSWORD = "1234"

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('logged_in'):
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        pwd = request.form.get('password')
        if user == USERNAME and pwd == PASSWORD:
            session['logged_in'] = True
            return redirect(url_for('index'))
        else:
            flash("Credenciais inválidas. Tente novamente.")
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/', methods=['GET', 'POST'])
@login_required
def index():
    results = []
    if request.method == 'POST':
        network_range = request.form.get('network_range')
        scanner = NetworkScanner(network_range)
        scanner.scan()
        results = scanner.process_results()
    return render_template('index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
