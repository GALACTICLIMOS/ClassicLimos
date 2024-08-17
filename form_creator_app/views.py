from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.conf import settings
filename = None
def index(request):
    return render(request, 'index.html')
def limohireservices(request):
    return render(request, 'limo-hire-services.html')


def fleet(request):
    return render(request, 'Fleet.html')
def KIDSLIMOPARTIES(request):
    return render(request, 'KIDSLIMOPARTIES.html')
def PROMLIMO(request):
    return render(request, 'PROMLIMO.html')
def ROYALASCOTLIMOHIRE(request):
    return render(request, 'ROYAL_ASCOT_LIMO_HIRE.html')
def SPECIALOCCASIONLIMOHIRE(request):
    return render(request, 'SPECIAL_OCCASION_LIMO HIRE.html')
def weddingcarhire(request):
    return render(request, 'wedding-car-hire.html')
#Fleet  funtion start
def SEATLUXURYCARS(request):
    return render(request, 'SEATLUXURYCARS.html')
def eSEATSTRETCHLIMOS(request):
    return render(request, 'eSEATSTRETCHLIMOS.html')
def sSEATSTRETCHLIMOS(request):
    return render(request, 'sSEATSTRETCHLIMOS.html')
def SEATPARTYBUSES(request):
    return render(request, 'SEATPARTYBUSES.html')

def OFFERS(request):
    return render(request, 'OFFERS.html')
def QUOTES(request):
    return render(request, 'new_quotes.html')
def CONTACT(request):
    return render(request, 'CONTACT.html')
def Reservation(request):
    render(request, 'reservationform.html')


def Reservation_form(request):
 
    if request.method == 'POST':
            
        print("saving reservation form")
        first_name = request.POST['First_Name']
        last_name  = request.POST['Last_Name']
        phone_num  = request.POST['phone']
        email  = request.POST['email']
        pick_up_address  = request.POST['Pick_Up_Address']
        drop_off_Address  = request.POST['Drop_off_Address']
        city  = request.POST['City']
        zipcode  = request.POST['Zipcode']
        pick_up_Date  = request.POST['Pick_up_Date']
        pick_Up_Time  = request.POST['Pick_Up_Time']
        stop_En_Route  = request.POST['Stop_En_Route']
        number_of_Hours  = request.POST['Number_of_Hours']
        no_of_Passengers  = request.POST['No_of_Passangers']
        select_Vehicle  = request.POST['Select_Vehicle']
        routing_Request  = request.POST['RoutingRequest']
        first_Name_credit_card  = request.POST['First_name_credit_card']
        last_Name_credit_card  = request.POST['Last_Name_credit_card']
        credit_card_Number  = request.POST['Credit_card_Number']
        month_Year  = request.POST['Month_Year']
        Digit3_cvvifAMEX  = request.POST['digit3_cvvifAMEX']
        billing_Address  = request.POST['Billing_Address']

        try:
            s = RESERVATION_FORM.objects.create(first_name=first_name, last_name=last_name, phone_num=phone_num, email=email, pick_up_address=pick_up_address, drop_off_Address=drop_off_Address , city=city, zipcode=zipcode, pick_up_Date=pick_up_Date, pick_Up_Time=pick_Up_Time, stop_En_Route=stop_En_Route, number_of_Hours=number_of_Hours, no_of_Passengers=no_of_Passengers, select_Vehicle=select_Vehicle, routing_Request=routing_Request, first_Name_credit_card=first_Name_credit_card, last_Name_credit_card=last_Name_credit_card, credit_card_Number=credit_card_Number, month_Year=month_Year, Digit3_cvvifAMEX=Digit3_cvvifAMEX,billing_Address=billing_Address)
            s.save()
            print("Reservation form data saved to db.")
        except Exception as e:
            print(e)
            print("Error in saving reservation data to database.")

        try:
            details_dict  = {'filename':filename,'first_name':first_name,'last_name':last_name,'phone_num':phone_num,'email':email,'pick_up_address':pick_up_address,'drop_off_Address':drop_off_Address,'city':city,'zipcode':zipcode,'pick_up_Date':pick_up_Date,'pick_Up_Time':pick_Up_Time,'stop_En_Route':stop_En_Route,'number_of_Hours':number_of_Hours,'no_of_Passengers':no_of_Passengers,'selected_vehicle':select_Vehicle,'routing_Request':routing_Request,'first_Name_credit_card':first_Name_credit_card,'last_Name_credit_card':last_Name_credit_card,'credit_card_Number':credit_card_Number,'month_Year':month_Year,'Digit3_cvvifAMEX':Digit3_cvvifAMEX,'billing_Address':billing_Address}
            send_godaddyMAil_reservation_form(details_dict)
            print("mail sent succesfully.")
            return render(request,'sent_message.html')
            # return redirect('/')
        except Exception as e:
            print(e)
            print("There was an error in sending mail.")
        
        return render(request,'ErrorFaced.html')
    return render(request, 'reservationform.html')

