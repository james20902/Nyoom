from flask import Flask, render_template

nyoom = Flask(__name__)

@nyoom.route('/')
def home():
    return render_template('home.html')

@nyoom.route('/nyooming')
def connected():
    return render_template('chat.html')

if __name__ == '__main__':
    nyoom.run(debug=True)