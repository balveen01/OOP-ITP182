#DONE BY LOW XUAN JIE
from modeltimingcondo import Timingcondo
from modeltiminghospital import Timinghospital
from modeltimingmall import Timingmall
from modeltimingbus import Timingbus
from datetime import datetime
import shelve



def createNewTimingBus(userid, timingbus, busno, busstopno):
    objstr = userid + '#' + timingbus + "#"+ busno + "#" + busstopno
    print("createNewTimingbus: for >>" + objstr)

    dbtimings = shelve.open('files\mydbtimings.db', 'c')
    new_record = Timingbus(userid, timingbus, busno,busstopno)
    print(new_record)
    dbtimings[new_record.get_timingbusid()] = new_record
    dbtimings.close()

def processSomeRecords1(bb):
    print("process: for userid >>" + bb)

    dbtimings = shelve.open('files\mydbtimings.db')
    timingbuslist = []   # create list for html display
    for row in dbtimings.keys():
        print('processAllTimingbuss: timingbus row>> ' + row)
        nobj = dbtimings[row]
        busstopno = nobj.get_busstopno()
        if busstopno == bb:
            print(nobj.get_timingbusid())
            print(nobj.get_userid())
            print(nobj.get_timingbus())
            timingbuslist.append(nobj)
    dbtimings.close() # close db file
    return timingbuslist

def processAllTimingbuss(userid):
    print("processAlltimingbuss: for userid >>" + userid)

    dbtimings = shelve.open('files\mydbtimings.db')
    timingbuslist = []   # create list for html display
    for row in dbtimings.keys():
        print('processAllTimingbuss: timingbus row>> ' + row)
        nobj = dbtimings[row]
        print(nobj.get_timingbusid())
        print(nobj.get_userid())
        print(nobj.get_timingbus())
        timingbuslist.append(nobj)
    dbtimings.close() # close db file
    return timingbuslist


def processTimingbusUpdateStatus(timingbusid):
    print('processTimingbusUpdateStatus: for timingbusid >>' + timingbusid)



def processTimingbusUpdateDetails(timingbusid, timingbus):
    dbtiming = shelve.open("files\mydbtimings.db", writeback= True)
    print("test processtimngupdartedetals >>>")
    print(timingbusid)
    print(timingbus)
    print("test processtimngupdartedetals >>>")
    for row in dbtiming.keys():
        if row == timingbusid:
            nobj = dbtiming[row]
            print(nobj)
            nobj.set_timingbus(timingbus)
            print(nobj)
            dbtiming[row] = nobj
    dbtiming.close()



def processTimingbusDeleteDetails(timingbusid):
    dbtiming = shelve.open('files/mydbtimings.db',writeback=True)
    print('test processTimingbusDeleteDetails >>>')
    print(timingbusid)
    print('test processTimingbusDeleteDetails >>>')
    for row in dbtiming.keys():
        print('note row>>' + row)
        if row == timingbusid:
            del dbtiming[row]
    dbtiming.close()


def createNewTimingHospital(userid, fromhospital, tohospital, hospital):
    objstr = userid + '#' + fromhospital + "#"+ tohospital + "#" + hospital
    print("createNewTiminghospital: for >>" + objstr)

    dbhospitaltimings = shelve.open('files\mydbhospitaltimings.db', 'c')
    new_record = Timinghospital(userid, fromhospital, tohospital,hospital)
    print(new_record)
    dbhospitaltimings[new_record.get_timinghospitalid()] = new_record
    dbhospitaltimings.close()

def processSomeRecords2(hh):
    print("process: for userid >>" + hh)

    dbhospitaltimings = shelve.open('files\mydbhospitaltimings.db')
    timinghospitallist = []   # create list for html display
    for row in dbhospitaltimings.keys():
        print('processAllTiminghospitals: timinghospital row>> ' + row)
        nobj = dbhospitaltimings[row]
        hospital = nobj.get_hospital()
        if hospital == hh:
            print(nobj.get_fromhospital())
            print(nobj.get_tohospital())
            print(nobj.get_hospital())
            timinghospitallist.append(nobj)
    dbhospitaltimings.close() # close db file
    return timinghospitallist


def processAllTiminghospitals(userid):
    print("processAlltiminghospitals: for userid >>" + userid)

    dbhospitaltimings = shelve.open('files\mydbhospitaltimings.db')
    timinghospitallist = []   # create list for html display
    for row in dbhospitaltimings.keys():
        print('processAllTiminghospitals: timinghospital row>> ' + row)
        nobj = dbhospitaltimings[row]
        print(nobj.get_timinghospitalid())
        print(nobj.get_userid())
        print(nobj.get_hospital())
        timinghospitallist.append(nobj)
    dbhospitaltimings.close() # close db file
    return timinghospitallist

