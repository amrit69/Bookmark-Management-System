from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('bookmarks/',views.bookmarks, name='bookmark'),
    path('login/',views.login, name='login'),
    

]
