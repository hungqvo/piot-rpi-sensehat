import csv
from datetime import datetime
import os

class csvHandler:
    # Symbolic initialization
    index_numer = 0

    # Get absolute file_name
    path = (__file__).split("writeToCsv.py")[0]
    file_name = path + "winner.csv"
    
    @classmethod
    def get_index_number(cls):
        # Get ordering number
        try:
            with open(cls.file_name, "r", encoding = "utf-8") as data_read:
                data = data_read.readlines()
            # Get index from the last line of csv
            lastRow = data[-1]
            index_number = int((lastRow.split(","))[0]) + 1
        
        # If file has not existed, index is 1
        except FileNotFoundError:
            index_number = 1

        return index_number

    @classmethod  
    def write_to_csv(cls, game_result):
        # Get the current time stamp
        now = datetime.now()
        time_stamp = now.strftime("%d/%m/%Y %H:%M:%S")
        
        index_number = cls.get_index_number()
        # Compile the message row
        row_contents = [index_number,game_result,time_stamp]
        
        # Append to the current file
        try:
            with open(cls.file_name, "a+", newline="") as writer_obj:
                csv_writer = csv.writer(writer_obj)
                csv_writer.writerow(row_contents)

        # If not created, create new file
        except FileNotFoundError:
            with open(cls.file_name, "w", newline="") as writer_obj:
                csv_writer = csv.writer(writer_obj)
                csv_writer.writerow(row_contents)

    