from django.db import models






    
class Get_Quick_Quote(models.Model):
    Name = models.CharField(max_length=30 , null= True)
    email = models.CharField(max_length=30 , null= True)
    Phone = models.CharField(max_length=30 , null= True)
    Pick_Location = models.CharField(max_length=150 , null= True)
    Drop_Location = models.CharField(max_length=150 , null= True)
    Select_Vehicle = models.CharField(max_length=30 , null= True)
    No_of_Passengers = models.CharField(max_length=30 , null= True)
    No_of_Hours = models.CharField(max_length=30 , null= True)
    Trip_Type = models.CharField(max_length=30 , null= True)
    Pickup_Date = models.CharField(max_length=30 , null= True)
    Pickup_Time = models.CharField(max_length=30 , null= True)

class RESERVATION_FORM(models.Model):
    first_name = models.CharField(max_length=30 , null= True)
    last_name = models.CharField(max_length=30 , null= True)
    phone_num = models.CharField(max_length=30 , null= True)
    email = models.EmailField(max_length=100 , null = False )
    pick_up_address =   models.CharField(max_length=100,  null= True)
    drop_off_Address =  models.CharField(max_length=100,  null= True)
    city = models.CharField(max_length=30,  null= True)
    zipcode = models.CharField(max_length=30,  null= True)
    pick_up_Date = models.CharField(max_length=30,  null= True)
    pick_Up_Time =  models.CharField(max_length=30,  null= True)
    stop_En_Route = models.CharField(max_length=100,  null= True)
    number_of_Hours = models.IntegerField(null= True)
    no_of_Passengers = models.IntegerField(null= True)
    select_Vehicle = models.CharField(max_length=30,null= True)
    routing_Request = models.CharField(max_length=100,  null= True)
    # Billing Information
    first_Name_credit_card =  models.CharField(max_length=30,  null= True)
    last_Name_credit_card =  models.CharField(max_length=30,  null= True)
    credit_card_Number =  models.CharField(max_length=30,  null= True)
    month_Year =  models.CharField(max_length=30,  null= True)
    Digit3_cvvifAMEX =  models.CharField(max_length=100,  null= True)
    Billing_email =  models.EmailField(max_length=100,  null= True)
    billing_Address =  models.CharField(max_length=100,  null= True)
    
