from django.conf.urls import url
from login import views

# app1 url file

urlpatterns = [
    url(r'^$', views.getTitle, name='getTitle'),
    
]