from flask import Flask, jsonify, request
from db import create, getAllEmployee, updateEmployee


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
        db_result = getAllEmployee()
        return db_result
    except:
        return jsonify({"msg": "Listing employees failed"}), 400

# update an employee
@app.route('/update', methods=['PATCH'])
def updateEmployeee():
    try:
        data = request.get_json()
        updateEmployee(data["updateKey"], data)
        return jsonify({"msg": "Successfully Updated"}), 200
    except:
        return jsonify({"msg": "Update Failed"}), 400


if __name__=='__main__':
    app.run()