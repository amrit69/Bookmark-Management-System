from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('bookmark',views.bookmark, name='bookmark'),
    path('login',views.login, name='login'),
    path('register',views.register, name='register'),
    path('password',views.password, name='password'),
    
    

    

]
