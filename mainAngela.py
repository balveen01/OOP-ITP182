#DONE BY MICAH ANGELA
from modelTimingMRT import Timing
from datetime import datetime
from modelExit import Exit
import shelve


def createNewTiming(userid, location,destination, time):
    objstr = userid + '#' + location + "#" + destination + "#" + time
    print("createNewTiming: for >>" + objstr)

    dbtimings = shelve.open('files\mydbtimingmrts.db', 'c')
    new_record = Timing(userid, location, destination, time)
    print(new_record)
    dbtimings[new_record.get_timingid()] = new_record
    dbtimings.close()


def processAllTimings(userid):
    print("processAllTimings: for userid >>" + userid)

    dbtimings = shelve.open('files\mydbtimingmrts.db')
    timinglist = []   # create list for html display
    for row in dbtimings.keys():
        print('processAllTimings: timing row>> ' + row)
        nobj = dbtimings[row]
        print(nobj.get_timingid())
        print(nobj.get_userid())
        print(nobj.get_location())
        print(nobj.get_destination())
        print(nobj.get_time())
        print(nobj.get_datecreated())
        print(nobj.get_status())
        timinglist.append(nobj)
    dbtimings.close() # close db file
    return timinglist


def processTimingUpdateStatus(timingid):
    print('processTimingUpdateStatus: for timingid >>' + timingid)
    print('NEED YOUR CODING HERE')


def processTimingUpdateDetails(timingid, timing):
    dbtimings = shelve.open('files\mydbtimingmrts.db', writeback=True)
    print('test processTimingUpdateDetails >>>')
    print(timingid)
    print(timing)
    print('test processTimingUpdateDetails >>>')
    for row in dbtimings.keys():
        print('timing row >> ' + row)
        if row == timingid:
            nobj = dbtimings[row]
            print(nobj)
            print(nobj)
            dbtimings[row] = nobj
    dbtimings.close()


def processTimingDeleteDetails(timingid):
    dbnotes = shelve.open('files\mydbtimingmrts.db', writeback = True)
    print(timingid)
    for row in dbnotes.keys():
        print('timing row>> ' + row)
        if row == timingid:
            del dbnotes[row]

    dbnotes.close()


def dateTime():
    now = datetime.now()
    time = now.strftime("%d-%m-%Y")
    return time


def time():
    timeNow = datetime.now().strftime("%I:%M %p")
    return timeNow


def createNewExit(userid, station,image1,image2,image3,image4):
    objstr = userid + '#' + station + "#" + image1 + "#" + image2 + "#" + image3 + "#" + image4
    print("createNewTiming: for >>" + objstr)

    dbexit = shelve.open('files\mydbexit.db', 'c')
    new_record = Exit(userid, station, image1,image2,image3,image4)
    print(new_record)
    dbexit[new_record.get_station()] = new_record
    dbexit.close()


def processAllExit(userid):
    print("processAllTimings: for userid >>" + userid)

    dbexit = shelve.open('files\mydbexit.db')
    exitlist = []   # create list for html display
    for row in dbexit.keys():
        print('processAllExit: timing row>> ' + row)
        nobj = dbexit[row]
        print(nobj.get_station())
        print(nobj.get_image1())
        print(nobj.get_image2())
        print(nobj.get_image3())
        print(nobj.get_image4())
        exitlist.append(nobj)
    dbexit.close() # close db file
    return exitlist


def processAllExitstation(userid,station):
    print(">>>>>>>>>>>>>: for userid >>" + userid)

    dbexit = shelve.open('files\mydbexit.db')
    exitlist = []   # create list for html display
    for row in dbexit.keys():
        print('processAllExit: timing row>> ' + row)
        nobj = dbexit[row]
        if nobj.get_station() == station:
            print(nobj.get_station())
            print(nobj.get_image1())
            print(nobj.get_image2())
            print(nobj.get_image3())
            print(nobj.get_image4())
            exitlist.append(nobj)
    dbexit.close() # close db file
    return exitlist
