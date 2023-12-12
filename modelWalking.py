#DONE BY BALVEEN KAUR AND LIM RU MEI
import datetime


class Route:
    def __init__(self, userid, location,destination,image):
        str_routeid = str(datetime.datetime.now().timestamp()) # to generate routeid using timestamp
        self.__routeid = str_routeid   # routeid is used as key for shelve
        self.__userid = userid
        self.__location = location
        self.__image = image
        self.__destination = destination
        self.__status = 'statusA'
        self.__datecreated = datetime.datetime.today().strftime('%m-%d-%Y')

    def get_routeid(self):
        return self.__routeid

    def get_userid(self):
        return self.__userid

    def get_image(self):
        return self.__image

    def get_location(self):
        return self.__location

    def get_destination(self):
        return self.__destination

    def get_status(self):
        return self.__status

    def get_datecreated(self):
        return self.__datecreated

    def set_location(self, location):
        self.__location = location

    def set_image(self,image):
        self.__image = image

    def set_destination(self, destination):
        self.__destination = destination

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        s = self.__routeid + '-' + self.__userid + '-' + self.__location + '-' + self.__destination + '-' + self.__datecreated + '-' + self.__status
        return s
