#DONE BY LOW XUAN JIE
import datetime


class Promotion:
    def __init__(self, promotion):
        str_promoid = str(datetime.datetime.now().timestamp()) # to generate promotionid using timestamp
        self.__promo = str_promoid   # promotionid is used as key for shelve
        self.__datecreated = datetime.datetime.today().strftime('%Y-%m-%d')

    def get_promo(self):
        return self.__promo

    def get_datecreated(self):
        return self.__datecreated

    def set_promo(self, promotion):
        self.__promo = promotion


    def __str__(self):
        s = self.__promo + '-' + self.__datecreated
        return s
