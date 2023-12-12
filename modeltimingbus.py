#DONE BY LOW XUAN JIE
import datetime


class Timingbus:
    def __init__(self, userid, timingbus, busno, busstopno):
        str_timingbusid = str(datetime.datetime.now().timestamp()) # to generate timingbusid using timestamp
        self.__timingbusid = str_timingbusid   # timingbus id is used as key for shelve
        self.__userid = userid
        self.__timingbus = timingbus #bus stop no.
        self.__busno = busno
        self.__busstopno = busstopno


    def get_timingbusid(self):
        return self.__timingbusid

    def get_userid(self):
        return self.__userid

    def get_timingbus(self):
        return self.__timingbus

    def get_busno(self):
        return self.__busno

    def get_busstopno(self):
        return self.__busstopno


    def set_busstopno(self,busstopno):
        return self.__busstopno

    def set_busno(self,busno):
        self.__busno = busno

    def set_timingbus(self, timingbus):
        self.__timingbus = timingbus


    def __str__(self):
        s = self.__timingbusid + '-' + self.__userid + '-' +self.__busno+ '-'  + self.__timingbus+ '-' +self.__busstopno
        return s
