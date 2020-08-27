#!/usr/bin/python3
import requests
import json
import os
from datetime import datetime
from sense_hat import SenseHat
from dotenv import load_dotenv
from pathlib import Path
from databaseConnection import MySQLConn
from senseHatCalibration import Calibration

class Monitor:
  sense = SenseHat()
  #get the accurate temperature from Calibration class
  cali = Calibration()
  real_temp = cali.get_accurate_temp()
  humidity = cali.getHumidity()
  #connect to the mySQL database
  mysqlconn = MySQLConn()
  mydb = mysqlconn.conn
  #get the current date time
  now = datetime.now()
  #formating the date (month:day:year)
  time = now.strftime("%m/%d/%Y") 
  mycursor = mysqlconn.cursor
  #def __init__(self, temperature, humidity):
  #  self.temperature = temperature
  #  self.humidity = humidity
    

  def saveToDatabase(self):
   #if the temperature and the humidity are in the comfortable range, save to the data base with true value in comfortable column 
    if self.comfortableHumidityRange()["comfortable"] and self.comfortableTemperatureRange()["comfortable"]:
      sql = "INSERT INTO records (date,temperature, humidity, comfortable) VALUES (%s,%s,%s,true)"
      val = (self.time,self.real_temp, self.humidity)
    else:
      sql = "INSERT INTO records (date,temperature, humidity, comfortable) VALUES (%s,%s,%s,false)"
      val = (self.time, self.real_temp, self.humidity) 
    self.mycursor.execute(sql,val)
    self.mydb.commit()
# check if the temperature is in the comfortable range, 
# if no return false and the value details in a turple of dictionary
# otherwise just return True 
  def comfortableTemperatureRange(self):
    with open('config.json') as configFile:
      data = json.load(configFile)
    if self.real_temp < data['cold_max']:
      return {"comfortable": False,"detail":"below "+str(data['cold_max']-self.real_temp)}
    if self.real_temp > data['hot_min']:
      return {"comfortable": False,"detail":"above"+str(self.real_temp-data['hot_min'])}
    else:
      return {"comfortable": True}
# same with temperature    
  def comfortableHumidityRange(self):
    with open('config.json') as configFile:
      data = json.load(configFile)
    if self.humidity< data['humidity_min']:
      return {"comfortable": False,"detail":"below "+str(data['humidity_min']-self.humidity)}
    if self.humidity>data['humidity_max']:
      return {"comfortable": False,"detail":"above"+str(self.humidity- data['humidity_max'])}
    else:
      return{"comfortable": True}
# the flow is first save to the database
# so if the count of uncomfortable is 1 means has not notified yet
# it will return false
  def notified(self):
    sql = """SELECT count(comfortable) FROM records WHERE records.comfortable is false and records.date = %(date)s"""
    value= {'date':self.time}
    self.mycursor.execute(sql,value)
    result = self.mycursor.fetchone()
    if result[0] == 1:
      return False
    if result[0] == 0 or result[0] >1:
      return True
# check if the end of the day with no uncomfortable value recorded
  def end_of_the_day(self):
    if self.now.hour == 23 and self.now.minute == 59 and self.now.second >= 0 and self.now.second <= 59 and self.notified():
      return True
    else:
      return False
# setup the post request to the push bullet with the content variable  
  def postRequest(self,content):
    url = "https://api.pushbullet.com/v2/pushes"
    header = {'Content-Type': 'application/json','access-token': os.getenv("ACCESS_TOKEN")}
    data = {"body":content,"title": "Temperature and Humidity monitoring","type":"note"}
    res = requests.post(url, headers = header , json = data)
    print(res.text)
# if the end of the day and everything is all good, it will notify the avarage of temperature and humidity in whole day
# whenever the temperature and the humidity reach out the comfortable range, notify immediately
# with the value details but only if there are no notification before(self.notified())
  def pushNotify(self):
    if self.end_of_the_day():
      sql = "Select AVG(records.temperature), AVG(records.humidity) from records"
      self.mycursor.execute(sql)
      result = self.mycursor.fetchone()
      self.postRequest("The Temperature and humidity are in the comfortable range with " + result[0] + " Celsius Degree and " + result[1] + "percent in avarage")  
    elif not self.comfortableTemperatureRange()["comfortable"] and not self.notified():
      self.postRequest("The Temperature is " +self.comfortableTemperatureRange()["detail"] + " of the comfortable range")
    elif not self.comfortableHumidityRange()["comfortable"] and not self.notified():
      self.postRequest("The Humidity is " + self.comfortableHumidityRange()["detail"] + " of the comfortable range")
    

#declare the class then save to the database then call the pushNotify() 
monitor = Monitor()
monitor.saveToDatabase()
monitor.pushNotify()
