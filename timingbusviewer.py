import datetime


class TimingbusViewer:
    def __init__(self, userid, busstopno, busno):
        str_timingbusviewid = str(datetime.datetime.now().timestamp()) # to generate timingbusid using timestamp
        self.__timingbusid = str_timingbusviewid   # timingbus id is used as key for shelve
        self.__userid = userid
        self.__busstopno = busstopno
        self.__busno = busno


    def get_busno(self):
        return self.__busno

    def get_timingbusid(self):
        return self.__timingbusid

    def get_userid(self):
        return self.__userid

    def get_busstopno(self):
        return self.__busstopno


    def set_busno(self,busno):
        self.__busno = busno

    def set_busstopno(self,busstopno):
        self.__busstopno = busstopno


    def __str__(self):
        s = self.__timingbusid + '-' + self.__userid + '-' +self.__busstopno
        return s
