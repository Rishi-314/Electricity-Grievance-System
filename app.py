from flask import Flask, render_template, redirect, url_for, request, flash, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
from werkzeug.security import generate_password_hash, check_password_hash
# SELECT * FROM user_log;
app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key
import os
# MySQL configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'         # <-- CHANGE THIS
app.config['MYSQL_PASSWORD'] = '2@@5Rish' # <-- CHANGE THIS
app.config['MYSQL_DB'] = 'EGS'

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
        password = generate_password_hash(request.form['password'])
        address_line1 = request.form.get('address_line1', '')
        address_line2 = request.form.get('address_line2', '')
        city = request.form.get('city', '')
        pincode = request.form['pincode']
        division_id = request.form.get('division_id', None)

        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM Users WHERE phone = %s OR email = %s', (phone, email))
        account = cursor.fetchone()
        if account:
            flash('Account already exists with this phone or email.', 'danger')
        else:
            cursor.execute('''
                INSERT INTO Users (name, phone, email, password, address_line1, address_line2, city, pincode, division_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            ''', (name, phone, email, password, address_line1, address_line2, city, pincode, division_id))
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
        cursor.execute('SELECT * FROM Users WHERE phone = %s', (phone,))
        user = cursor.fetchone()
        if user and check_password_hash(user['password'], password):
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
        user_id = session['user_id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE user_id = %s', (user_id,))
        users = cursor.fetchone()
        user_name = users['name'] if users else session['user_name']
        return render_template('dashboard.html', user_name=user_name, user_info=users)
    else:
        return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'loggedin' in session:
        user_id = session['user_id']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE user_id = %s', (user_id,))
        users = cursor.fetchone()
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            address_line1 = request.form.get('address_line1', '')
            address_line2 = request.form.get('address_line2', '')
            city = request.form.get('city', '')
            pincode = request.form['pincode']
            division_id = request.form.get('division_id', None)
            cursor.execute('''
                UPDATE Users
                SET name = %s, email = %s, address_line1 = %s, address_line2 = %s, city = %s, pincode = %s, division_id = %s
                WHERE user_id = %s
            ''', (name, email, address_line1, address_line2, city, pincode, division_id, user_id))
            mysql.connection.commit()
            flash('Profile updated successfully!', 'success')
            session['user_name'] = name
            return redirect(url_for('dashboard'))
        return render_template('profile.html', user_info=users)
    else:
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/edit_profile', methods=['POST'])
def edit_profile():
    if 'loggedin' in session:
        user_id = session['user_id']
        name = request.form['name']
        email = request.form['email']
        pincode = request.form['pincode']
        district = request.form['district']
        zone = request.form['zone']
        # Phone is readonly, not updated

        cursor = mysql.connection.cursor()
        cursor.execute('''
            UPDATE Users
            SET name = %s, email_id = %s, pincode = %s, district = %s, zone = %s
            WHERE user_id = %s
        ''', (name, email, pincode, district, zone, user_id))
        mysql.connection.commit()
        flash('Profile updated successfully!', 'success')
        session['user_name'] = name
        return redirect(url_for('dashboard'))
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)