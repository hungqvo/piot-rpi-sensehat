import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request
import math

@app.route('/get', methods=['GET'])
def get_newest():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
    # select the newest records
        cursor.execute("Select * from records order by records.time Desc limit 1")
        recordRow = cursor.fetchone()
        respone = jsonify(recordRow)
        respone.status_code = 200
        cursor.close()
        conn.close()
        return respone
    except Exception as e:
        print(e)
	    
@app.route('/upload', methods=['POST'])
def upload_new():
    try:
        _json = request.json
    # check if the request body is correct
        if 'humidity' in _json and 'temperature' in _json and 'comfortable' in _json and 'date' in _json and request.method == 'POST':
            _temperature = _json['temperature']
            _humidity = _json['humidity']
            _comfortable = _json['comfortable']
            _date = _json['date']
            query = "Insert into records(date, temperature, humidity, comfortable) values(%s ,%s ,%s ,%s)"
            bindData = (_date, _temperature, _humidity, _comfortable)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(query, bindData)
            conn.commit()
            cursor.close()
            conn.close()
            response = jsonify('Record has been added successfully')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)

@app.route('/update', methods =['PUT'])
def update_newest():
    try:
        _json = request.json
        if 'temperature' in _json and 'humidity' in _json and 'comfortable' in _json and request.method =='PUT':
            query = "Update records set temperature=%s, humidity=%s, comfortable=%s Order by records.time Desc Limit 1 "
            _temperature = _json['temperature']
            _humidity = _json['humidity']
            _comfortable = _json['comfortable']
            bindData = ( _temperature, _humidity, _comfortable)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(query, bindData)
            conn.commit()
            cursor.close()
            conn.close()
            response = jsonify('Record has been updated successfully')
            response.status_code = 200
            return response
        else:
            return not_found()
    except Exception as e:
        print(e)
            
@app.errorhandler(404)
# handling the error that makes the incorrect request
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
app.run()