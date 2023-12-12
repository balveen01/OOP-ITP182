#DONE BY MICAH ANGELA
class Exit:
    def __init__(self, userid, station, image1, image2, image3, image4):
        self.__userid = userid
        self.__station = station
        self.__image1 = image1
        self.__image2 = image2
        self.__image3 = image3
        self.__image4 = image4

    def get_userid(self):
        return self.__userid

    def get_station(self):
        return self.__station


    def get_image1(self):
        return self.__image1

    def get_image2(self):
        return self.__image2

    def get_image3(self):
        return self.__image3

    def get_image4(self):
        return self.__image4

    def set_station(self, station):
        self.__station = station

    def set_image1(self, image1):
        self.__image1 = image1

    def set_image2(self, image2):
        self.__image2 = image2

    def set_image3(self, image3):
        self.__image3 = image3

    def set_image4(self, image4):
        self.__image4 = image4


    def __str__(self):
        s = self.__userid + '-' + self.__station + '-'
        return s

