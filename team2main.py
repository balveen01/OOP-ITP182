#DONE BY BALVEEN, DANYCE, RU MEI, LOW XUAN JIE AND ANGELA (DONE INDIVIDUALLY)
from flask import Flask
from flask import render_template, flash, redirect, url_for
from flask import request
from flask import session
import shelve
from wtforms import form
import functools

from mainRegister import create_user
from mainRegister import get_user


from team2forms import *
import mainBalveen
import mainSteph
import mainRumei
import mainDanyce
import mainAngela

app = Flask(__name__)
app.secret_key = 'secret987'

#user done by Ru Mei
@app.route('/')
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username or password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                session['userid'] = username
                return redirect(url_for('homepage2'))
        flash(error)
    return render_template('login.html')

#HOME PAGE DONE BY BALVEEN KAUE
@app.route('/home')
def home():
    return render_template('HOME.html', session_userid=session['userid'])

# @app.route('/homepage2')
# def homepage2():
#     return render_template('homepage2.html',session_userid=session['userid'])


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session['id'] is None:
            return redirect(url_for('login'))
        return view(**kwargs)
    return wrapped_view



# @app.route('/home2')
# def home2():
#     return render_template('homepage2.html')

@app.route('/login',  methods=('GET', 'POST'))
def login():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        else:
            user = get_user(username, password)
            if user is None:
                error = 'Wrong username and password'
            else:
                session['id'] = user.get_id()
                session['user_name'] = user.get_username()
                session['userid'] = username
                return redirect(url_for('home'))
        flash(error)
    return render_template('login.html')

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        handphonenumber = request.form['handphonenumber']
        homeaddress = request.form['homeaddress']
        workaddress = request.form['workaddress']
        otheraddress = request.form['otheraddress']
        error = None

        if not firstname:
            error = 'Fistname is required'
        elif not lastname:
            error = 'Lastname is required'
        elif not username:
            error = 'Username is required.'
        elif not email:
            error = 'Email is required.'
        elif not password:
            error = 'Password is required.'
        elif not handphonenumber:
            error = 'Handphone number is required.'
        elif not homeaddress:
            error = 'Home address is required.'
        elif not workaddress:
            error = 'Work address is required.'
        elif not otheraddress:
            error = 'Other address is required.'

        else:
            create_user(firstname, lastname, username, email, password, handphonenumber, homeaddress, workaddress, otheraddress)
            return redirect(url_for('login', form=form))
        flash(error)
    return render_template('register.html' ,form =form)

@app.route('/logout')
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

#WALKING ROUTE DONE BY ...

@app.route('/walking_create', methods=['GET', 'POST'])
def walking_create():
    print("Creating route")
    destination = "Yio Chu Kang"
    location1 = "Bishan"
    image1 = "BYCK.PNG"
    mainRumei.createNewRoute(session['userid'],location1, destination, image1)

    print("Creating route")
    destination = "Aljunied"
    location2 = "EW"
    image1 = "KY.PNG"
    mainRumei.createNewRoute(session['userid'], location2, destination, image1)

    print("Creating route")
    destination = "Promenade"
    location3 = "Kallang"
    image1 = "KP.PNG"
    mainRumei.createNewRoute(session['userid'],location3, destination, image1)
    return redirect(url_for("walking_retrieve"))

@app.route('/walking_retrieve', methods=['GET', 'POST'])
def walking_retrieve():
    routelist = []
    form = Searchroute(request.form)
    routelist = mainRumei.processAllRoutes(session['userid'])
    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            location = form.location.data
            destination = form.destination.data
            image1 = form.image1.data
            mainRumei.createNewRoute(session['userid'], location,destination, image1)
            flash("Parking created")
            return redirect(url_for('walking_search'))
    return render_template('walkinglist.html', session_userid=session['userid'], route=routelist,form=form, count=len(routelist))

