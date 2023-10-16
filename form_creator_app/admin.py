from django.contrib import admin
from .models import *
# Register your models here.
class RESERVATION_FORMAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','phone_num','email','pick_up_address', 'drop_off_Address', 'city','zipcode', 'pick_up_Date', 'pick_Up_Time','stop_En_Route','number_of_Hours','no_of_Passengers','select_Vehicle','routing_Request','first_Name_credit_card', 'last_Name_credit_card','credit_card_Number','month_Year','Digit3_cvvifAMEX','Billing_email', 'billing_Address')
admin.site.register(RESERVATION_FORM, RESERVATION_FORMAdmin)


class Get_Quick_QuoteAdmin(admin.ModelAdmin):
    list_display = ('Name','email','Phone','Pick_Location', 'Drop_Location', 'Select_Vehicle', 'No_of_Passengers', 'No_of_Hours', 'Trip_Type', 'Pickup_Date', 'Pickup_Time')
admin.site.register(Get_Quick_Quote, Get_Quick_QuoteAdmin)