def send_godaddyMAil_reservation_form(data):
    # try:
            
    import os
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.image import MIMEImage

    msg = MIMEMultipart()
    msg['Subject'] = "Reservation Request!"
    msg['From'] = "Info@vipclasslimos.com"
    msg['To'] = "Info@vipclasslimos.com"
    # msg['To'] = "asif5955iqbal@yahoo.com"

    # Add the logo to the message object
    # with open(logo_path, 'rb') as f:
    #     logo_data = f.read()
    # logo = MIMEImage(logo_data)
    # logo.add_header('Content-ID', '<logo>')
    # msg.attach(logo)

    # Create the HTML version of the email body
    html_body = f"""\
    <html>
    <body>
        <p>A Reservation Request has been received. Details are as following:</p>
        <ul>
        <li>First Name: {data['first_name']}</li>
        <li>Last Name: {data['last_name']}</li>
        <li>Phone No: {data['phone_num']}</li>
        <li>Mail: {data['email']}</li>
        <li>Pickup Address: {data['pick_up_address']}</li>
        <li>Drop off Address: {data['drop_off_Address']}</li>
        <li>City: {data['city']}</li>
        <li>Zipcode: {data['zipcode']}</li>
        <li>Pick up Date: {data['pick_up_Date']}</li>
        <li>Pick Up Time: {data['pick_Up_Time']}</li>
        <li>Stop En Route: {data['stop_En_Route']}</li>
        <li>Number of Hours: {data['number_of_Hours']}</li>
        <li>No. of passengers: {data['no_of_Passengers']}</li>
        
        <li>Selected Vehicle: {data['selected_vehicle']}</li>
        <li>Routing Request: {data['routing_Request']}</li>
        <p>Billing Information is as following</p>
        <li>First Name (as per on card): {data['first_Name_credit_card']}</li>
        <li>Last Name (as per on card): {data['last_Name_credit_card']}</li>
        <li>Credit Card Number: {data['credit_card_Number']}</li>
        <li>Month/Year: {data['month_Year']}</li>
        <li>3 Digit CVV: {data['Digit3_cvvifAMEX']}</li>
        <li>Billing Address: {data['billing_Address']}</li>
        </ul>
      
       <h2>Terms and Condition</h2>
        
        <p>Thank you for reserving VIP CLASS LIMO'S for quality assurance please review your 
        reservation for proper dates, addresses and times. It is up to you to inform us of
        any corrections this is not VIP CLASS LIMO'S  responsibility. In case of any question 
        call us at (888)383-3911. 100 non-refundable payment is expected when the reservation
        is made. All payments are non-refundable and non-transferable in any case of cancellation.
        Cancellations must be submitted in writing, via email. Remaining payments Must be Paid 30 
       days before reservation date and will be charged on card on file automatically. Reply to 
       this email to constitute your acceptance of these terms via email. Cancellation requests must
       be done in writing via email to Info@vipclasslimos.com
       Thank you.</p
        <p>Overtime R 10 Minute Grace Period Is Allowed. All overtime will be charged to the
        same credit card. we use for booking. Overtime is charged by the hour not prorated 
        per minute and will be charged same rate as per signed contract per hour rates 
        at the time of booking. Credit card onfile will be charged, prior to the event date, 
        for overtime and damages deposit. Security deposit will be refunded upon completion
        of the trip after inspection of the vehicle if there is no overtime and damages 
        refund will be processed in 3 to 4 working days. In the event we have another
        engagement after your service, there is no guarantee that VIP CLASS LIMO'S  Will 
        be available for overtime hours beyond your contracted time block. We reserve
        the right to conclude services at any moment once the contractual period has 
        expired. We do not intend to be tardy on your service help us to be on time for our 
        next Trip. If you feel you need more time, please book in advance and we will gladly 
        accommodate to our best ability. Payment Accep We accept all major Credit Cards and 
        Cash payments. If paying by check, it must clear 7 days before your services date .
        Cardholder Acceptance: I read the contract and I accept the VIP CLASS LIMO'S  terms
        and conditions, and I understand All payments are non-refundable in any case of cancelation.</p>

        <h3>Traffic Congestion:</h3>

        <p>Stops and Addresses Listed on your contract all addresses must be provided in advance,
        VIP CLASS LIMO'S  will not be held responsible for time lost mapping new addresses
        or trying to find landmarks. Please list all addresses in advance to ensure quality
        mapping and routing.  Note Any Tolls On the road customer must pay. It is agreed and
        understood that VIP CLASS LIMO'S  shall not be held liable or responsible for
        delays in traffic, roadblocks, alternative route delays or because of the misdirection
        of the driver by passengers. Delays for inclement weather shall also be the responsibility
        of the contracted VIP CLASS LIMO'S  does not offer credits during traffic delays,
        please allow extra time for travel if you feel it is necessary. Please consider your
        times carefully when booking or choosing a lengthier package.</p>

        <h1>Weather Policy</h1>
        <p>VIP CLASS LIMO'S  rentals reserves the right to suspend service if weather is inclement
        and could jeopardize safety. In these instances, a rain & Snow date will be allowed for
        the customer to choose a future date. All deposits will be Hold for future date.</p>

        <h3>VEHICLE DAMAGE POLICY</h3>
        <p>The Agreeing guarantor of this reservation accepts full financial liability for any physical
        damage or breakage of crystal, switches, burn marks, stains etc. Escape Hatches are for
        emergencies only. VIP CLASS LIMO'S  rental reserves the right to terminate service with
        no refund to client if clients renting service act in disorderly or violent manner. VIP CLASS LIMO'S 
        reserves the right to initiate legal collection proceedings for loss of service or damage
        fees that are not fully paid within 14 days past date of service and will bill for any and all
        attorneys’ fees, collection expenses and court costs incurred.</p>

        <h3>SMOKING/ALCOHOL POLICY</h3>
        <p>Our Vehicles are non-smoking. A $ 250.00 charge per occurrence will apply. If needed, your driver
        will pull over to allow passengers to smoke outside Limousine. Illegal use of drugs is prohibited
        in our limousines and can terminate ride at no refund to customer. Alcohol consumption in our
        vehicle is not permissible if any passenger on board is under the age of 21, alcohol must not be
        present during these instances or services may be terminated. In the event of illness,
        a minimum $350.00 clean-up will apply for steam cleaning and detailing all bodily fluids.</p>

        <h3>PASSENGER COUNT</h3
        <p>No chauffeur will operate a vehicle with more passengers than the vehicle is rated to accommodate.
        Please ensure the vehicle you are renting will accommodate your passenger count.</p>

        <h3>GENERAL ADDITIONAL POLICY</h3>
            <p>If for any reason the firm is unable to perform the service as contract,
            its maximum liability shall be limited to a full refund of any monies paid 
            by customers toward their rental or a credit towards future service. In rare 
            instances we reserve the right to substitute vehicles in the event of mechanical 
            failure. In the event of mechanical failure, VIP CLASS LIMO'S  rentals reserves 
            the right to make a comparable substitution. In the event we have advance 
            notice of a vehicle being taken out of service, we will contact you and 
            advise you of available options. If a vehicle becomes disabled in the route 
            to your service, we will send a comparable substitution at no extra charge to you. 
            It is agreed that no person shall cause any contracted vehicle to be overloaded past 
            the passenger capacity of any contracted vehicle. It is further understood that
            all passengers should discharge themselves from the vehicle orderly and should 
            check for personal items before departing the contracted vehicle.
            VIP CLASS LIMO'S shall not be responsible for any items left in a contracted vehicle.
            It is your responsibility to check the vehicle for personal items.
            The contracting person agrees that all claims and or complaints
            must be submitted in writing to VIP CLASS LIMO'S  rentals no later than 
            7days after the scheduled event. Moreover, should it be deemed necessary
            for VIP CLASS LIMO'S  to enlist attorneys or collection agencies to assist in 
            collection of monies due for non-payment of services or a breach of this contract,
            it shall be at the expense of the contracted event. Failure to comply with any 
            or all terms and conditions of this contract may result in termination of your ride,
            forfeiture of all payments and deposits the contracted event acknowledges that upon,
            reading and understanding the terms and conditions of this contract, 
            hereby agrees by signing this contract. Chauffeurs have the authority 
            to determine if vehicles can safely make tight turns or enter narrow
            driveways, in such instance’s clients may need to walk to or from the vehicle. 
            For your safety, walking or standing in the vehicle is prohibited while in motion.
            VIP CLASS LIMO'S  will not be held liable for injury sustained if limousine must 
            come to an immediate stop.</p>
            <h3>Note</h3>
           <p style="color: white; background-color: orange;">Card holder Acceptance: I read the contract and I accept all
           VIP CLASS LIMO'S  rentals terms and conditions and I understand All payments are non refundable.</p>
    
        <p></p>
        <p>Thank you.</p>
        
    </body>
    </html>
    """
    # Add the HTML version of the email body to the message object
    msg.attach(MIMEText(html_body, 'html'))

    # Connect to the SMTP server
    smtp_server = "smtpout.secureserver.net"

    smtp_port = 465  # Use port 465 for SSL encryption


    server = smtplib.SMTP_SSL(smtp_server, smtp_port)
    username = "Info@vipclasslimos.com"
    password = 'Marksmith@30047'
    server.login(username, password)

    # Send the email
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    # Disconnect from the server
    server.quit()
    print('successufully sent reservation_form email.')



