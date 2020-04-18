from flask import Flask, render_template, request
from client import Client

connection = Client
nyoom = Flask(__name__)


@nyoom.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if connection.validate(connection, request.form['ipbox'], int(request.form['portbox'])):
            return connected()
        else:
            print('oh no')
    return render_template('home.html')


@nyoom.route('/nyooming', methods=['GET', 'POST'])
def connected():
    if request.method == 'POST':
        connection.send_message(request.form['inputbox'])
    # if request.method == 'GET':
    #     print('temp')
        #update textbox
    return render_template('chat.html')


if __name__ == '__main__':
    nyoom.run(debug=True)
