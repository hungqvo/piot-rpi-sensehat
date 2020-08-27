
from databaseConnection import MySQLConn
import json
class Report:
#connect to the database
    mysqlconn = MySQLConn()
    mydb = mysqlconn.conn
    
    mycursor = mysqlconn.cursor
    def writeReport(self):
#get the list of the days in the database
        dayList = "Select distinct records.date from records"
        self.mycursor.execute(dayList)
        alldayResult = self.mycursor.fetchall()
#get the list of the bad days (contains uncomfortable record(s))
#the list contains the date and all the temperature that's out the comfortable range
        badday = "Select records.date, group_concat(records.temperature) from records where records.comfortable is false group by records.date"
        self.mycursor.execute(badday)
        baddayResult = self.mycursor.fetchall()

        diction = self.goodNBad(alldayResult,baddayResult)
        print(diction["goodDay"])
        print(diction["badDay"])
        file = open('report.csv','w')
        file.write("Date, Status \n")
        file.close()
#loof through all days
        for i in alldayResult:
        # if the day is in the badDay
            if i[0] in diction['badDay']:
                with open('config.json') as configFile:
                    data = json.load(configFile)
                #get the index of a day in allday by it's value
                index = diction['badDay'].index(i[0])
# take the first one among the bad records of that day (baddayResult[index][1][0]) 
# to write to the csv file
                tuple_temp = self.turn_string_to_tuple(baddayResult[index][1])
                for j in tuple_temp:
                    if j <data['cold_max']:
                        file_object = open('report.csv', 'a')
                        diff = data['cold_max']-j
                        file_object.write(i[0]+" BAD: "+str(diff)+ " C degree below the comfort temperature\n")
                        file_object.close()
                        break
                    if j > data['hot_min']:
                        diff = j-data['hot_min']
                        file_object = open('report.csv', 'a')
                        file_object.write(i[0]+" BAD: "+str(diff)+ "C degree above the comfort temperature\n")
                        file_object.close()
                        break
# if the day is good day, just write OK
            if i[0] in diction['goodDay']:
                file_object = open('report.csv', 'a')
                file_object.write(i[0]+" OK \n")
                file_object.close()
# create the dictionary contain list of bad and goodDay distinctionally 
# from all day and bad day
    def goodNBad(self,allday, badday):
        d = dict()
        goodDay=[]
        listContentBadDayOnly=[]
        for i in badday:
            listContentBadDayOnly.append(i[0])
        for j in allday:
            if j[0] not in listContentBadDayOnly:
                goodDay.append(j[0])
        d['goodDay'] = goodDay
        d['badDay'] = listContentBadDayOnly
        return d
    
    def turn_string_to_tuple(self,string):
        return tuple(map(int, string.split(','))) 

report = Report()
report.writeReport()