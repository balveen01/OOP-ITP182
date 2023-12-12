#DONE BY BALVEEN
from modelBooking import Booking
from modelcamerataxi import Camera
from datetime import datetime
import shelve



def createNewBooking(userid, transportation, location, destination, time ):
    objstr = userid + '#' + transportation + "#" + location + "#" + destination + "#" + time
    print("createNewBooking: for >>" + objstr)
    dbbookings = shelve.open('files/mydbbookings.db', 'c')
    #new_record = "hello my name is balveen"
    new_record = Booking(userid, transportation, location, destination,time)
    print(new_record)
    #dbbookings["okay"] = new_record
    dbbookings[new_record.get_bookingid()] = new_record
    dbbookings.close()


def processAllbookings(userid):
    print("processAllBookings: for userid >>" + userid)
    dbbookings = shelve.open('files/mydbbookings.db')
    bookinglist = []   # create list for html display
    for row in dbbookings.keys():
        print('processAllBookings: booking row>> ' + row)
        nobj = dbbookings[row]
        print(nobj.get_bookingid())
        print(nobj.get_userid())
        print(nobj.get_location())
        print(nobj.get_destination())
        print(nobj.get_transportation())
        bookinglist.append(nobj)
    dbbookings.close() # close db file
    return bookinglist

def processBookingsByTrasnport(userid, transport):
    print("processAllBookings: for userid >>" + userid)
    dbbookings = shelve.open('files/mydbbookings.db')
    bookinglist1 = []   # create list for html display
    for row in dbbookings.keys():
        print('processAllBookings: booking row>> ' + row)
        nobj = dbbookings[row]
        if nobj.get_transportation() == transport:
            print(nobj.get_bookingid())
            print(nobj.get_userid())
            print(nobj.get_location())
            print(nobj.get_destination())
            print(nobj.get_transportation())
            bookinglist1.append(nobj)
    dbbookings.close() # close db file
    return bookinglist1


def processbookingUpdateStatus(bookingid):
    print('processBookingUpdateStatus: for bookingid >>' + bookingid)
    print('NEED YOUR CODING HERE')


def processBookingUpdateDetails(bookingid, transportation,timing):
    dbbookings = shelve.open("files/mydbbookings.db", writeback= True)
    print("test processbokingupdatedetails >>>")
    print(bookingid)
    print(transportation)
    print(timing)
    print("test processbokingupdatedetails >>>")
    for row in dbbookings.keys():
        print("booking row>>" + row)
        if row == bookingid:
            nobj = dbbookings[row]
            print(nobj)
            nobj.set_transportation(transportation)
            nobj.set_time(timing)
            print(nobj)
            dbbookings[row] = nobj
    dbbookings.close()



def processBookingDelete(bookingid):
    print("processBookingDelete: for bookingid >>" + bookingid)
    dbbookings = shelve.open("files/mydbbookings.db", writeback=True)
    print(bookingid)
    for row in dbbookings.keys():
        print("booking row >>" + row)
        if row == bookingid:
            del dbbookings[row]
    dbbookings.close()


def dateTime():
    now = datetime.now()
    time = now.strftime("%d-%m-%Y")
    return time


def time():
    timeNow = datetime.now().strftime("%I:%M %p")
    return timeNow


def createNewCamera(userid, expressway,image1,image2):
    objstr = userid + '#' + expressway  + '#' + image1 + '#' + image2
    print("createNewCamera: for >>" + objstr)

    dbcamera = shelve.open('files/mydbcamera.db', 'c')
    new_record = Camera(userid, expressway,image1,image2)
    print(new_record)
    dbcamera[new_record.get_cameraid()] = new_record
    dbcamera.close()

def processAllcamera(userid):
    print("processAllRoute: for userid >>" + userid)
    dbcamera = shelve.open('files/mydbcamera.db')
    cameralist = []   # create list for html display
    for row in dbcamera.keys():
        print('processAllCamera: camera row>> ' + row)
        robj = dbcamera[row]
        print(robj.get_cameraid())
        print(robj.get_userid())
        print(robj.get_expressway())
        print(robj.get_image1())
        print(robj.get_image2())
        print(robj.get_datecreated())
        cameralist.append(robj)
    dbcamera.close() # close db file
    return cameralist

def processAllcameraexpressway(userid, expressway):
    print("processAllCamera: for userid >>" + userid)
    dbcamera = shelve.open('files/mydbcamera.db')
    cameralist = []   # create list for html display
    for row in dbcamera.keys():
        print('processAllCameraexpressway: camera row>> ' + row)
        nobj = dbcamera[row]
        if nobj.get_expressway() == expressway:
            print(nobj.get_cameraid())
            print(nobj.get_userid())
            print(nobj.get_expressway())
            print(nobj.get_image1)
            print(nobj.get_image2)
            print(nobj.get_datecreated())
            cameralist.append(nobj)
    dbcamera.close() # close db file
    return cameralist


