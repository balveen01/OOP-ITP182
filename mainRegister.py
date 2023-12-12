#DONE BY LIM RU MEI
import shelve
import datetime
import uuid



class User:
    def __init__(self, id):
        self.__id = id
        self.__firstname = ''
        self.__lastname = ''
        self.__username = ''
        self.__email = ''
        self.__password = ''
        self.__handphonenumber = ''
        self.__homeaddress = ''
        self.__workaddress = ''
        self.__otheraddress = ''

    def get_id(self):
        return self.__id

    def get_firstname(self):
        return self.__firstname

    def get_lastname(self):
        return self.__lastname

    def get_username(self):
        return self.__username

    def get_email(self):
        return self.__email

    def get_password(self):
        return self.__password

    def get_handphonenumber(self):
        return self.__handphonenumber

    def get_homeaddress(self):
        return self.__homeaddress

    def get_schooladdress(self):
        return self.__schooladdress

    def get_workaddress(self):
        return self.__workaddress

    def get_otheraddress(self):
        return self.__otheraddress

    # def set_uid(self, uid):
    #     self.__uid = uid

    def set_firstname(self, firstname):
        self.__firstname = firstname

    def set_lastname(self, lastname):
        self.__lastname = lastname

    def set_username(self, username):
        self.__username = username

    def set_email(self, email):
        self.__email = email

    def set_password(self, password):
        self.__password = password

    def set_handphonenumber(self, handphonenumber):
        self.__handphonenumber = handphonenumber

    def set_homeaddress(self, homeaddress):
        self.__homeaddress = homeaddress

    def set_workaddress(self, workaddress):
        self.__workaddress = workaddress

    def set_otheraddress(self, otheraddress):
        self.__otheraddress = otheraddress

users = shelve.open('user')
blogs = shelve.open('blog')

def create_user(firstname, lastname, username, email, password, handphonenumber, homeaddress, workaddress, otheraddress ):

    id = str(uuid.uuid4())
    user = User(id)
    user.set_firstname(firstname)
    user.set_lastname(lastname)
    user.set_username(username)
    user.set_email(email)
    user.set_password(password)
    user.set_handphonenumber(handphonenumber)
    user.set_homeaddress(homeaddress)
    user.set_workaddress(workaddress)
    user.set_otheraddress(otheraddress)
    users[id] = user


# def get_user(firstname, lastname, username, email, password, handphonenumber, homeaddress, workaddress, otheraddress ):
#     klist = list(users.keys())
#     for key in klist:
#         user =users[key]
#         print(user.get_firstname(), firstname, user.get_lastname(), lastname, user.get_username(), username, user.get_email(), email, user.get_password(), password, user.get_handphonenumber(), handphonenumber, user.get_homeaddress(), homeaddress, user.get_workaddress(), workaddress, user.get_otheraddress(), otheraddress)
#         if user.get_firstname() == firstname and user.get_lastname() == lastname and user.get_username() == username and user.get_email() == email and user.get_handphonenumber() == handphonenumber and user.get_password() == password and user.get_homeaddress() == homeaddress and user.get_workaddress() == workaddress and user.get_otheraddress() == otheraddress:
#             return user
#     return None

def get_user(username, password):
    klist = list(users.keys())
    for key in klist:
        user = users[key]
        print(user.get_username(), username, user.get_password(), password)
        if user.get_username() == username and user.get_password() == password:
            return user
    return None
