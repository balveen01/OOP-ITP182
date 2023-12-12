#DONE BY MICAH ANGELA
import datetime


class Timing:
    def __init__(self, userid, location, destination, time):
        str_timingid = str(datetime.datetime.now().timestamp()) # to generate timingid using timestamp
        self.__timingid = str_timingid   # timingid is used as key for shelve
        self.__userid = userid
        self.__location = location
        self.__destination = destination
        self.__time = time
        self.__status = 'Arriving'
        self.__datecreated = datetime.datetime.today().strftime('%d-%m-%Y')

    def get_timingid(self):
        return self.__timingid

    def get_userid(self):
        return self.__userid

    def get_location(self):
        return self.__location

    def get_destination(self):
        return self.__destination

    def get_time(self):
        return self.__time

    def get_status(self):
        return self.__status

    def get_datecreated(self):
        return self.__datecreated

    def set_location(self, location):
        self.__location = location

    def set_destination(self,destination):
        self.__destination = destination

    def set_time(self, time):
        self.__time = time

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        s = self.__timingid + '-' + self.__userid + '-' + self.__location + '-' + self.__datecreated + '-' + self.__status + "-" + self.__destination + "-" + self.__time
        return s
