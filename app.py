from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world1():
    return render_template('wheel1.html')

@app.route('/wheel')
def hello_world():
    return render_template('wheel.html')

if __name__ == '__main__':
    app.run()
