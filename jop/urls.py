from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.jop_list),
    path('int:ip',views.jop_detail)
]