def processTiminghospitalDeleteDetails(timinghospitalid):
    dbhospitaltiming = shelve.open('files/mydbhospitaltimings.db',writeback=True)
    print('test processTiminghospitalDeleteDetails >>>')
    print(timinghospitalid)
    print('test processTiminghospitalDeleteDetails >>>')
    for row in dbhospitaltiming.keys():
        print('note row>>' + row)
        if row == timinghospitalid:
            del dbhospitaltiming[row]
    dbhospitaltiming.close()

def createNewTimingMall(userid, frommall, tomall, mall):
    objstr = userid + '#' + frommall + "#"+ tomall + "#" + mall
    print("createNewTimingmall: for >>" + objstr)

    dbmalltimings = shelve.open('files\mydbmalltimings.db', 'c')
    new_record = Timingmall(userid, frommall, tomall,mall)
    print(new_record)
    dbmalltimings[new_record.get_timingmallid()] = new_record
    dbmalltimings.close()

def processSomeRecords3(mm):
    print("process: for userid >>" + mm)

    dbmalltimings = shelve.open('files\mydbmalltimings.db')
    timingmalllist = []   # create list for html display
    for row in dbmalltimings.keys():
        print('processAllTimingmalls: timingmall row>> ' + row)
        nobj = dbmalltimings[row]
        mall = nobj.get_mall()
        if mall == mm:
            print(nobj.get_frommall())
            print(nobj.get_tomall())
            print(nobj.get_mall())
            timingmalllist.append(nobj)
    dbmalltimings.close() # close db file
    return timingmalllist


def processAllTimingmalls(userid):
    print("processAlltimingmalls: for userid >>" + userid)

    dbmalltimings = shelve.open('files\mydbmalltimings.db')
    timingmalllist = []   # create list for html display
    for row in dbmalltimings.keys():
        print('processAllTimingmalls: timingmall row>> ' + row)
        nobj = dbmalltimings[row]
        print(nobj.get_timingmallid())
        print(nobj.get_userid())
        print(nobj.get_mall())
        timingmalllist.append(nobj)
    dbmalltimings.close() # close db file
    return timingmalllist

def processTimingmallDeleteDetails(timingmallid):
    dbmalltiming = shelve.open('files/mydbmalltimings.db',writeback=True)
    print('test processTimingmallDeleteDetails >>>')
    print(timingmallid)
    print('test processTimingmallDeleteDetails >>>')
    for row in dbmalltiming.keys():
        print('note row>>' + row)
        if row == timingmallid:
            del dbmalltiming[row]
    dbmalltiming.close()

def createNewTimingCondo(userid, fromcondo, tocondo, condo):
    objstr = userid + '#' + fromcondo + "#"+ tocondo + "#" + condo
    print("createNewTimingcondo: for >>" + objstr)

    dbcondotimings = shelve.open('files\mydbcondotimings.db', 'c')
    new_record = Timingcondo(userid, fromcondo, tocondo,condo)
    print(new_record)
    dbcondotimings[new_record.get_timingcondoid()] = new_record
    dbcondotimings.close()

def processSomeRecords4(cd):
    print("process: for userid >>" + cd)

    dbcondotimings = shelve.open('files\mydbcondotimings.db')
    timingcondolist = []   # create list for html display
    for row in dbcondotimings.keys():
        print('processAllTimingcondos: timingcondo row>> ' + row)
        nobj = dbcondotimings[row]
        condo = nobj.get_condo()
        if condo == cd:
            print(nobj.get_fromcondo())
            print(nobj.get_tocondo())
            print(nobj.get_condo())
            timingcondolist.append(nobj)
    dbcondotimings.close() # close db file
    return timingcondolist


def processAllTimingcondos(userid):
    print("processAlltimingcondos: for userid >>" + userid)

    dbcondotimings = shelve.open('files\mydbcondotimings.db')
    timingcondolist = []   # create list for html display
    for row in dbcondotimings.keys():
        print('processAllTimingcondos: timingcondo row>> ' + row)
        nobj = dbcondotimings[row]
        print(nobj.get_timingcondoid())
        print(nobj.get_userid())
        print(nobj.get_condo())
        timingcondolist.append(nobj)
    dbcondotimings.close() # close db file
    return timingcondolist

def processTimingcondoDeleteDetails(timingcondoid):
    dbcondotiming = shelve.open('files/mydbcondotimings.db',writeback=True)
    print('test processTimingcondoDeleteDetails >>>')
    print(timingcondoid)
    print('test processTimingcondoDeleteDetails >>>')
    for row in dbcondotiming.keys():
        print('note row>>' + row)
        if row == timingcondoid:
            del dbcondotiming[row]
    dbcondotiming.close()



def dateTime():
    now = datetime.now()
    time = now.strftime("%d-%m-%Y")
    return time


def time():
    timeNow = datetime.now().strftime("%I:%M %p")
    return timeNow

