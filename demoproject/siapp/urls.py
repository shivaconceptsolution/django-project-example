from . import views
from django.urls import path
urlpatterns=[
    path('',views.index,name='index'),
    path('hello',views.welcome,name='testfun'),
    path('radioexample',views.radioexample,name='radioexample'),
    path('checkboxexample',views.checkboxexample,name='checkboxexample'),
    path('colorexample',views.colorexample,name='colorexample'),
    path('feesexample',views.feesexample,name='feesexample'),
    path('listexample',views.listexample,name='listexample'),
    path('ddlexample',views.ddlexample,name='ddlexample'),
    path('dynamicform',views.dynamicform,name='dynamicform')
]