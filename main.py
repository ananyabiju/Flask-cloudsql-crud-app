from flask import Flask, jsonify, request


app = Flask(__name__)


@app.route('/welcome', methods=['GET'])
def welcome_note():
    return jsonify('Welcome to Flask app')

if __name__=='__main__':
    app.run()