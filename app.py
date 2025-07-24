from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'         # <-- CHANGE THIS
app.config['MYSQL_PASSWORD'] = '2@@5Rish' # <-- CHANGE THIS
app.config['MYSQL_DB'] = 'user'

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        pincode = request.form['pincode']
        district = request.form['district']
        zone = request.form['zone']
        password = request.form['password']
        password_hash = generate_password_hash(password)

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM user_info WHERE phone = %s', (phone,))
        account = cursor.fetchone()
        if account:
            flash('Account already exists with this phone number.', 'danger')
        else:
            cursor.execute('''
                INSERT INTO user_info (name, phone, email_id, password_hash, district, zone, pincode)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            ''', (name, phone, email, password_hash, district, zone, pincode))
            mysql.connection.commit()
            flash('You have successfully registered! Please login.', 'success')
            return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form['phone']
        password = request.form['password']

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM user_info WHERE phone = %s', (phone,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password_hash'], password):
            session['loggedin'] = True
            session['user_id'] = user['user_id']
            session['user_name'] = user['name']
            return redirect(url_for('dashboard'))
        else:
            flash('Incorrect phone or password.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'loggedin' in session:
        user_name = session['user_name']
        return render_template('dashboard.html', user_name=user_name)
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
