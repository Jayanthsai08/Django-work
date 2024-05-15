from django.urls import path
from timeapp import views

urlpatterns = [
    path('t1/', views.myfunc),
]
