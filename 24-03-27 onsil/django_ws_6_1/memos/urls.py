from django.urls import path
from . import views

app_name = 'memos'

urlpatterns = [
    path('memos/',views.index, name ='index')
]