@app.route("/walking_search",  methods=['GET', 'POST'])
def walking_search():
    form = Searchwalking(request.form)
    routelist1 = []
    location = form.location.data
    routelist1 = mainRumei.processAllRouteslocation(session["userid"],location)
    return render_template('walkingsearch.html', session_userid=session['userid'], route1=routelist1,form=form,count=len(routelist1))


#BOOKINGS DONE BY BALVEEN
@app.route('/booking_create', methods=['GET', 'POST'])
def booking_create():
    form = CreateBookingForm(request.form)

    nlist = []
    nlist = mainBalveen.processAllbookings(session['userid']) # to find the number of bookings created

    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            transportation = form.transportation.data
            location = form.location.data
            destination = form.destination.data
            time = form.time.data
            mainBalveen.createNewBooking(session['userid'], transportation, location, destination, time)
            flash("booking created")
            return redirect(url_for('booking_retrieve'))
    return render_template('bookingcreate.html', session_userid=session['userid'], form=form, count=len(nlist))


@app.route('/booking_retrieve', methods=['GET', 'POST'])
def booking_retrieve():
    bookinglist = []
    form = Searchbooking(request.form)
    transport = form.search.data
    bookinglist = mainBalveen.processAllbookings(session['userid'])
    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            transport = form.search.data
            bookinglist = mainBalveen.processBookingsByTrasnport(session['userid'], transport)
            return redirect(url_for('booking_search'))
    return render_template('bookinglisting.html', session_userid=session['userid'], bookings=bookinglist,form=form, count=len(bookinglist))

@app.route("/booking_search",  methods=['GET', 'POST'])
def booking_search():
    form = Searchbooking(request.form)
    bookinglist1 = []
    transport = form.search.data
    bookinglist1 = mainBalveen.processBookingsByTrasnport(session["userid"], transport)
    return render_template('bookingsearch.html', session_userid=session['userid'], booking1s=bookinglist1,form=form, count=len(bookinglist1), transport=transport)


@app.route('/booking_update_details/<string:bookingstr>/', methods=['GET', 'POST'])
def booking_update_details(bookingstr):
    print('bookingupdate >>' + bookingstr)
    bookingid = bookingstr
    form = UpdatebookingForm(request.form)
    form.bookingid.data = bookingid
    #transportation = form.transportation.data
    #timing = form.time.data
    #bookinglist1 = mainBalveen.processBookingUpdateDetails(bookingid, timing, transportation)
    return render_template('bookingupdate.html', session_userid=session['userid'], form=form, bookingid=bookingid)

@app.route("/booking_update_save", methods= ["GET","POST"])
def booking_update_save():
    print("the method is " + request.method)
    form = UpdatebookingForm(request.form)
    if request.method == "POST":
        if not form.validate():
            print("all fields are required")
        else:
            bookingid = form.bookingid.data
            transportation = form.transportation.data
            timing = form.timing.data
            print("test booking_update_save >>")
            print(bookingid)
            print(transportation)
            print(timing)
            print("test booking_update_save >>")
            mainBalveen.processBookingUpdateDetails(bookingid,transportation,timing)
            flash("note edited")
            return redirect(url_for("booking_retrieve"))
        return render_template("bookingupdate.html", session_userid = session["userid"], form = form )

@app.route('/booking_update_status/<string:bookingstr>/', methods=['GET', 'POST'])
def booking_update_status(bookingstr):
    print('bookingupdate >>' + bookingstr)
    form = Searchbooking(request.form)
    transport = form.search.data
    bookinglist1 = []
    bookinglist1 = mainBalveen.processBookingsByTrasnport(session["userid"], transport)
    bookingid = bookingstr
    mainBalveen.processbookingUpdateStatus(bookingid)
    flash("booking status updated")
    bookinglist = []
    bookinglist = mainBalveen.processAllbookings(session['userid'])
    return render_template('bookinglisting.html', session_userid=session['userid'], bookings=bookinglist, booking1s=bookinglist1, form=form,count=len(bookinglist))

