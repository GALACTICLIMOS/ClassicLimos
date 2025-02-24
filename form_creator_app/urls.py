
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
   
    path('index', views.index, name='index'),
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
    path('send_email', views.send_email, name='send_email'),

    # new

    path('BostonMA', views.bostonma, name='BostonMA'),
    path('AtlantaGeorgia', views.AtlantaGeorgia , name='AtlantaGeorgia'),
    path('AlexandriaVA', views.AlexandriaVA , name='AlexandriaVA'),
    path('ArlingtonTexas', views.ArlingtonTexas , name='ArlingtonTexas'),
    path('BaltimoreMD', views.BaltimoreMD , name='BaltimoreMD'),
    path('ChicagoIL', views.ChicagoIL , name='ChicagoIL'),
    path('DallasTX', views.DallasTX , name='DallasTX'),
    path('FortMyersFL', views.FortMyersFL , name='FortMyersFL'),
    path('SanFranciscoCA', views.SanFranciscoCA , name='SanFranciscoCA'),
    path('SacramentoCA', views.SacramentoCA , name='SacramentoCA'),
    path('PhoenixAZ', views.PhoenixAZ , name='PhoenixAZ'),
    path('PittsburghPA', views.PittsburghPA , name='PittsburghPA'),
    path('PhiladelphiaPA', views.PhiladelphiaPA , name='PhiladelphiaPA'),
    path('LasVegasNV', views.LasVegasNV , name='LasVegasNV'),
    path('LosAngelesCA', views.LosAngelesCA , name='LosAngelesCA'),
    path('NewYorkCityNY', views.NewYorkCityNY , name='NewYorkCityNY'),
    path('WashingtonDC', views.WashingtonDC , name='WashingtonDC'),
    path('MiamiFL', views.MiamiFL , name='MiamiFL'),

    
    path('CharlotteNC', views.CharlotteNC, name='CharlotteNC'),
    path('ClevelandOH', views.ClevelandOH, name='ClevelandOH'),
    path('TampaFL', views.TampaFL, name='TampaFL'),
    path('HoustonTX', views.HoustonTX, name='HoustonTX'),
    
    
    
    
    
    
    
    
    
    
    
]

