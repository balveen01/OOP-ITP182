#DONE BY BALVEEN
import datetime

class Camera:
    def __init__(self, userid, expressway,image1,image2):
        str_cameraid = str(datetime.datetime.now().timestamp())
        self.__cameraid = str_cameraid
        self.__userid = userid
        self.__expressway = expressway
        #self.__location = location
        self.__image1 = image1
        self.__image2 = image2
        self.__datecreated = datetime.datetime.today().strftime('%Y-%m-%d')

    def get_userid(self):
        return self.__userid

    def get_expressway(self):
        return self.__expressway

    def get_datecreated(self):
        return self.__datecreated

    def get_cameraid(self):
        return self.__cameraid

    #def get_location(self):
        #return self.__location

    def get_image1(self):
        return self.__image1

    def set_image1(self, image1):
        self.__image1 = image1

    def get_image2(self):
        return self.__image2

    def set_image2(self, image2):
        self.__image2 = image2

    #def set_location(self,location):
        #return self.__location

    def set_expressway(self, expressway):
        self.__expressway= expressway


    def __str__(self):
        s = self.__cameraid + "-" + self.__userid + '-' + self.__datecreated + '-'  + "-" + self.__expressway
        return s