@app.route('/booking_delete/<string:bookingstr>/', methods=['GET', 'POST'])
def booking_delete(bookingstr):
    bookingid = bookingstr
    print('bookingdelete >>' + bookingid)
    mainBalveen.processBookingDelete(bookingid)
    flash("booking deleted")
    return redirect(url_for("booking_retrieve"))

#TAXI ROUTE DONE BY BALVEEN

@app.route('/camerataxi_create')
def camerataxi_create():
    print("Creating expressway")
    expressway1 = "AYE"
    image1 = "trafficAYE1.jpg"
    image2 = "trafficAYE2.jpg"
    mainBalveen.createNewCamera(session['userid'], expressway1, image1, image2)

    print("Creating expressway")
    expressway1 = "CTE"
    image1 = "trafficCTE1.jpg"
    image2 = "trafficCTE2.jpg"
    mainBalveen.createNewCamera(session['userid'], expressway1, image1, image2)

    print("Creating expressway")
    expressway1 = "Woodlands Checkpoint"
    image1 = "woodssg.jpg"
    image2 = "woodsjohor.jpg"
    mainBalveen.createNewCamera(session['userid'], expressway1, image1, image2)

    return redirect(url_for("camerataxi_retreive"))
    #return render_template('HOME.html',session_userid=session['userid'] )

@app.route('/camerataxi_retreive', methods=['GET', 'POST'])
def camerataxi_retreive():
    cameralist = []
    form = Searchcamera(request.form)
    cameralist = mainBalveen.processAllcamera(session["userid"])
    print("the method is " + request.method)
    if request.method == "POST":
        if not form.validate():
            print("all fields are required")
        else:
            print("test 2")
            expressway = form.expressway.data
            image1 = form.image1.data
            image2 = form.image2.data
            mainBalveen.createNewCamera(session['userid'],expressway,image1,image2)
            return redirect(url_for("camera_search"))
    return render_template('taxicameralisting.html', session_userid=session['userid'], cameras=cameralist, count=len(cameralist),form=form)


@app.route("/camera_search",  methods=['GET', 'POST'])
def camera_search():
    form = Searchcamera(request.form)
    cameralist1 = []
    expressway = form.expressway.data
    cameralist1 = mainBalveen.processAllcameraexpressway(session["userid"], expressway)
    return render_template('taxicamerasearch.html', session_userid=session['userid'], camera1s=cameralist1,form=form,count=len(cameralist1), expressway = expressway)















#CYCLING DONE BY DANYCE

@app.route('/cycling1_delete/<string:routestr>/', methods=['GET'])
def cycling1_delete(routestr):
    routeid = routestr
    mainDanyce.processRouteDeleteDetails(routeid)
    flash("note edited")
    return redirect(url_for("route_retrieve"))



@app.route('/cycling2_delete/<string:parkingstr>/', methods=['GET'])
def cycling2_delete(parkingstr):
    parkingid = parkingstr
    mainDanyce.processParkingDeleteDetails(parkingstr)
    flash("note edited")
    return redirect(url_for("parking_retrieve"))

@app.route('/cycling2_edit/<string:parkingstr>/', methods=['GET'])
def cycling2_edit(parkingstr):
    parkingid = parkingstr
    form = UpdateParkingForm(request.form)
    form.parkingid.data = parkingid
    print("Test 1")
    return render_template('cycling2update.html', session_userid=session['userid'], parkingid=parkingid, form=form)

@app.route('/cycling2_update_save', methods=['GET','POST'])
def cycling2_update_save(parkingstr):
    print("the method is" + request.method)
    form = UpdateParkingForm(request.form)

    if request.method == 'POST':
        if not form.validate():
            print("all fields are required")

        else:
            parkingid = form.parkingid.data
            parking = form.parking.data
            print("test cycling2_update_save >> ")
            print(parkingid)
            print(parking)
            print("test cycling2_update_save >> ")
            mainDanyce.processParkingUpdateDetails(parkingid,parking)
            flash("parking edited")
            return redirect(url_for("parking_retrieve"))
    return render_template('cycling2update.html', session_userid=session['userid'],form=form)





