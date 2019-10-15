from flask import Flask, render_template
from flask import Flask, render_template, redirect, url_for, request,flash, session


app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/minigame')
def index():
    return render_template('index.html')

@app.route('/level2')
def level2():
    return render_template('level2.html')
@app.route('/secret')
def secret_level():
    pass

@app.route('/final')
def final():
    return render_template('final_challenge.html')

@app.route('/prize')
def prize():
    return render_template('pr1z3.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['password'] != 'followyourdream':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('wrong password')
            return redirect(url_for('prize'))
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