# def Get_Quick_Quote_method(request):

#     Name = request.POST['Name']
#     email = request.POST['email']
#     Phone = request.POST['Phone']
#     Pick_Location = request.POST['Pick_Location']
#     Drop_Location = request.POST.get('Drop_Location')
#     Select_Vehicle = request.POST.get('Select_Vehicle')
#     No_of_Passengers = request.POST['No_of_Passengers']
#     No_of_Hours = request.POST['No_of_Hours']
#     Trip_Type = request.POST['Trip_Type']
#     Pickup_Date = request.POST['Pickup_Date']
#     Pickup_Time = request.POST['Pickup_Time']
#     print('Name', Name)
#     print('email', email)
#     print('Phone', Phone)
#     print('Pick_Location', Pick_Location)
#     print('Drop_Location', Drop_Location)
#     print('Select_Vehicle', Select_Vehicle)
#     print('No_of_Passengers', No_of_Passengers)
#     print('No_of_Hours', No_of_Hours)
#     print('Trip_Type', Trip_Type)
#     print('Pickup_Date', Pickup_Date)
#     print('Pickup_Time', Pickup_Time)
#     G = Get_Quick_Quote.objects.create(Name = Name, email = email, Phone = Phone, Pick_Location = Pick_Location, Drop_Location = Drop_Location, Select_Vehicle = Select_Vehicle, No_of_Passengers = No_of_Passengers, No_of_Hours = No_of_Hours, Trip_Type = Trip_Type , Pickup_Date = Pickup_Date , Pickup_Time = Pickup_Time )
#     G.save()
#     return redirect('index')




