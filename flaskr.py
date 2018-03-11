from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/goals')
def goals():
    return render_template('goals.html')

@app.route('/account')
def account():
    return render_template('account.html')

@app.route('/login2')
def login():
    return render_template('login2.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
