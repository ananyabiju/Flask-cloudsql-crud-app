from flask import Flask, jsonify, request
from db import create, get


app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def welcome_note():
    return jsonify('Welcome to Flask app')

@app.route('/addEmployee', methods=['POST'])
def addEmployee():
    try:
        data = request.get_json()
        queryVal = 'INSERT INTO employees (name, email, position) VALUES(%s, %s, %s)', ({data['name']}, {data['email']}, {data['position']})
        create(queryVal)
        return jsonify({"msg": "Employee Added Successfully"}), 200
    except:
        return jsonify({"msg": "Error"}), 400



if __name__=='__main__':
    app.run()