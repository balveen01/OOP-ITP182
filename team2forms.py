#DONE BY BALVEEN, DANYCE, RU MEI, LOW XUAN JIE AND ANGELA (DONE INDIVIDUALLY)
from wtforms import Form, StringField, TextAreaField, RadioField, SelectField, validators, PasswordField, SubmitField
from datetime import timedelta

#for bookings DONE BY BALVEEN
class CreateBookingForm(Form):

    destination = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    location = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    transportation = SelectField("", choices=[("Taxi", "Taxi"), ("Grab", "Grab"), ("Grab-hitch", "Grab-hitch")])
    time = SelectField("", choices = [("0800","08 00"),("0900","09 00"),("1000","10 00"),("1100","11 00"),("1200","12 00"),("1300","13 00"),("1400","14 00"),("1500","15 00"),("1600","16 00"),("1700","17 00"),("1800","18 00"),("1900","19 00"),("2000","20 00"),("2100","21 00")])

class Searchbooking(Form):
    search = StringField("", [validators.Length(min=1, max=150), validators.DataRequired()])
    #search = SelectField("",choices=[("Taxi", "Taxi"),("Grab", "Grab"), ("Grab-hitch","Grab-hitch")])

class UpdatebookingForm(Form):
    bookingid = StringField('')
    #booking = StringField("booking", [validators.Length(min=1, max=150), validators.DataRequired()])
    transportation = SelectField("", choices=[("Taxi", "Taxi"), ("Grab", "Grab"), ("Grab-hitch", "Grab-hitch")])
    timing = SelectField("", choices = [("0800","08 00"),("0900","09 00"),("1000","10 00"),("1100","11 00"),("1200","12 00"),("1300","13 00"),("1400","14 00"),("1500","15 00"),("1600","16 00"),("1700","17 00"),("1800","18 00"),("1900","19 00"),("2000","20 00"),("2100","21 00")])


#for taxi route DONE BY BALVEEN
class CreatetaxiRouteForm(Form):
    destination = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    location = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])


class SearchRoute(Form):
    search = StringField("", [validators.Length(min=1, max=150), validators.DataRequired()])

#for taxi camera DONE BY BALVEEN
class Searchcamera(Form):
    expressway = StringField("", [validators.Length(min=1, max=150), validators.DataRequired()])


#class Createtaxicameraform(FlaskForm):
    #expressway = SelectField("", choices=[("Please select the expressway", "Please select the expressway"),("AIE", "Ayer Rajah Expressway(AIE)"), ("BKE", "Bukit Timah Expressway(BKE)"),("CTE", "Centeral Expressway(CTE)"), ("ECP", "East Coast Parkway(ECP)"),("KPE", "Kallang-Paya Lebar Expressway(KPE)"),("KJE", "Kranji Expressway(KJE)"), ("MCE", "Marina Coastal Expressway(MCE)"),("PIE", "Pan-Island Expressway(PIE)"), ("SLE", "Seletar Expressway(SLE)"),("SG", "Sentosa Gateway"), ("TPE", "Tampines Expressway(TPE)"),("TC", "Tuas Checkpoint"), ("WC", "Woodlands Checkpoint")])
    #image1 = FileField()
    #image2 = FileField()



#for cycling DONE BY DANYCE
class CreateRouteForm(Form):
    location = StringField("", [validators.Length(min=1, max=150), validators.DataRequired()])
    destination = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])


class UpdateRouteForm(Form):
    routeid = StringField('')
    location = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    destination = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])



class CreateEWForm(Form):
    station = SelectField("", choices = [("Select an MRT station","Select an MRT station"),("Aljunied","Aljunied"),("Bedok","Bedok"),("Boon Lay","Boon Lay"),("Bugis","Bugis"),("Buona Vista","Buona Vista"),("Chinese Garden","Chinese Garden"),("Clementi","Clementi"),("Commonwealth","Commonwealth"),("Dover","Dover"),("Eunos","Eunos"),
                                         ("Expo","Expo"),("Gul Circle","Gul Circle"),("Joo Koon","Joo Koon"),("Jurong East","Jurong East"),("Kallang","Kallang"),("Kembangan","Kembangan"),("Lakeside","Lakeside"),("Lavender","Lavender"),("Outram Park","Outram Park"),
                                         ("Pasir Ris","Pasir Ris"),("Paya Lebar","Paya Lebar"),("Pioneer","Pioneer"),("Queenstown","Queenstown"),("Redhill","Redhill"),("Simei","Simei"),("Tampines","Tampines"),("Tanah Merah","Tanah Merah"),("Tiong Bahru","Tiong Bahru"),("Tuas Crescent","Tuas Crescent"),("Tuas Link","Tuas Link"),("Tuas West Road","Tuas West Road")])

class UpdateParkingForm(Form):
    parkingid = StringField('')
    parking = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])