@app.route('/Parking_create', methods=['GET', 'POST'])
def Parking_create():
    print("Creating parking")
    station = "Bedok"
    location1 = "EW"
    image1 = "bedok.jpg"
    mainDanyce.createNewParking(session['userid'],location1, station, image1)

    print("Creating parking")
    station = "Aljunied"
    location2 = "EW"
    image1 = "aljunied.jpg"
    mainDanyce.createNewParking(session['userid'],location2, station, image1)

    print("Creating parking")
    station = "Expo"
    location3 = "EW"
    image1 = "expo.jpg"
    mainDanyce.createNewParking(session['userid'],location3, station, image1)

    print("Creating parking")
    station = "Jurong East"
    location4 = "NS/EW"
    image1 = "JE.jpg"
    mainDanyce.createNewParking(session['userid'], location4, station, image1)

    print("Creating parking")
    station = "Sembawang"
    location5 = "NS"
    image1 = "sembawang.jpg"
    mainDanyce.createNewParking(session['userid'],location5, station, image1)

    return redirect(url_for("parking_retrieve"))

@app.route('/parking_retrieve', methods=['GET', 'POST'])
def parking_retrieve():
    parkinglist = []
    form = Searchparking(request.form)
    parkinglist = mainDanyce.processAllParkings(session['userid'])
    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            station = form.location.data
            image1 = form.image1.data
            mainDanyce.createNewParking(session['userid'], station, image1)
            flash("Parking created")
            return redirect(url_for('parking_search'))
    return render_template('parkinglist.html', session_userid=session['userid'], parking=parkinglist,form=form, count=len(parkinglist))

@app.route("/parking_search",  methods=['GET', 'POST'])
def parking_search():
    form = Searchparking(request.form)
    parkinglist1 = []
    station = form.station.data
    parkinglist1 = mainDanyce.processAllParkingsStation(session["userid"],station)
    return render_template('parkingsearch.html', session_userid=session['userid'], parkinglist1=parkinglist1,form=form,count=len(parkinglist1))





@app.route('/Route_create', methods=['GET', 'POST'])
def Route_create():
    print("Creating route")
    destination = "Yio Chu Kang"
    location1 = "Bishan"
    image1 = "BYCK.PNG"
    mainDanyce.createNewRoute(session['userid'],location1, destination, image1)

    print("Creating route")
    destination = "Khatib"
    location2 = "Yew Tee"
    image1 = "KY.PNG"
    mainDanyce.createNewRoute(session['userid'],location2, destination, image1)

    print("Creating route")
    destination = "Promenade"
    location3 = "Kallang"
    image1 = "KP.PNG"
    mainDanyce.createNewRoute(session['userid'],location3, destination, image1)
    return redirect(url_for("route_retrieve"))

@app.route('/route_retrieve', methods=['GET', 'POST'])
def route_retrieve():
    routelist = []
    form = Searchroute(request.form)
    routelist = mainDanyce.processAllRoutes(session['userid'])
    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            location = form.location.data
            destination = form.destination.data
            image1 = form.image1.data
            mainDanyce.createNewRoute(session['userid'], location,destination, image1)
            flash("Parking created")
            return redirect(url_for('route_search'))
    return render_template('cycling1list.html', session_userid=session['userid'], route=routelist,form=form, count=len(routelist))

@app.route("/route_search",  methods=['GET', 'POST'])
def route_search():
    form = Searchroute(request.form)
    routelist1 = []
    location = form.location.data
    routelist1 = mainDanyce.processAllRouteslocation(session["userid"],location)
    return render_template('cycling1search.html', session_userid=session['userid'], route1=routelist1,form=form,count=len(routelist1))





