import os.path
import os

from flask import Flask, redirect, url_for, request, jsonify, render_template
from os import path
from signal import signal, SIGINT
from sys import exit

app = Flask(__name__)

def handler(signal_received, frame):
    print('SIGINT detected. Exiting gracefully!')
    exit(0)

@app.errorhandler(400)
def bad_request(error):
    app.logger.error("Something is wrong")
    return render_template('400.html'), 400

@app.errorhandler(404)
def page_not_found(error):
    app.logger.error('Something is wrong')
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    app.logger.error("Something is wrong")
    return render_template('500.html'), 500

@app.errorhandler(501)
def implementation_error(error):
    app.logger.error("Something is wrong")
    return render_template('501.html'), 501

@app.route('/success/<name>')
def success(name):
    if path.isdir(name):
        arr = os.listdir(name)

        return jsonify(
            {
                "Folder name: ": name,
                "Files list: ": arr
            })
    else:
        return page_not_found(name)

@app.route('/login', methods = ['GET'])
def login():
    userInput = request.args.get('keyboard')

    return redirect(url_for('success', name = userInput))

if __name__ == '__main__':
    signal(SIGINT, handler)
    print('Running...Press CTRL-C to exit')
    while True:
        app.run()