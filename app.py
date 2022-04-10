import json
import os.path
import os
import re

from flask import Flask, redirect, url_for, request, jsonify
from os import path

app = Flask(__name__)

@app.route('/success/<name>/<filtr>')
def success(name, filtr):
    print(filtr)
    arr = os.listdir(name)
    #r = re.compile(filtr)
    #filtered_list = list(filter(r.match, arr))

    return jsonify(
        {
            "Folder name: ":name,
            "Files list: ":arr
        })

@app.route('/login', methods = ['GET'])
def login():
    userInput = request.args.get('keyboard')
    print(userInput)
    userInput2 = request.args.get('regex')
    return redirect(url_for('success', name = userInput, filtr = userInput2))

if __name__ == '__main__':
   app.run()