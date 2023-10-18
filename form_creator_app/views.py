from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
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



def reservationform(request):
    
    if request.method == 'POST':
        
        print("saving reservation form")
        first_name = request.POST['First_Name']
        last_name  = request.POST['Last_Name']
        phone_num  = request.POST['phone']
        email  = request.POST['email']
        pick_up_address  = request.POST['Pick_Up_Address']
        drop_off_Address  = request.POST['Drop_off_Address']
        city  = request.POST['City']
        zipcode  = request.POST['ZipCode']
        pick_up_Date  = request.POST['Pick_up_Date']
        pick_Up_Time  = request.POST['Pick_Up_Time']
        stop_En_Route  = request.POST['Stop_En_Route']
        number_of_Hours  = request.POST['Number_of_Hours']
        no_of_Passengers  = request.POST['No_of_Passangers']
        select_Vehicle  = request.POST['Select_Vehicle']
        routing_Request  = request.POST['Message']
        print('billing information')
        first_Name_credit_card  = request.POST['First_name_credit_card']
        last_Name_credit_card  = request.POST['Last_Name_credit_card']
        credit_card_Number  = request.POST['Credit_card_Number']
        month_Year  = request.POST['Month_Year']
        Digit3_cvvifAMEX  = request.POST['digit3_cvvifAMEX']
        Billing_email  = request.POST['Billing_email']
        billing_Address  = request.POST['Billing_Address']
        print('first_name', first_name)
        print('last_name', last_name)
        print('phone_num', phone_num)
        print('email', email)
        print('pick_up_address', pick_up_address)
        print('drop_off_Address', drop_off_Address)
        print('city', city)
        print('zipcode', zipcode)
        print('pick_up_Date', pick_up_Date)
        print('pick_Up_Time', pick_Up_Time)
        print('stop_En_Route', stop_En_Route)
        print('number_of_Hours', number_of_Hours)
        print('no_of_Passengers', no_of_Passengers)
        print('select_Vehicle', select_Vehicle)
        print('routing_Request', routing_Request)
        print('first_Name_credit_card', first_Name_credit_card)
        print('last_Name_credit_card', last_Name_credit_card)
        print('credit_card_Number', credit_card_Number)
        print('month_Year', month_Year)
        print('Digit3_cvvifAMEX', Digit3_cvvifAMEX)
        print('Billing_email', Billing_email)
        print('billing_Address',billing_Address)
        s = RESERVATION_FORM.objects.create(first_name=first_name, last_name=last_name, phone_num=phone_num, email=email, pick_up_address=pick_up_address, drop_off_Address=drop_off_Address , city=city, zipcode=zipcode, pick_up_Date=pick_up_Date, pick_Up_Time=pick_Up_Time, stop_En_Route=stop_En_Route, number_of_Hours=number_of_Hours, no_of_Passengers=no_of_Passengers, select_Vehicle=select_Vehicle, routing_Request=routing_Request, first_Name_credit_card=first_Name_credit_card, last_Name_credit_card=last_Name_credit_card, credit_card_Number=credit_card_Number, month_Year=month_Year, Digit3_cvvifAMEX=Digit3_cvvifAMEX,Billing_email = Billing_email ,billing_Address=billing_Address)
        s.save()
        
        return redirect('reservation')
        
    return render(request, 'reservationform.html')



def Get_Quick_Quote_method(request):

    Name = request.POST['Name']
    email = request.POST['email']
    Phone = request.POST['Phone']
    Pick_Location = request.POST['Pick_Location']
    Drop_Location = request.POST.get('Drop_Location')
    Select_Vehicle = request.POST.get('Select_Vehicle')
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
    return redirect('index')