def Get_Quick_Quote_method(request):
    try:
        
        Name = request.POST['Name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        Pick_Location = request.POST['Pick_Location']
        Drop_Location = request.POST['Drop_Location']
        Select_Vehicle = request.POST['Select_Vehicle']
        No_of_Passengers = request.POST['No_of_Passengers']
        No_of_Hours = request.POST['No_of_Hours']
        Trip_Type = request.POST['Trip_Type']
        Pickup_Date = request.POST['Pickup_Date']
        Pickup_Time = request.POST['Pickup_Time']
        print('Name', Name)
        print('email', email)
        print('Phone', Phone)
        print('Pick_Location', Pick_Location)
        print('Drop_Location', Drop_Location)
        print('Select_Vehicle', Select_Vehicle)
        print('No_of_Passengers', No_of_Passengers)
        print('No_of_Hours', No_of_Hours)
        print('Trip_Type', Trip_Type)
        print('Pickup_Date', Pickup_Date)
        print('Pickup_Time', Pickup_Time)
        G = Get_Quick_Quote.objects.create(Name = Name, email = email, Phone = Phone, Pick_Location = Pick_Location, Drop_Location = Drop_Location, Select_Vehicle = Select_Vehicle, No_of_Passengers = No_of_Passengers, No_of_Hours = No_of_Hours, Trip_Type = Trip_Type , Pickup_Date = Pickup_Date , Pickup_Time = Pickup_Time )
        G.save()
        try:
            details_dict = {'Name':Name,'email':email,'Phone':Phone,'Pick_Location':Pick_Location,'Drop_Location':Drop_Location,'Select_Vehicle':Select_Vehicle,'No_of_Passengers':No_of_Passengers,'No_of_Hours':No_of_Hours,'Trip_Type':Trip_Type,'Pickup_Date':Pickup_Date,'Pickup_Time':Pickup_Time}
            send_godaddyMAil_quotation(details_dict)
            print("Get_Quick_Quote_method mail sent succesfully.")
        except Exception as e:
            print(e)
            print("There was an error in sending Get_Quick_Quote_method mail.")
        print("Form submitted.")
        # return render(request,'OrderPlaced.html')
        
        return redirect('index')
    except Exception as e:
        print(e)
        return redirect('index')

def send_godaddyMAil_quotation(data):
    try:
            
        import smtplib
        from email.mime.text import MIMEText
        msg = MIMEText(" A Quote Request has been received.\n\n"
                "Name: {Name}\n"
                "Email: {email}\n"
                "Phone No.: {Phone}\n"
                "Pick Location: {Pick_Location}\n"
                "Drop_Location: {Drop_Location}\n"
                "Select Vehicle: {Select_Vehicle}\n"
                "No. of Passengers: {No_of_Passengers}\n"
                "No. of Hours: {No_of_Hours}\n"
                "Trip Type: {Trip_Type}\n"
                "Pickup Date: {Pickup_Date}\n"
                "Pickup Time: {Pickup_Time}\n\n"

                "Thank you.".format(**data))
        
        # msg.set_content("Order details are as following:\n"+str(data)+'\n Thank you.')
        msg['Subject'] = "Quote Request!"
        msg['From'] = "Info@vipclasslimos.com"
        msg['To'] = "Info@vipclasslimos.com"

        # Connect to the SMTP server
        smtp_server = "smtpout.secureserver.net"
        smtp_port = 465 # Use port 465 for SSL encryption
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        username = "Info@vipclasslimos.com"
        password = 'Marksmith@30047'
        # password = settings.Mail_password
        server.login(username, password)

        # Send the email
        server.send_message(msg)

        # Disconnect from the server
        server.quit()
        print("Quotation sent to admin")
        return redirect('index')
    except Exception as e:
        print(e)
        return redirect('index')
    
def Message_send(request):
    return render(request, 'sent_message.html')




# signature pad

from django.conf import settings
from django.core.mail import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import smtplib
import os
import base64
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def send_email1234(request):
    uploaded_signature_url = None
    if request.method == 'POST':
        # Create a multipart message
        msg = MIMEMultipart()
        msg['Subject'] = "Reservation Request!"
        msg['From'] = "Info@vipclasslimos.com"
        msg['To'] = "Info@vipclasslimos.com"
        first_name = request.POST['First_Name']
        last_name  = request.POST['Last_Name']
        phone_num  = request.POST['phone']
        email  = request.POST['email']
        pick_up_address  = request.POST['Pick_Up_Address']
        drop_off_Address  = request.POST['Drop_off_Address']
        city  = request.POST['City']
        zipcode  = request.POST['Zipcode']
        pick_up_Date  = request.POST['Pick_up_Date']
        pick_Up_Time  = request.POST['Pick_Up_Time']
        stop_En_Route  = request.POST['Stop_En_Route']
        number_of_Hours  = request.POST['Number_of_Hours']
        no_of_Passengers  = request.POST['No_of_Passangers']
        select_Vehicle  = request.POST['Select_Vehicle']
        routing_Request  = request.POST['RoutingRequest']
        first_Name_credit_card  = request.POST['First_name_credit_card']
        last_Name_credit_card  = request.POST['Last_Name_credit_card']
     
        credit_card_Number  = request.POST['Credit_card_Number']
        month_Year  = request.POST['Month_Year']
        Digit3_cvvifAMEX  = request.POST['digit3_cvvifAMEX']
        billing_Address  = request.POST['Billing_Address']
        print('first_name', first_name)
        print('last_name', last_name)

        # Add your email message text here
        message_text = f"""
        
        <html>
        <body>
        <h3> --- RESERVATION FORM --- </h3>
        
        Frist Name :{first_name}
        last Name  :{last_name}
        Phone Number   :{phone_num}
        Email   :{email}
        Pick up address :{pick_up_address}
        Drop off Address  :{drop_off_Address}
        City   :{city}
        zipcode   :{zipcode}
        pick_up_Date :{pick_up_Date}
        pick_Up_Time  :{pick_Up_Time}
        stop_En_Route   :{stop_En_Route}
        number_of_Hours   :{ number_of_Hours}
        no_of_Passengers :{no_of_Passengers}
        select_Vehicle   :{select_Vehicle }
        routing_Request   :{routing_Request}
        
        ---Billing Information---
        
        first_Name_credit_card  :{first_Name_credit_card}
        last_Name_credit_card :{last_Name_credit_card}
        credit_card_Number    :{credit_card_Number }
        month_Year   :{ month_Year}
        Digit3_cvvifAMEX :{Digit3_cvvifAMEX}
        billing_Address :{billing_Address}


        Terms and Condition
        
        Thank you for reserving VIP CLASS LIMO for quality assurance please review your 
        reservation for proper dates, addresses and times. It is up to you to inform us of
        any corrections this is not VIP CLASS  LIMO responsibility. In case of any question 
        call us at (888)383-3911. 100 non-refundable payment is expected when the reservation
        is made. All payments are non-refundable and non-transferable in any case of cancellation.
        Cancellations must be submitted in writing, via email. Remaining payments Must be Paid 30 
       days before reservation date and will be charged on card on file automatically. Reply to 
       this email to constitute your acceptance of these terms via email. Cancellation requests must
       be done in writing via email to Info@vipclasslimos.com
       Thank you.
        Overtime R 10 Minute Grace Period Is Allowed. All overtime will be charged to the same credit card. we use for booking. Overtime is charged by the hour not prorated per minute and will be charged same rate as per signed contract per hour rates at the time of booking. Credit card onfile will be charged, prior to the event date, for overtime and damages deposit. Security deposit will be refunded upon completion of the trip after inspection of the vehicle if there is no overtime and damages refund will be processed in 3 to 4 working days. In the event we have another engagement after your service, there is no guarantee that  VIP CLASS LIMO'S  Will be available for overtime hours beyond your contracted time block. We reserve the right to conclude services at any moment once the contractual period has expired. We do not intend to be tardy on your service help us to be on time for our next Trip. If you feel you need more time, please book in advance and we will gladly accommodate to our best ability. Payment Accep We accept all major Credit Cards and Cash payments. If paying by check, it must clear 7 days before your services date . Cardholder Acceptance: I read the contract and I accept the VIP CLASS LIMO'S terms and conditions, and I understand All payments are non-refundable in any case of cancelation.

        Traffic Congestion:

        Stops and Addresses Listed on your contract all addresses must be provided in advance,
        VIP CLASS LIMO'S will not be held responsible for time lost mapping new addresses
        or trying to find landmarks. Please list all addresses in advance to ensure quality
        mapping and routing.  Note Any Tolls On the road customer must pay. It is agreed and
        understood that  VIP CLASS LIMO'S  shall not be held liable or responsible for
        delays in traffic, roadblocks, alternative route delays or because of the misdirection
        of the driver by passengers. Delays for inclement weather shall also be the responsibility
        of the contracted  VIP CLASS LIMO'S  does not offer credits during traffic delays,
        please allow extra time for travel if you feel it is necessary. Please consider your
        times carefully when booking or choosing a lengthier package.

        Weather Policy
         VIP CLASS LIMO'S  rentals reserves the right to suspend service if weather is inclement
        and could jeopardize safety. In these instances, a rain & Snow date will be allowed for
        the customer to choose a future date. All deposits will be Hold for future date.

        VEHICLE DAMAGE POLICY
        The Agreeing guarantor of this reservation accepts full financial liability for any physical
        damage or breakage of crystal, switches, burn marks, stains etc. Escape Hatches are for
        emergencies only.  VIP CLASS LIMO'S  rental reserves the right to terminate service with
        no refund to client if clients renting service act in disorderly or violent manner.  VIP CLASS LIMO'S 
        reserves the right to initiate legal collection proceedings for loss of service or damage
        fees that are not fully paid within 14 days past date of service and will bill for any and all
        attorneys’ fees, collection expenses and court costs incurred.

        SMOKING/ALCOHOL POLICY
        Our Vehicles are non-smoking. A $ 250.00 charge per occurrence will apply. If needed, your driver
        will pull over to allow passengers to smoke outside Limousine. Illegal use of drugs is prohibited
        in our limousines and can terminate ride at no refund to customer. Alcohol consumption in our
        vehicle is not permissible if any passenger on board is under the age of 21, alcohol must not be
        present during these instances or services may be terminated. In the event of illness,
        a minimum $350.00 clean-up will apply for steam cleaning and detailing all bodily fluids.

        PASSENGER COUNT
        No chauffeur will operate a vehicle with more passengers than the vehicle is rated to accommodate.
        Please ensure the vehicle you are renting will accommodate your passenger count.

        GENERAL ADDITIONAL POLICY
            If for any reason the firm is unable to perform the service as contract, its maximum liability shall be limited to a full refund of any monies paid by customers toward their rental or a credit towards future service. In rare instances we reserve the right to substitute vehicles in the event of mechanical failure. In the event of mechanical failure,  VIP CLASS LIMO'S  rentals reserves the right to make a comparable substitution. In the event we have advance notice of a vehicle being taken out of service, we will contact you and advise you of available options. If a vehicle becomes disabled in the route to your service, we will send a comparable substitution at no extra charge to you. It is agreed that no person shall cause any contracted vehicle to be overloaded past the passenger capacity of any contracted vehicle. It is further understood that all passengers should discharge themselves from the vehicle orderly and should check for personal items before departing the contracted vehicle.  VIP CLASS LIMO'S  shall not be responsible for any items left in a contracted vehicle. It is your responsibility to check the vehicle for personal items. The contracting person agrees that all claims and or complaints must be submitted in writing to  VIP CLASS LIMO'S  rentals no later than 7days after the scheduled event. Moreover, should it be deemed necessary for  VIP CLASS LIMO'S  to enlist attorneys or collection agencies to assist in collection of monies due for non-payment of services or a breach of this contract, it shall be at the expense of the contracted event. Failure to comply with any or all terms and conditions of this contract may result in termination of your ride, forfeiture of all payments and deposits the contracted event acknowledges that upon, reading and understanding the terms and conditions of this contract, hereby agrees by signing this contract. Chauffeurs have the authority to determine if vehicles can safely make tight turns or enter narrow driveways, in such instance’s clients may need to walk to or from the vehicle. For your safety, walking or standing in the vehicle is prohibited while in motion.  VIP CLASS LIMO'S  will not be held liable for injury sustained if limousine must come to an immediate stop.
                    """
        print(message_text)
        msg.attach(MIMEText(message_text, 'plain'))
        signature_data = 'Umer'
        # Get the signature data from the hidden input field
        signature_data = request.POST.get('signature_data')
        print('signature_data', signature_data)

        if signature_data:
            # Attach the signature image to the email
            signature = MIMEImage(base64.b64decode(signature_data.split(',')[1]), 'png')
            signature.add_header('Content-Disposition', 'attachment', filename='signature.png')
            msg.attach(signature)

            # Set the uploaded_signature_url to the URL of the temporary signature image
            uploaded_signature_url = settings.MEDIA_URL + 'temp_signature.png'
            obj = smtplib.SMTP_SSL("smtpout.secureserver.net", 465)

            # Authentication
            username = "Info@vipclasslimos.com"
            password = 'Marksmith@30047'
            obj.login(username, password)

            # Sending the email
            obj.sendmail(msg['From'], msg['To'], msg.as_string())

            # Quit the server
            obj.quit()
        print('signature successufully sent reservation_form email.')    

        # Rest of your email sending code...

        return render(request, 'msgsndsuccessfully.html', {'email_sent': True, 'uploaded_signature_url': uploaded_signature_url})

    return render(request, 'reservationform.html', {'uploaded_signature_url': uploaded_signature_url})

    

def send_email(request):
    uploaded_signature_url = ''

    if request.method == 'POST':
        try:
            # Create a multipart message
            msg = MIMEMultipart()
            msg['Subject'] = "Reservation Request!"
            msg['From'] = "Info@vipclasslimos.com"
            msg['To'] = "Info@vipclasslimos.com"
            
            first_name = request.POST['First_Name']
            print('first_name',first_name)
            last_name  = request.POST['Last_Name']
            print('last_name',last_name)
            phone_num  = request.POST['phone']
            print('phone_num',phone_num)
            
            email  = request.POST['email']
            pick_up_address  = request.POST['Pick_Up_Address']
            drop_off_Address  = request.POST['Drop_off_Address']
            city  = request.POST['City']
            zipcode  = request.POST['Zipcode']
            pick_up_Date  = request.POST['Pick_up_Date']
            pick_Up_Time  = request.POST['Pick_Up_Time']
            stop_En_Route  = request.POST['Stop_En_Route']
            number_of_Hours  = request.POST['Number_of_Hours']
            no_of_Passengers  = request.POST['No_of_Passangers']
            select_Vehicle  = request.POST['Select_Vehicle']
            routing_Request  = request.POST['RoutingRequest']
            first_Name_credit_card  = request.POST['First_name_credit_card']
            last_Name_credit_card  = request.POST['Last_Name_credit_card']
        
            credit_card_Number  = request.POST['Credit_card_Number']
            month_Year  = request.POST['Month_Year']
            Digit3_cvvifAMEX  = request.POST['digit3_cvvifAMEX']
            billing_Address  = request.POST['Billing_Address']
                # Your email message text here
            message_text = """
                    
        <html>
        <body>
        
        <h3>RESERVATION FORM</h3>
    <li>First Name: {first_name}</li>
    <li>Last Name: {last_name}</li>
    <li>Phone Number: {phone_num}</li>
    <li>Email: {email}</li>
    <li>Pick up address: {pick_up_address}</li>
    <li>Drop off Address: {drop_off_Address}</li>
    <li>City: {city}</li>
    <li>zipcode: {zipcode}</li>
    <li>pick_up_Date: {pick_up_Date}</li>
    <li>pick_Up_Time: {pick_Up_Time}</li>
    <li>stop_En_Route: {stop_En_Route}</li>
    <li>number_of_Hours: {number_of_Hours}</li>
    <li>no_of_Passengers: {no_of_Passengers}</li>
    <li>select_Vehicle: {select_Vehicle}</li>
    <li>routing_Request: {routing_Request}</li>

    <h3>Billing Information</h3>

    <li>first_Name_credit_card: {first_Name_credit_card}</li>
    <li>last_Name_credit_card: {last_Name_credit_card}</li>
    <li>credit_card_Number: {credit_card_Number}</li>
    <li>month_Year: {month_Year}</li>
    <li>Digit3_cvvifAMEX: {Digit3_cvvifAMEX}</li>
    <li>billing_Address: {billing_Address}</li>


        <h2>Terms and Condition</h2>
        
        <p>Thank you for reserving  VIP CLASS LIMO'S  for quality assurance please review your 
        reservation for proper dates, addresses and times. It is up to you to inform us of
        any corrections this is not  VIP CLASS LIMO'S  responsibility. In case of any question 
        call us at (888)383-3911. 100 non-refundable payment is expected when the reservation
        is made. All payments are non-refundable and non-transferable in any case of cancellation.
        Cancellations must be submitted in writing, via email. Remaining payments Must be Paid 30 
       days before reservation date and will be charged on card on file automatically. Reply to 
       this email to constitute your acceptance of these terms via email. Cancellation requests must
       be done in writing via email to Info@vipclasslimos.com
       Thank you.</p
        <p>Overtime R 10 Minute Grace Period Is Allowed. All overtime will be charged to the
        same credit card. we use for booking. Overtime is charged by the hour not prorated 
        per minute and will be charged same rate as per signed contract per hour rates 
        at the time of booking. Credit card on file will be charged, prior to the event date, 
        for overtime and damages deposit. Security deposit will be refunded upon completion
        of the trip after inspection of the vehicle if there is no overtime and damages 
        refund will be processed in 3 to 4 working days. In the event we have another
        engagement after your service, there is no guarantee that  VIP CLASS LIMO'S  Will 
        be available for overtime hours beyond your contracted time block. We reserve
        the right to conclude services at any moment once the contractual period has 
        expired. We do not intend to be tardy on your service help us to be on time for our 
        next Trip. If you feel you need more time, please book in advance and we will gladly 
        accommodate to our best ability. Payment Accep We accept all major Credit Cards and 
        Cash payments. If paying by check, it must clear 7 days before your services date .
        Cardholder Acceptance: I read the contract and I accept the  VIP CLASS LIMO'S  terms
        and conditions, and I understand All payments are non-refundable in any case of cancelation.</p>

        <h3>Traffic Congestion:</h3>

        <p>Stops and Addresses Listed on your contract all addresses must be provided in advance,
         VIP CLASS LIMO'S  will not be held responsible for time lost mapping new addresses
        or trying to find landmarks. Please list all addresses in advance to ensure quality
        mapping and routing.  Note Any Tolls On the road customer must pay. It is agreed and
        understood that  VIP CLASS LIMO'S  shall not be held liable or responsible for
        delays in traffic, roadblocks, alternative route delays or because of the misdirection
        of the driver by passengers. Delays for inclement weather shall also be the responsibility
        of the contracted  VIP CLASS LIMO'S  does not offer credits during traffic delays,
        please allow extra time for travel if you feel it is necessary. Please consider your
        times carefully when booking or choosing a lengthier package.</p>

        <h1>Weather Policy</h1>
        <p> VIP CLASS LIMO'S  rentals reserves the right to suspend service if weather is inclement
        and could jeopardize safety. In these instances, a rain & Snow date will be allowed for
        the customer to choose a future date. All deposits will be Hold for future date.</p>

        <h3>VEHICLE DAMAGE POLICY</h3>
        <p>The Agreeing guarantor of this reservation accepts full financial liability for any physical
        damage or breakage of crystal, switches, burn marks, stains etc. Escape Hatches are for
        emergencies only.  VIP CLASS LIMO'S  rental reserves the right to terminate service with
        no refund to client if clients renting service act in disorderly or violent manner.  VIP CLASS LIMO'S 
        reserves the right to initiate legal collection proceedings for loss of service or damage
        fees that are not fully paid within 14 days past date of service and will bill for any and all
        attorneys’ fees, collection expenses and court costs incurred.</p>

        <h3>SMOKING/ALCOHOL POLICY</h3>
        <p>Our Vehicles are non-smoking. A $ 250.00 charge per occurrence will apply. If needed, your driver
        will pull over to allow passengers to smoke outside Limousine. Illegal use of drugs is prohibited
        in our limousines and can terminate ride at no refund to customer. Alcohol consumption in our
        vehicle is not permissible if any passenger on board is under the age of 21, alcohol must not be
        present during these instances or services may be terminated. In the event of illness,
        a minimum $350.00 clean-up will apply for steam cleaning and detailing all bodily fluids.</p>

        <h3>PASSENGER COUNT</h3
        <p>No chauffeur will operate a vehicle with more passengers than the vehicle is rated to accommodate.
        Please ensure the vehicle you are renting will accommodate your passenger count.</p>

        <h3>GENERAL ADDITIONAL POLICY</h3>
            <p>If for any reason the firm is unable to perform the service as contract,
            its maximum liability shall be limited to a full refund of any monies paid 
            by customers toward their rental or a credit towards future service. In rare 
            instances we reserve the right to substitute vehicles in the event of mechanical 
            failure. In the event of mechanical failure,  VIP CLASS LIMO'S  rentals reserves 
            the right to make a comparable substitution. In the event we have advance 
            notice of a vehicle being taken out of service, we will contact you and 
            advise you of available options. If a vehicle becomes disabled in the route 
            to your service, we will send a comparable substitution at no extra charge to you. 
            It is agreed that no person shall cause any contracted vehicle to be overloaded past 
            the passenger capacity of any contracted vehicle. It is further understood that
            all passengers should discharge themselves from the vehicle orderly and should 
            check for personal items before departing the contracted vehicle.
             VIP CLASS LIMO'S  shall not be responsible for any items left in a contracted vehicle.
            It is your responsibility to check the vehicle for personal items.
            The contracting person agrees that all claims and or complaints
            must be submitted in writing to  VIP CLASS LIMO'S  rentals no later than 
            7days after the scheduled event. Moreover, should it be deemed necessary
            for  VIP CLASS LIMO'S  to enlist attorneys or collection agencies to assist in 
            collection of monies due for non-payment of services or a breach of this contract,
            it shall be at the expense of the contracted event. Failure to comply with any 
            or all terms and conditions of this contract may result in termination of your ride,
            forfeiture of all payments and deposits the contracted event acknowledges that upon,
            reading and understanding the terms and conditions of this contract, 
            hereby agrees by signing this contract. Chauffeurs have the authority 
            to determine if vehicles can safely make tight turns or enter narrow
            driveways, in such instance’s clients may need to walk to or from the vehicle. 
            For your safety, walking or standing in the vehicle is prohibited while in motion.
             VIP CLASS LIMO'S  will not be held liable for injury sustained if limousine must 
            come to an immediate stop.</p>
            <h3>Note</h3>
           <p style="color: white; background-color: orange;">Card holder Acceptance: I read the contract and I accept all
            VIP CLASS LIMO'S  rentals terms and conditions and I understand All payments are non refundable.</p>
    
        </body>
        </html>
        
                    """
            # print(message_text)
            message_text = message_text.replace("{first_name}",first_name)
           
            message_text = message_text.replace("{last_name}",last_name)
            message_text = message_text.replace("{phone_num}",phone_num)
            message_text = message_text.replace("{email}",email)
            message_text = message_text.replace("{pick_up_address}",pick_up_address)
            message_text = message_text.replace("{drop_off_Address}",drop_off_Address)
            message_text = message_text.replace("{city}",city)
            message_text = message_text.replace("{zipcode}",zipcode)
            message_text = message_text.replace("{pick_up_Date}",pick_up_Date)
            message_text = message_text.replace("{pick_Up_Time}",pick_Up_Time)
            message_text = message_text.replace("{stop_En_Route}",stop_En_Route)
            message_text = message_text.replace("{number_of_Hours}",number_of_Hours)
            message_text = message_text.replace("{no_of_Passengers}",no_of_Passengers)
            message_text = message_text.replace("{select_Vehicle}",select_Vehicle)

            message_text = message_text.replace("{number_of_Hours}",number_of_Hours)
            message_text = message_text.replace("{first_Name_credit_card}",first_Name_credit_card)
            message_text = message_text.replace("{no_of_Passengers}",no_of_Passengers)
            message_text = message_text.replace("{routing_Request}",routing_Request)
            message_text = message_text.replace("{last_Name_credit_card}",last_Name_credit_card)
            message_text = message_text.replace("{credit_card_Number}",credit_card_Number)
           
            message_text = message_text.replace("{month_Year}",month_Year)
            message_text = message_text.replace("{Digit3_cvvifAMEX}",Digit3_cvvifAMEX)
            message_text = message_text.replace("{billing_Address}",billing_Address)
            msg.attach(MIMEText(message_text, 'html'))
            
            
            signature_data= False
            # Get the signature data from the hidden input field
            signature_data = request.POST.get('signature_data')
            print('i am here')
            if signature_data:
                # Attach the signature image to the email
                signature = MIMEImage(base64.b64decode(signature_data.split(',')[1]), 'png')
                signature.add_header('Content-Disposition', 'attachment', filename='signature.png')
                
                msg.attach(signature)

                # Set the uploaded_signature_url to the URL of the temporary signature image
                uploaded_signature_url = settings.MEDIA_URL + 'temp_signature.png'

                # SMTP configuration and email sending
                smtp_server = "smtpout.secureserver.net"  # Your SMTP server address
                smtp_port = 465  # Port for SMTP_SSL (update to your server's settings)
  
                username = "Info@vipclasslimos.com"
                password = 'Marksmith@30047'
                obj = smtplib.SMTP_SSL(smtp_server, smtp_port)

                # Authentication
                obj.login(username, password)

                # Sending the email
                obj.sendmail(msg['From'], msg['To'], msg.as_string())

                # Quit the server
                obj.quit()

                print('Successfully sent reservation_form email.')

        except Exception as e:
            print(f'Error sending email: {str(e)}')

    return render(request, 'reservationform.html', {'uploaded_signature_url': uploaded_signature_url})
 
