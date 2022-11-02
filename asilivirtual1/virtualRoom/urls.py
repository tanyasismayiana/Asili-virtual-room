from django.urls import path 
from virtualRoom import views, forms

urlpatterns=[
path("",views.VirtualRoom.as_view(),name ="Virtualroom")
]