@app.route('/Promotions_create', methods=['GET', 'POST'])
def Promotions_create():

    print('the method is ' + request.method)
    return render_template('cycling3create.html', session_userid=session['userid'])

@app.route('/promotion_retrieve')
def promotion_retrieve():
    promotionlist = []
    promotionlist = mainDanyce.processAllPromotion(session['userid'])
    return render_template('cycling3listing.html', session_userid=session['userid'], cycling3s=promotionlist, count=len(promotionlist))



#BUS DONE BY STEPHANIE


@app.route('/traffic')
def traffic():
        form = BusExpressway(request.form)
        return render_template('trafficcam.html', session_userid=session['userid'], form=form)


@app.route('/timingbus_create', methods=['GET', 'POST'])
def timingbus_create():
    form = CreateTimingbus(request.form)
    #sprint('hi')
    nlist = []
    nlist = mainSteph.processAllTimingbuss(session['userid']) # to find the number of timingbuss created

    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            timingbus = form.timingbus.data
            busno = form.busno.data
            busstopno = form.busstopno.data
            mainSteph.createNewTimingBus(session['userid'], timingbus,busno,busstopno)
            flash("timingbus created")
            return redirect(url_for('timingbus_retrieve'))
    return render_template('bustimingcreate.html', session_userid=session['userid'], form=form, count=len(nlist))


@app.route('/timingbus_retrieve')
def timingbus_retrieve():
    timingbuslist = []
    timingbuslist = mainSteph.processAllTimingbuss(session['userid'])
    return render_template('bustiminglisting.html', session_userid=session['userid'], timingbuss=timingbuslist, count=len(timingbuslist))


@app.route('/timingbus_update_status/<string:timingbusstr>/', methods=['GET', 'POST'])
def timingbus_update_status(timingbusstr):
    print('timingbusupdate >>' + timingbusstr)
    timingbusid = timingbusstr
    mainSteph.processTimingbusUpdateStatus(timingbusid)
    flash("timingbus status updated")
    timingbuslist = []
    timingbuslist = mainSteph.processAllTimingbuss(session['userid'])
    return render_template('bustiminglisting.html', session_userid=session['userid'], timingbuss=timingbuslist, count=len(timingbuslist))


@app.route('/timingbus_update_details/<string:timingbusstr>/', methods=['GET', 'POST'])
def timingbus_update_details(timingbusstr):
    print('timingbusupdate >>' + timingbusstr)
    timingbusid = timingbusstr
    form = UpdateTimingbus(request.form)
    return render_template('bustimingupdate.html', session_userid=session['userid'], form=form)


@app.route('/timingbus_viewer', methods=['GET', 'POST'])
def timingbus_viewer():
    form = TimingBusViewer(request.form)
    print('>>>>>!!!!!!@@@@@@@@@')
    print(form.busstopno.data)
    busstopno = form.busstopno.data
    if request.method == 'POST':
        timingbuslist = mainSteph.processSomeRecords1(busstopno)
        return render_template('bustiminglistingUser.html', session_userid=session['userid'], timingbuss=timingbuslist,
                           count=len(timingbuslist), busstopno = busstopno)

    return render_template('bustimingviewer.html', session_userid=session['userid'],form = form)

@app.route('/bus_delete/<string:deletestr>/', methods=['GET'])
def bus_delete(deletestr):
        timingbusid = deletestr
        print('>>>>>>>>>!!!!!!!')
        print(timingbusid)
        mainSteph.processTimingbusDeleteDetails(timingbusid)
        flash("note edited")
        return redirect(url_for('timingbus_retrieve'))