class Createparkingform(Form):
    station = SelectField("", choices=[("Select an MRT station", "Select an MRT station"), ("Aljunied", "Aljunied"),
                                       ("Bedok", "Bedok"), ("Boon Lay", "Boon Lay"), ("Bugis", "Bugis"),
                                       ("Buona Vista", "Buona Vista"), ("Chinese Garden", "Chinese Garden"),
                                       ("Clementi", "Clementi"), ("Commonwealth", "Commonwealth"), ("Dover", "Dover"),
                                       ("Eunos", "Eunos"),
                                       ("Expo", "Expo"), ("Gul Circle", "Gul Circle"), ("Joo Koon", "Joo Koon"),
                                       ("Jurong East", "Jurong East"), ("Kallang", "Kallang"),
                                       ("Kembangan", "Kembangan"), ("Lakeside", "Lakeside"), ("Lavender", "Lavender"),
                                       ("Outram Park", "Outram Park"),
                                       ("Pasir Ris", "Pasir Ris"), ("Paya Lebar", "Paya Lebar"), ("Pioneer", "Pioneer"),
                                       ("Queenstown", "Queenstown"), ("Redhill", "Redhill"), ("Simei", "Simei"),
                                       ("Tampines", "Tampines"), ("Tanah Merah", "Tanah Merah"),
                                       ("Tiong Bahru", "Tiong Bahru"), ("Tuas Crescent", "Tuas Crescent"),
                                       ("Tuas Link", "Tuas Link"), ("Tuas West Road", "Tuas West Road")])


class Searchparking(Form):
    station = SelectField("", choices=[("Select an MRT station", "Select an MRT station"), ("Aljunied", "Aljunied"),
                                       ("Bedok", "Bedok"), ("Boon Lay", "Boon Lay"), ("Bugis", "Bugis"),
                                       ("Buona Vista", "Buona Vista"), ("Chinese Garden", "Chinese Garden"),
                                       ("Clementi", "Clementi"), ("Commonwealth", "Commonwealth"), ("Dover", "Dover"),
                                       ("Eunos", "Eunos"),
                                       ("Expo", "Expo"), ("Gul Circle", "Gul Circle"), ("Joo Koon", "Joo Koon"),
                                       ("Jurong East", "Jurong East"), ("Kallang", "Kallang"),
                                       ("Kembangan", "Kembangan"), ("Lakeside", "Lakeside"), ("Lavender", "Lavender"),
                                       ("Outram Park", "Outram Park"),
                                       ("Pasir Ris", "Pasir Ris"), ("Paya Lebar", "Paya Lebar"), ("Pioneer", "Pioneer"),
                                       ("Queenstown", "Queenstown"), ("Redhill", "Redhill"), ("Simei", "Simei"),
                                       ("Tampines", "Tampines"), ("Tanah Merah", "Tanah Merah"),
                                       ("Tiong Bahru", "Tiong Bahru"), ("Tuas Crescent", "Tuas Crescent"),
                                       ("Tuas Link", "Tuas Link"), ("Tuas West Road", "Tuas West Road")])


class Searchroute(Form):
    location = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])




#for MRT DONE BY ANGELA
class CreateTimingForm(Form):
    location = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    destination = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    time = RadioField('', choices=[('1330', '1330'), ('1430', '1430'), ('1530', '1530')], default='F')


class UpdateTimingForm(Form):
    timingid = StringField('')
    timing = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])


class Searchexit(Form):
    #station = SelectField("", choices=[('-- Select an MRT station --', '-- Select an MRT station --'),
                                       #('Yew Tee Station (NS5)', 'Yew Tee Station (NS5)'),
                                       #('Marsiling Station (NS8)', 'Marsiling Station (NS8)'),
                                       #('Yio Chu Kang Station (NS15)', 'Yio Chu Kang Station (NS15)'),
                                       #('Esplanade Station (CC3', 'Esplanade Station (CC3)'),
                                       #('Dhoby Ghaut Station (NS24 / CC1 / NE6)')])
    station = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])


#for bus DONE BY LOW XUAN JIE

class CreateTimingbus(Form):
    timingbus = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    busno =StringField(': ', [validators.Length(min=1, max=150), validators.DataRequired()])
    busstopno = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])

class UpdateTimingbus(Form):
    timingbusid = StringField(': ')
    timingbus = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])
    #busno =StringField('Bus No.', [validators.Length(min=1, max=150), validators.DataRequired()])

class TimingBusViewer(Form):
    busstopno = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])

class BusExpressway(Form):
    busexpressway = SelectField('',choices=[('Pan Island Expressway(PIE)'),('Ayer Rajah Expressway(AYE)'),('East Coast Parkway (ECP)'),('Sentosa Gateway'),('Central Expressway (CTE)'),('Tampines Expressway (TPE)'),('Kallang-Paya Lebar Expressway (KPE)'),('Seletar Expressway (SLE)'),('Bukit Timah Expressway (BKE)'),('Kranji Expressway (JKE)'),('Marina Coastal Expressway (MCE)'),('Tuas Checkpoint'),('Woodland Checkpoint')])


class CreateTiminghospital(Form):
    fromhospital = StringField('From Hospital: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    tohospital =StringField('To Hospital: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    hospital = StringField('Hospital: ', [validators.Length(min=1, max=150), validators.DataRequired()])
class TimingHospitalViewer(Form):
    hospital = StringField('', [validators.Length(min=1, max=150), validators.DataRequired()])

class CreateTimingmall(Form):
    frommall = StringField('From Mall: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    tomall =StringField('To Mall: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    mall = StringField('Mall: ', [validators.Length(min=1, max=150), validators.DataRequired()])

class TimingMallViewer(Form):
    mall = StringField(' ', [validators.Length(min=1, max=150), validators.DataRequired()])


class CreateTimingcondo(Form):
    fromcondo = StringField('From Condominium: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    tocondo =StringField('To Condominium: ', [validators.Length(min=1, max=150), validators.DataRequired()])
    condo = StringField('Condominium: ', [validators.Length(min=1, max=150), validators.DataRequired()])

class TimingCondoViewer(Form):
    condo = StringField(' ', [validators.Length(min=1, max=150), validators.DataRequired()])

# for walking
class Searchwalking(Form):
    location = StringField(' ', [validators.Length(min=1, max=150), validators.DataRequired()])
