import mysql.connector
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv(verbose=True)
env_path = os.getcwd()
load_dotenv(dotenv_path= env_path + '/.env')
class MySQLConn:
    conn = mysql.connector.connect(
    host= os.getenv("HOST"), 
    user= os.getenv("USERR"),
    password= os.getenv("PASSWORD") ,
    database= os.getenv("DATABASE"),
    port= os.getenv("PORT")
    )
  
    cursor = conn.cursor()
