#DONE BY LOW XUAN JIE
import datetime


class TimingHospitalViewer:
    def __init__(self, userid, hospital):
        str_timinghospitalviewid = str(datetime.datetime.now().timestamp()) # to generate timingbusid using timestamp
        self.__timinghospitalid = str_timinghospitalviewid   # timingbus id is used as key for shelve
        self.__userid = userid
        self.__hospital = hospital



    def get_timinghospitalid(self):
        return self.__timinghospitalid

    def get_userid(self):
        return self.__userid

    def get_hospital(self):
        return self.__hospital


    def set_hospital(self,hospital):
        self.__hospital = hospital


    def __str__(self):
        s = self.__timinghospitalid + '-' + self.__userid + '-' +self.__hospital
        return s
