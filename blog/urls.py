from django.urls import path
from .views import (
    HomeList
   
)
app_name= "Post"
urlpatterns = [
     path('', HomeList.as_view(),  name='home'),
    
]