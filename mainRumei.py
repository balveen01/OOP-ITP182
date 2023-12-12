#DONE BY LIM RU MEI
from modelWalking import Route

from datetime import datetime
import shelve




def createNewRoute(userid, location, destination,image):
    objstr = userid + '#' + location + destination + image
    print("createNewRoute: for >>" + objstr)

    dbroutes = shelve.open('files\mydbwalking.db', 'c')
    new_record = Route(userid, location, destination,image)
    print(new_record)
    dbroutes[new_record.get_routeid()] = new_record
    dbroutes.close()


def processAllRoutes(userid):
    print("processAllRoutes: for userid >>" + userid)

    dbroutes = shelve.open('files\mydbwalking.db')
    routelist = []   # create list for html display
    for row in dbroutes.keys():
        print('processAllRoutes: route row>> ' + row)
        nobj = dbroutes[row]
        print(nobj.get_routeid())
        print(nobj.get_userid())
        print(nobj.get_image())
        print(nobj.get_location())
        print(nobj.get_destination())
        print(nobj.get_datecreated())
        print(nobj.get_status())
        routelist.append(nobj)
    dbroutes.close() # close db file
    return routelist


def processAllRouteslocation(userid, location):
    print("processAllRoutes: for userid >>" + userid)

    dbroutes = shelve.open('files\mydbwalking.db')
    routelist = []   # create list for html display
    for row in dbroutes.keys():
        print('processAllRoutes: route row>> ' + row)
        nobj = dbroutes[row]
        if nobj.get_location() == location:
            print(nobj.get_routeid())
            print(nobj.get_userid())
            print(nobj.get_image())
            print(nobj.get_location())
            print(nobj.get_destination())
            print(nobj.get_datecreated())
            print(nobj.get_status())
            routelist.append(nobj)
    dbroutes.close() # close db file
    return routelist



def dateTime():
    now = datetime.now()
    time = now.strftime("%d-%m-%Y")
    return time


def time():
    timeNow = datetime.now().strftime("%I:%M %p")
    return timeNow
