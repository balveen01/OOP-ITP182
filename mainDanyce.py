#DONE BY DANYCE LEE
from modelCycling import Route
from modelParking import Parking
from modelPromotion import Promotion

from datetime import datetime
import shelve


def createNewRoute(userid, location, destination,image):
    objstr = userid + '#' + location + destination + image
    print("createNewRoute: for >>" + objstr)

    dbroutes = shelve.open('files\mydbroutes.db', 'c')
    new_record = Route(userid, location, destination,image)
    print(new_record)
    dbroutes[new_record.get_routeid()] = new_record
    dbroutes.close()


def processAllRoutes(userid):
    print("processAllRoutes: for userid >>" + userid)

    dbroutes = shelve.open('files\mydbroutes.db')
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

    dbroutes = shelve.open('files\mydbroutes.db')
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



def processRouteUpdateStatus(routeid):
    print('processRouteUpdateStatus: for routeid >>' + routeid)


def processRouteDeleteDetails(routeid):
    dbroutes = shelve.open("files\mydbroutes.db",writeback=True)
    print(routeid)
    for row in dbroutes.keys():
        print("note row >>" + row)
        if row == routeid:
                del dbroutes[row]
    dbroutes.close()

def processRouteUpdateDetails(routeid,location,destination):
    dbroutes = shelve.open("files\mydbroutes.db",writeback=True)
    print('test processRouteUpdateDetails >>>')
    print(routeid)
    print(location)
    print(destination)

    print('test processRouteUpdateDetails >>>')
    for row in dbroutes.keys():
        print("note row >>" + row)
        if row == routeid:
               nobj = dbroutes[row]
               print(nobj)
               nobj.set_location(location)
               nobj.set_destination(destination)

               print(nobj)
               dbroutes[row]= nobj
    dbroutes.close()


def dateTime():
    now = datetime.now()
    time = now.strftime("%d-%m-%Y")
    return time


def time():
    timeNow = datetime.now().strftime("%I:%M %p")
    return timeNow



def createNewParking(userid,location, station,image1):
    objstr = userid + '#' + station + "#" + image1 + "#" + location
    print("createNewParking: for >>" + objstr)

    dbparkings = shelve.open('files\mydbparkings.db', 'c')
    new_record = Parking(userid,location, station,image1)
    print(new_record)
    dbparkings[new_record.get_parkingid()] = new_record
    dbparkings.close()


def processAllParkings(userid):
    print("processAllParkings: for userid >>" + userid)

    dbparkings = shelve.open('files\mydbparkings.db')
    parkinglist = []   # create list for html display
    for row in dbparkings.keys():
        print('processAllParkings: parking row>> ' + row)
        nobj = dbparkings[row]
        print(nobj.get_parkingid())
        print(nobj.get_location())
        print(nobj.get_userid())
        print(nobj.get_station())
        print(nobj.get_datecreated())
        print(nobj.get_status())
        parkinglist.append(nobj)
    dbparkings.close() # close db file
    return parkinglist

def processAllParkingsStation(userid, station):
    print("processAllParkings: for userid >>" + userid)

    dbparkings = shelve.open('files\mydbparkings.db')
    parkinglist = []   # create list for html display
    for row in dbparkings.keys():
        print('processAllParkings: parking row>> ' + row)
        nobj = dbparkings[row]
        if nobj.get_station () == station:
            print(nobj.get_parkingid())
            print(nobj.get_location())
            print(nobj.get_userid())
            print(nobj.get_station())
            print(nobj.get_datecreated())
            print(nobj.get_status())
            parkinglist.append(nobj)
    dbparkings.close() # close db file
    return parkinglist


def processParkingDeleteDetails(parkingid):
    dbparkings = shelve.open("files\mydbparkings.db",writeback=True)
    print(parkingid)
    for row in dbparkings.keys():
        print("note row >>" + row)
        if row == parkingid:
                del dbparkings[row]
    dbparkings.close()

def processParkingUpdateDetails(parkingid,parking):
    dbparking = shelve.open("files\mydbparkings.db",writeback=True)
    print('test processParkingUpdateDetails >>>')
    print(parkingid)
    print(parking)
    print('test processParkingUpdateDetails >>>')
    for row in dbparking.keys():
        print("note row >>" + row)
        if row == parkingid:
               nobj = dbparking[row]
               print(nobj)
               nobj.set_parkingid(parking)
               print(nobj)
               dbparking[row]= nobj
    dbparking.close()


def createNewPromotion(userid, promotion):
    objstr = userid + '#' + promotion
    print("createNewPromotion: for >>" + objstr)

    dbpromotion = shelve.open('files\mydbpromotion.db', 'c')
    new_record = Promotion(userid, promotion)
    print(new_record)
    dbpromotion[new_record.get_promo()] = new_record
    dbpromotion.close()


def processAllPromotion(userid,):
    print("processAllPromotion: for userid >>" + userid)

    dbpromotion = shelve.open('files\mydbpromotion.db')
    promotionlist = []   # create list for html display
    for row in dbpromotion.keys():
        print('processAllPromotion: promo row>> ' + row)
        nobj = dbpromotion[row]
        print(nobj.get_promotionid())
        print(nobj.get_datecreated())
        promotionlist.append(nobj)
    dbpromotion.close() # close db file
    return promotionlist

def processAllFavourite(userid,):
    print("processAllFavourite: for userid >>" + userid)

    dbfavourite = shelve.open('files\mydbfavourite.db')
    favouritelist = []   # create list for html display
    for row in dbfavourite.keys():
        print('processAllRoutes: route row>> ' + row)
        nobj = dbfavourite[row]
        print(nobj.get_favourite())
        favouritelist.append(nobj)
    dbfavourite.close() # close db file
    return favouritelist

