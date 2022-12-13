import os
import pymysql
pymysql.install_as_MySQLdb()


def connect_tcp_socket():
    db_host = os.environ.get("INSTANCE_HOST")  # e.g. '127.0.0.1'
    db_user = os.environ.get("DB_USER")  # e.g. 'my-db-user'
    db_pass = os.environ.get("DB_PASS")  # e.g. 'my-db-password'
    db_name = os.environ.get("DB_NAME")  # e.g. 'my-database'
    db_port = os.environ.get("DB_PORT")  # e.g. 3306
    return f'mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'