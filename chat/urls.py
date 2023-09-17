
from django.urls import path , include
from . import views

urlpatterns = [

    path('',views.index,name="index"),
    path('chatbot/',views.chatbot,name="chatbot"),
    path('chatbot/get/',views.get,name="get"),
    path('chatbot/get/back/',views.back,name="back/"),
    



]
