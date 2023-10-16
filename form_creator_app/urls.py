
from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    
    path('reservation', views.reservationform, name='reservation'),
    path('fleet', views.fleet, name='fleet'),
    path('Get_Quick_Quote', views.Get_Quick_Quote_method , name = "Get_Quick_Quote"),
]

