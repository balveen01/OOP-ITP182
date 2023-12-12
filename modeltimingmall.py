#DONE BY LOW XUAN JIE
import datetime


class Timingmall:
    def __init__(self, userid, frommall, tomall, mall):
        str_timingmallid = str(datetime.datetime.now().timestamp()) # to generate timingbusid using timestamp
        self.__timingmallid = str_timingmallid   # timingbus id is used as key for shelve
        self.__userid = userid
        self.__frommall = frommall #bus stop no.
        self.__tomall = tomall
        self.__mall= mall

    def get_timingmallid(self):
        return self.__timingmallid

    def get_userid(self):
        return self.__userid

    def get_frommall(self):
        return self.__frommall

    def get_tomall(self):
        return self.__tomall

    def get_mall(self):
        return self.__mall

    def set_frommall(self,frommall):
        return self.__frommall

    def set_tomall(self,tomall):
        self.__tomall = tomall

    def set_mall(self, mall):
        self.__mall = mall


    def __str__(self):
        s = self.__timingmallid + '-' + self.__userid + '-' +self.__frommall+ '-'  + self.__tomall+ '-' +self.__mall
        return s
