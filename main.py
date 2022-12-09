from flask import Flask, jsonify, request
from db import create, read, update_operation, delete, create_sql_table
from flask_cors import CORS


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/welcome', methods=['GET'])
def welcome_note():
    return jsonify('Welcome to Flask app')

# --------------ADDING EMPLOYEES---------------#
@app.route('/create', methods=['POST'])
def createEmployee():
    try:
        data = request.get_json()
        create(data)
        return jsonify({"msg": "Employee Added Successfully"}), 200
    except Exception as e:
        return jsonify({"msg": "Employee Creation Failed.. User Already Exists", "error": e}), 400

# ---------------GET ALL EMPLOYEES-------------#
@app.route('/list', methods=['GET'])
def readEmployee():
    try:
        return read()
    except Exception as e:
        return jsonify({"msg": "Listing employees failed", "error": e}), 400

# # --------------GET A PARTICULAR EMPLOYEE-------------#
# @app.route('/read/<email>', methods=['GET'])
# def readEmployee(email):
#     try:
#         return get_employee(email)
#     except Exception as e:
#         return jsonify({"msg": "Listing employees failed", "error": e}), 400

# ---------------UPDATE AN EMPLOYEE-------------------#
@app.route('/update', methods=['PUT'])
def updateEmployeee():
    try:
        data = request.get_json()
        update_operation(data)
        return jsonify({"msg": "Successfully Updated"}), 200
    except Exception as e:
        return jsonify({"msg": "Update Failed", "error": e}), 400

# ---------------DELETE AN EMPLOYEE--------------#
@app.route('/delete/<email>', methods=['DELETE'])
def deleteEmployee(email):
    try:
        delete(email)
        return jsonify({'msg': "Successfully deleted the employee"}), 200
    except Exception as e:
        return jsonify({"msg": "Employee deletion failed", "error": e}), 400

@app.route('/create_table/<TableName>')
def createTable(TableName):
    try:
        create_sql_table(TableName)
        return jsonify({'msg': "Successfully deleted the employee"}), 200
    except Exception as e:
        return jsonify({"msg": "Employee deletion failed", "error": e}), 400



if __name__=='__main__':
    app.run()