@app.route('/timinghospital_create', methods=['GET', 'POST'])
def timinghospital_create():
    form = CreateTiminghospital(request.form)
    #sprint('hi')
    nlist = []
    nlist = mainSteph.processAllTiminghospitals(session['userid']) # to find the number of timingbuss created

    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            fromhospital = form.fromhospital.data
            tohospital = form.tohospital.data
            hospital = form.hospital.data
            mainSteph.createNewTimingHospital(session['userid'], fromhospital,tohospital,hospital)
            flash("timinghospital created")
            return redirect(url_for('timinghospital_retrieve'))
    return render_template('hospitalcreate.html', session_userid=session['userid'], form=form, count=len(nlist))


@app.route('/timinghospital_retrieve')
def timinghospital_retrieve():
    timinghospitallist = []
    timinghospitallist = mainSteph.processAllTiminghospitals(session['userid'])
    return render_template('hospitallisting.html', session_userid=session['userid'], timinghospitals=timinghospitallist, count=len(timinghospitallist))

@app.route('/hospital_delete/<string:deletestr>/', methods=['GET'])
def hospital_delete(deletestr):
        timinghospitalid = deletestr
        print('>>>>>>>>>!!!!!!!')
        print(timinghospitalid)
        mainSteph.processTiminghospitalDeleteDetails(timinghospitalid)
        flash("note edited")
        return redirect(url_for('timinghospital_retrieve'))

@app.route('/timinghospital_viewer', methods=['GET', 'POST'])
def timinghospital_viewer():
    form = TimingHospitalViewer(request.form)
    print('>>>>>!!!!!!@@@@@@@@@')
    print(form.hospital.data)
    hospital = form.hospital.data
    if request.method == 'POST':
        timinghospitallist = mainSteph.processSomeRecords2(hospital)
        return render_template('hospitallistingUser.html', session_userid=session['userid'], timinghospitals=timinghospitallist,
                           count=len(timinghospitallist), hospital = hospital)

    return render_template('hospitalviewer.html', session_userid=session['userid'],form = form)




@app.route('/timingmall_create', methods=['GET', 'POST'])
def timingmall_create():
    form = CreateTimingmall(request.form)
    #sprint('hi')
    nlist = []
    nlist = mainSteph.processAllTimingmalls(session['userid']) # to find the number of timingbuss created

    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            frommall = form.frommall.data
            tomall = form.tomall.data
            mall = form.mall.data
            mainSteph.createNewTimingMall(session['userid'], frommall,tomall,mall)
            flash("timingmall created")
            return redirect(url_for('timingmall_retrieve'))
    return render_template('mallcreate.html', session_userid=session['userid'], form=form, count=len(nlist))


@app.route('/timingmall_retrieve')
def timingmall_retrieve():
    timingmalllist = []
    timingmalllist = mainSteph.processAllTimingmalls(session['userid'])
    return render_template('malllisting.html', session_userid=session['userid'], timingmalls=timingmalllist, count=len(timingmalllist))

@app.route('/mall_delete/<string:deletestr>/', methods=['GET'])
def mall_delete(deletestr):
        timingmallid = deletestr
        print('>>>>>>>>>!!!!!!!')
        print(timingmallid)
        mainSteph.processTimingmallDeleteDetails(timingmallid)
        flash("note edited")
        return redirect(url_for('timingmall_retrieve'))

@app.route('/timingmall_viewer', methods=['GET', 'POST'])
def timingmall_viewer():
    form = TimingMallViewer(request.form)
    print('>>>>>!!!!!!@@@@@@@@@')
    print(form.mall.data)
    mall = form.mall.data
    if request.method == 'POST':
        timingmalllist = mainSteph.processSomeRecords3(mall)
        return render_template('malllistingUser.html', session_userid=session['userid'], timingmalls=timingmalllist,
                           count=len(timingmalllist),mall=mall)

    return render_template('mallviewer.html', session_userid=session['userid'],form = form)


