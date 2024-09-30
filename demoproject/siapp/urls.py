from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index'),
    path('hello',views.welcome,name='testfun'),
    path('radioexample',views.radioexample,name='radioexample'),
    path('checkboxexample',views.checkboxexample,name='checkboxexample')
]