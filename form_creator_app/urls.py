
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    
    path('reservation', views.Reservation_form, name='reservation'),
    path('fleet', views.fleet, name='fleet'),
    path('limo-hir-eservices', views.limohireservices, name='limo-hire-services'),
    path('Get_Quick_Quote', views.Get_Quick_Quote_method , name = "Get_Quick_Quote"),
    
    path('KIDSLIMOPARTIES', views.KIDSLIMOPARTIES, name='KIDSLIMOPARTIES'),
    path('PROMLIMO', views.PROMLIMO, name='PROMLIMO'),
    path('ROYALASCOTLIMOHIRE', views.ROYALASCOTLIMOHIRE, name='ROYALASCOTLIMOHIRE'),
    
    path('SPECIALOCCASIONLIMOHIRE', views.SPECIALOCCASIONLIMOHIRE, name='SPECIALOCCASIONLIMOHIRE'),
    path('weddingcarhire', views.weddingcarhire, name='weddingcarhire'),
    path('limo-hire-services', views.limohireservices, name='limo-hire-services'),
    #now fleet urls
    path('SEATLUXURYCARS', views.SEATLUXURYCARS, name='SEATLUXURYCARS'),
    path('eSEATSTRETCHLIMOS', views.eSEATSTRETCHLIMOS, name='eSEATSTRETCHLIMOS'),
    path('sSEATSTRETCHLIMOS', views.sSEATSTRETCHLIMOS, name='sSEATSTRETCHLIMOS'),
    path('SEATPARTYBUSES', views.SEATPARTYBUSES, name='SEATPARTYBUSES'),
    #OFFERScontact
    path('OFFERS', views.OFFERS, name='OFFERS'),
    path('QUOTES', views.QUOTES, name='QUOTES'),
    path('CONTACT', views.CONTACT, name='CONTACT'),
    path('Messagesend', views.Message_send, name='CONTACT'),
    
    
    
]

