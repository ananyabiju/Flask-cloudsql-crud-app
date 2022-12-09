import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


# CONNECTION EXECUTION WITH CLOUD-SQL
def open_connection():
    unix_socket = f'/cloudsql/{db_connection_name}'
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                password=db_password,
                unix_socket=unix_socket,
                db=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )

    except pymysql.MySQLError as e:
        return e
    return conn

# CREATE
def create(data):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO Employees (name, email, position) VALUES(%s, %s, %s)',
         ({data['name']}, {data['email']}, {data['position']}))
    conn.commit()
    conn.close()

# READ
def read():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Employees;')
        result = cursor.fetchall()
        if len(result) > 0:
            return jsonify({"data": result}), 200
        else:
            return "Oops! No data available"

# READ AN EMPLOYEE
def get_employee():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('SELECT * FROM Employees WHERE email= "anu@gmail.com"')
        result = cursor.fetchone()
        # if len(result) > 0:
        return jsonify({"data": result}), 200
        # else:
        #     return "Oops..! No employee found"


# UPDATE
def update_operation(data):
    conn = open_connection()
    with conn.cursor() as cursor:
            cursor.execute('DELETE from Employees WHERE email=%s', (data["email"]))
            cursor.execute('INSERT INTO Employees (name, email, position) VALUES(%s, %s, %s)',
         ({data['name']}, {data['email']}, {data['position']}))
    conn.commit()
    conn.close()

# DELETE
def delete(data):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('DELETE FROM Employees WHERE email= %s', (data))
    conn.commit()
    conn.close()
