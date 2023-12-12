#DONE BY BALVEEN
import datetime


class Booking:
    def __init__(self, userid, transportation, location, destination, time):
        str_bookingid = str(datetime.datetime.now().timestamp()) # to generate noteid using timestamp
        self.__bookingid = str_bookingid
        self.__userid = userid
        self.__transportation = transportation
        self.__datecreated = datetime.datetime.today().strftime('%Y-%m-%d')
        self.__location = location
        self.__destination = destination
        self.__time = time
        self.__transportation = transportation

    def get_transportation(self):
        return self.__transportation


    def get_destination(self):
        return self.__destination

    def get_location(self):
        return self.__location

    def get_bookingid(self):
        return self.__bookingid

    def get_userid(self):
        return self.__userid

    def get_datecreated(self):
        return self.__datecreated

    def get_time(self):
        return self.__time

    def set_time(self, time):
        self.__time = time

    def set_location(self, location):
        self.__location = location


    def set_destination(self, destination):
        self.__destination = destination

    def set_transportation(self, transportation):
        self.__transportation = transportation


    def __str__(self):
        s = self.__bookingid + '-' + self.__userid + '-' + self.__transportation + '-' + self.__datecreated + '-'  + "-" + self.__location + "-" + self.__destination + "-" + self.__time
        return s
