import io
import os
import requests
import csv
import json
import datetime
import logging
class log_weather:
    #parms={'dataType':'CLMTEMP', 'station':'HPV', 'rformat':'csv', 'year':'2020'}
    def __init__(self, loc_temp, loc_rain,url,params,dologging):
        self.loc_temp=loc_temp
        self.loc_rain=loc_rain
        self.url=url
        self.params=params
        self.dologging=dologging
        curtime=datetime.datetime.now()
        #date_target={'year': curtime.year, 'month': curtime.month, 'day': curtime.day}
        self.datelog=curtime.strftime("%Y_%m_%d")
        self.timelog=curtime.strftime("%H:%M:%S")
        self.header="Time_logged, Temperature at "+loc_temp+", Rainfall at "+loc_rain+'\n' 
        logs_folder='~/logs_weather/'
        logs_folder=os.path.expanduser(logs_folder)
        if not os.path.isdir(logs_folder):
            os.mkdir(logs_folder)
        self.pathtofile=logs_folder+self.datelog
        self.pathtolog=logs_folder+"debug_log"
        if self.dologging:
            logging.basicConfig(filename=self.pathtolog, level=logging.DEBUG)
#, encoding='utf-8'
        if not os.path.isfile(self.pathtofile):
            with open(self.pathtofile,'w') as f:
                f.write(self.header)

    def get_response(self, url, parms):
        response=requests.get(url, params=parms)
        if response.ok:
            data=response.text
        else:
            raise "Invalid response obtained"
        return response.text
    def log_data(self):
        data=self.get_response(self.url, self.params)
        data_f=json.loads(data)
        temperature_data=data_f["temperature"]["data"]
        rainfall_data=data_f["rainfall"]["data"]
        #print(temperature_data)
        #print(rainfall_data)
        templog=None
        rainlog=None
        for d in temperature_data:
            if d["place"]==self.loc_temp:
                templog=d["value"]
        for d in rainfall_data:
            if d["place"]==self.loc_rain:
                rainlog=d["max"]
        if templog==None:
            if self.dologging:
                logging.info(self.datelog+"::"+self.timelog+"::  Temperature value for "+self.loc_temp+" doesn't exist. Please try another location")
            templog=0
        if rainlog==None:
            if self.dologging:
                logging.info(self.datelog+"::"+self.timelog+"::  Rainfall value for "+self.loc_rain+" doesn't exist. Please try another location")
            rainlog=0
       # print(rainlog)
       # print(templog)
        #print(json.dumps(data_f, indent=4, sort_keys=True))
#        f=io.StringIO(data)
#        found=False
#        prev_row=[]
#        row=[]
#        for row in csv.reader(f):
#            if row[0]==str(self.date_target['year']):
#                found=True
#            elif found==True:
#                temp_found=float(prev_row[3])
#                date_found={'year': int(prev_row[0]), 'month':int(prev_row[1]), 'day':int(prev_row[2])}
#                break
#            prev_row=row
#        if date_found!=self.date_target:
#            print("Warning! data for target date not found, most recent date is", date_found)
#        else:
#            print("Found data for the day we were looking for")
        with open(self.pathtofile, 'a') as f:
            strtowrite=self.timelog+','+str(templog)+','+str(rainlog)+'\n'
            print(strtowrite)
            f.write(strtowrite)
