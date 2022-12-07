from flask import Flask, jsonify, request
from db import create, get


app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def welcome_note():
    return jsonify('Welcome to Flask app')

# adding employees
@app.route('/addEmployee', methods=['POST'])
def addEmployee():
    try:
        data = request.get_json()
        create(data)
        return jsonify({"msg": "Employee Added Successfully"}), 200
    except:
        return jsonify({"msg": "Error"}), 400


# getting all employees
@app.route('/list', methods=['GET'])
def getAllEmployees():
    try:
        query = 'SELECT * FROM employees;'
        db_result = get(query)
        return jsonify({"body": db_result, "msg": "Successfully listed"}), 200
    except:
        return jsonify({"msg": "Listing employees failed"}), 400


if __name__=='__main__':
    app.run()