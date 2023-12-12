#DONE BY LOW XUAN JIE
import datetime


class Timinghospital:
    def __init__(self, userid, fromhospital, tohospital, hospital):
        str_timinghospitalid = str(datetime.datetime.now().timestamp()) # to generate timingbusid using timestamp
        self.__timinghospitalid = str_timinghospitalid   # timingbus id is used as key for shelve
        self.__userid = userid
        self.__fromhospital = fromhospital #bus stop no.
        self.__tohospital = tohospital
        self.__hospital= hospital

    def get_timinghospitalid(self):
        return self.__timinghospitalid

    def get_userid(self):
        return self.__userid

    def get_fromhospital(self):
        return self.__fromhospital

    def get_tohospital(self):
        return self.__tohospital

    def get_hospital(self):
        return self.__hospital

    def set_fromhospital(self,fromhospital):
        return self.__fromhospital

    def set_tohospital(self,tohospital):
        self.__tohospital = tohospital

    def set_hospital(self, hospital):
        self.__hospital = hospital


    def __str__(self):
        s = self.__timinghospitalid + '-' + self.__userid + '-' +self.__fromhospital+ '-'  + self.__tohospital+ '-' +self.__hospital
        return s