@app.route('/timingcondo_create', methods=['GET', 'POST'])
def timingcondo_create():
    form = CreateTimingcondo(request.form)
    #sprint('hi')
    nlist = []
    nlist = mainSteph.processAllTimingcondos(session['userid']) # to find the number of timingbuss created

    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            fromcondo = form.fromcondo.data
            tocondo = form.tocondo.data
            condo = form.condo.data
            mainSteph.createNewTimingCondo(session['userid'], fromcondo,tocondo,condo)
            flash("timingcondo created")
            return redirect(url_for('timingcondo_retrieve'))
    return render_template('condocreate.html', session_userid=session['userid'], form=form, count=len(nlist))


@app.route('/timingcondo_retrieve')
def timingcondo_retrieve():
    timingcondolist = []
    timingcondolist = mainSteph.processAllTimingcondos(session['userid'])
    return render_template('condolisting.html', session_userid=session['userid'], timingcondos=timingcondolist, count=len(timingcondolist))

@app.route('/condo_delete/<string:deletestr>/', methods=['GET'])
def condo_delete(deletestr):
        timingcondoid = deletestr
        print('>>>>>>>>>!!!!!!!')
        print(timingcondoid)
        mainSteph.processTimingcondoDeleteDetails(timingcondoid)
        flash("note edited")
        return redirect(url_for('timingcondo_retrieve'))

@app.route('/timingcondo_viewer', methods=['GET', 'POST'])
def timingcondo_viewer():
    form = TimingCondoViewer(request.form)
    print('>>>>>!!!!!!@@@@@@@@@')
    print(form.condo.data)
    condo = form.condo.data
    if request.method == 'POST':
        timingcondolist = mainSteph.processSomeRecords4(condo)
        return render_template('condolistingUser.html', session_userid=session['userid'], timingcondos=timingcondolist,
                           count=len(timingcondolist),condo=condo)

    return render_template('condoviewer.html', session_userid=session['userid'],form = form)





#DONE BY ANGELA

@app.route('/timing_create', methods=['GET', 'POST'])
def timing_create():
    form = CreateTimingForm(request.form)

    nlist = []
    nlist = mainAngela.processAllTimings(session['userid']) # to find the number of timings created

    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('test2')
            location = form.location.data
            destination = form.destination.data
            time = form.time.data
            mainAngela.createNewTiming(session['userid'], location, destination, time)
            flash("timing created")
            return redirect(url_for('timing_retrieve'))
    return render_template('timingcreate.html', session_userid=session['userid'], form=form, count=len(nlist))


@app.route('/timing_retrieve')
def timing_retrieve():
    timinglist = []
    timinglist = mainAngela.processAllTimings(session['userid'])
    return render_template('timinglisting.html', session_userid=session['userid'], timings=timinglist, count=len(timinglist))


@app.route('/MRT_exit')
def MRT_exit():
    print("Creating MRT exit")

    station = "Yew Tee Station"
    image1 = "yewtee_ns5D.jpg"
    image2 = "yewtee_ns5D.jpg"
    image3 = "yewtee_ns5D.jpg"
    image4 = "yewtee_ns5D.jpg"
    mainAngela.createNewExit(session["userid"], station, image1, image2, image3, image4)

    print("Creating MRT exit")
    station = "Yio Chu Kang"
    image1 = "yck.jpg"
    image2 = "yck.jpg"
    image3 = "yck.jpg"
    image4 = "yck.jpg"
    mainAngela.createNewExit(session["userid"], station, image1, image2, image3, image4)

    print("Creating MRT exit")
    station = "Esplanade"
    image1 = "esplanade_cc3.jpg"
    image2 = "esplanade_cc3.jpg"
    image3 = "esplanade_cc3.jpg"
    image4 = "esplanade_cc3.jpg"
    mainAngela.createNewExit(session["userid"], station, image1, image2, image3, image4)

    print("Creating MRT exit")
    station = "Dhoby Ghaut"
    image1 = "esplanade_cc3.jpg"
    image2 = "esplanade_cc3.jpg"
    image3 = "esplanade_cc3.jpg"
    image4 = "esplanade_cc3.jpg"
    mainAngela.createNewExit(session["userid"], station, image1, image2, image3, image4)

    return redirect(url_for('MRT_exit_retreive'))
    #return render_template('MRTexit.html', session_userid=session['userid'], form=form, count=len(nlist))



