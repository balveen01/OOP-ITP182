#DONE BY DANYCE LEE
import datetime

class Parking:
    def __init__(self, userid, location, station,image1):
        str_parkingid = str(datetime.datetime.now().timestamp()) # to generate parkingid using timestamp
        self.__parkingid = str_parkingid   # parkingid is used as key for shelve
        self.__userid = userid
        self.__image1= image1
        self.__station = station
        self.__location = location
        self.__status = 'statusA'
        self.__datecreated = datetime.datetime.today().strftime('%m-%d-%Y')

    def get_parkingid(self):
        return self.__parkingid

    def get_location(self):
        return self.__location

    def get_userid(self):
        return self.__userid

    def get_station(self):
        return self.__station

    def get_status(self):
        return self.__status

    def get_datecreated(self):
        return self.__datecreated

    def get_image1(self):
        return self.__image1

    def set_station(self, station):
        self.__station = station

    def set_location(self,location):
        self.__location = location

    def set_status(self, status):
        self.__status = status

    def set_image1(self, image1):
        self.__image1 = image1

    def __str__(self):
        s = self.__parkingid + '-' + self.__userid + '-' + self.__station + '-' + self.__datecreated + '-' + self.__status + "-" + self.__location
        return s



