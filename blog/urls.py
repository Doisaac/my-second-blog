from django.urls import path
from .views import (
    HomeList,
    product_create_view
)
app_name= "Post"
urlpatterns = [
     path('', HomeList.as_view(),  name='home'),
     path('create/', product_create_view, name='nadd'),
]