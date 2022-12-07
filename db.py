import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')


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


def get(query):
    conn = open_connection()
    with conn.cursor() as cursor:
        queryData = cursor.execute(query)
        result = cursor.fetchall()
        if(queryData > 0):
            return jsonify(result)
        else:
            return "Oops! No data available"


def create(data):
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('INSERT INTO employees (name, email, position) VALUES(%s, %s, %s)',
         ({data['name']}, {data['email']}, {data['position']}))
    conn.commit()
    conn.close()