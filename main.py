from flask import Flask, jsonify, request
from db import create, read, update_operation
# , get_employee, update, delete, table_create, get_employee


app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def welcome_note():
    return jsonify('Welcome to Flask app')


# ADDING EMPLOYEES
@app.route('/create', methods=['POST'])
def createEmployee():
    try:
        data = request.get_json()
        create(data)
        return jsonify({"msg": "Employee Added Successfully"}), 200
    except:
        return jsonify({"msg": "Employee Creation Failed.. User Already Exists"}), 400

# getting all employees
@app.route('/list', methods=['GET'])
def readEmployee():
    try:
        return read()
    except:
        return jsonify({"msg": "Listing employees failed"}), 400

# # get an employee
# @app.route('/read', methods=['GET'])
# def readEmployee():
#     try:
#         # data = request.args.get('email')
#         return get_employee()
#     except:
#         return jsonify({"msg": "Listing employees failed"}), 400


# update an employee
@app.route('/update', methods=['PUT'])
def updateEmployeee():
    try:
        data = request.get_json()
        update_operation(data)
        return jsonify({"msg": "Successfully Updated"}), 200
    except:
        return jsonify({"msg": "Update Failed"}), 400

# # delete an employee
# @app.route('/delete', methods=['DELETE'])
# def deleteEmployee():
#     try:
#         data = request.args.get('email')
#         delete(data)
#         return jsonify({'msg': "Successfully deleted the employee"}), 200
#     except:
#         return jsonify({"msg": "Employee deletion failed"}), 400



if __name__=='__main__':
    app.run()