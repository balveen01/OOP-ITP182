#DONE BY LOW XUAN JIE
import datetime


class Timingcondo:
    def __init__(self, userid, fromcondo, tocondo, condo):
        str_timingcondoid = str(datetime.datetime.now().timestamp()) # to generate timingbusid using timestamp
        self.__timingcondoid = str_timingcondoid   # timingbus id is used as key for shelve
        self.__userid = userid
        self.__fromcondo = fromcondo #bus stop no.
        self.__tocondo = tocondo
        self.__condo = condo

    def get_timingcondoid(self):
        return self.__timingcondoid

    def get_userid(self):
        return self.__userid

    def get_fromcondo(self):
        return self.__fromcondo

    def get_tocondo(self):
        return self.__tocondo

    def get_condo(self):
        return self.__condo

    def set_fromcondo(self,fromcondo):
        return self.__fromcondo

    def set_tocondo(self,tocondo):
        self.__tocondo = tocondo

    def set_condo(self, condo):
        self.__condo = condo


    def __str__(self):
        s = self.__timingcondoid + '-' + self.__userid + '-' +self.__fromcondo+ '-'  + self.__tocondo+ '-' +self.__condo
        return s
