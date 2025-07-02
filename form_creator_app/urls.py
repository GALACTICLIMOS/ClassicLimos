
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
    


    # areas path
    path('AtlantaGeorgia', views.AtlantaGeorgia , name = 'AtlantaGeorgia'),
    path('AlexandriaVA', views.AlexandriaVA , name = 'AlexandriaVA'),
    path('ArlingtonTexas', views.ArlingtonTexas , name = 'ArlingtonTexas'),
    path('BaltimoreMD', views.BaltimoreMD , name = 'BaltimoreMD'),
    path('BostonMA', views.BostonMA , name = 'BostonMA'),
    path('CharlotteNC', views.CharlotteNC , name = 'CharlotteNC'),
    path('ChicagoIL', views.ChicagoIL , name = 'ChicagoIL'),
    path('Dallas', views.Dallas , name = 'Dallas'),
    path('FortMyersFL', views.FortMyersFL , name = 'FortMyersFL'),
    path('HoustonTX', views.HoustonTX , name = 'HoustonTX'),
    path('SanFranciscoCA', views.SanFranciscoCA , name = 'SanFranciscoCA'),
    path('SacramentoCA', views.SacramentoCA , name = 'SacramentoCA'),
    path('phoenix', views.phoenix , name = 'phoenix'),
    path('PittsburghPA', views.PittsburghPA , name = 'PittsburghPA'),
    path('Philadelphia', views.Philadelphia , name = 'Philadelphia'),
    path('LasVegasNV', views.LasVegasNV , name = 'LasVegasNV'),
    path('LosAngelesCA', views.LosAngelesCA , name = 'LosAngelesCA'),
    path('MiamiFL', views.MiamiFL , name = 'MiamiFL'),
    path('NewYorkCity', views.NewYorkCity , name = 'NewYorkCity'),
    path('ClevelandOH', views.ClevelandOH , name = 'ClevelandOH'),
    path('TampaFL', views.TampaFL , name = 'TampaFL'),
    path('Washington', views.Washington , name = 'Washington'),
    
    
]

