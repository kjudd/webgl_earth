from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('earth.html')

if __name__ == '__main__':
    app.run()
