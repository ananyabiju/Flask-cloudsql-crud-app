from flask import Flask, jsonify, request
from db import create, read, update


app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def welcome_note():
    return jsonify('Welcome to Flask app')

# adding employees
@app.route('/create', methods=['POST'])
def createEmployee():
    try:
        data = request.get_json()
        create(data)
        return jsonify({"msg": "Employee Added Successfully"}), 200
    except:
        return jsonify({"msg": "Employee Creation Failed.. User Already Exists"}), 400

# getting all employees
@app.route('/read/<email>', methods=['GET'])
def readEmployee():
    try:
        qs = request.view_args['email']
        # db_result = read(qs)
        lengthOfQ = len(qs)
        return jsonify(qs), 200
    except:
        return jsonify({"msg": "Listing employees failed"}), 400

# update an employee
@app.route('/update', methods=['PUT'])
def updateEmployeee():
    try:
        data = request.get_json()
        update(data)
        return jsonify({"msg": "Successfully Updated"}), 200
    except:
        return jsonify({"msg": "Update Failed"}), 400

# @app.route('/delete', methods=['DELETE'])
# def deleteEmployee():
#     try:
#     except:
#         return jsonify({"msg": "Employee deletion failed"}), 400

if __name__=='__main__':
    app.run()