@app.route('/MRT_exit_retreive', methods=['GET', 'POST'])
def MRT_exit_retreive():
    exitlist = []
    form = Searchexit(request.form)
    exitlist = mainAngela.processAllExit(session['userid'])
    print('the method is ' + request.method)
    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.')
            station = form.station.data
            mrtexit = form.mrtexit.data
            image1 = form.image1.data
            image2 = form.image2.data
            image3 = form.image3.data
            image4 = form.image4.data
            mainAngela.createNewExit(session['userid'], station, mrtexit, image1, image2, image3, image4)
            flash("exit created")
            return redirect(url_for('MRT_exit_search'))
    return render_template('MRTexitlisting.html', session_userid=session['userid'], exits=exitlist, form=form, count=len(exitlist))


@app.route("/MRT_exit_search",  methods=['GET', 'POST'])
def MRT_exit_search():
    form = Searchexit(request.form)
    exitlist1 = []
    station = form.station.data
    print('!!!!!!!!!!!!!!!!!!!!!!!!!!1.')
    print(station)
    exitlist = mainAngela.processAllExitstation(session["userid"], station)
    return render_template('MRTexitlisting.html', session_userid=session['userid'], exits=exitlist, form=form, count=len(exitlist))


@app.route('/timing_update_status/<string:timingstr>/', methods=['GET', 'POST'])
def timing_update_status(timingstr):
    print('timingupdate >>' + timingstr)
    timingid = timingstr
    mainAngela.processTimingUpdateStatus(timingid)
    flash("timing status updated")
    timinglist = []
    timinglist = mainAngela.processAllTimings(session['userid'])
    return render_template('timinglisting.html', session_userid=session['userid'], timings=timinglist, count=len(timinglist))


@app.route('/timing_update_save', methods = ['GET', 'POST'])
def timing_update_save():
    print('the method is: ' + request.method)
    form = UpdateTimingForm(request.form)

    if request.method == 'POST':
        if not form.validate():
            print('all fields are required')
        else:
            timingid = form.timingid.data
            timing = form.timing.data
            print('test timing_update_save >>')
            print(timingid)
            print(timing)
            print('test note_update_save >>')
            mainAngela.processTimingUpdateDetails(timingid, timing)
            flash('timing edited')
            return redirect(url_for('timing_retrieve'))
    return render_template('timingupdate.html', session_userid = session['userid'], form = form)


@app.route('/timing_update_details/<string:timingstr>/', methods=['GET', 'POST'])
def timing_update_details(timingstr):
    print('timingupdate >>' + timingstr)
    timingid = timingstr
    form = UpdateTimingForm(request.form)
    timingid = form.timingid.data
    return render_template('timingupdate.html', session_userid=session['userid'], form=form, timingid = timingid)


@app.route('/timing_edit/<string:timingstr>/', methods = ['GET'])
def timing_edit(timingstr):
    timingid = timingstr
    form = UpdateTimingForm(request.form)
    form.timingid.data = timingid
    print('test1')
    return render_template('timingupdate.html', session_userid = session['userid'], timingid = timingid, form = form)


@app.route('/timing_delete/<string:timingstr>/', methods = ['GET'])
def timing_delete(timingstr):
    timingid = timingstr
    print('test1')
    mainAngela.processTimingDeleteDetails(timingid)
    flash("Timing edited")
    return redirect(url_for('timing_retrieve'))


if __name__ == '__main__':
    app.debug = True
    app.run()



# HTML form passes information from the front-end of our application(what our users see)
# through Flask,
# and to the back-end(our Python code).


