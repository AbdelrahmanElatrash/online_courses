from django.urls import path 
from user_auth.views import *

urlpatterns = [
    path('',index,name='home')
    
]