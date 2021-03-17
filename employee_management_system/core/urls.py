from django.contrib import admin
from django.urls import path
from core.views import LoginView,Logout


urlpatterns = [
    path('login/', LoginView.as_view(),name = "login"),
    # path('logout/', Logout,name = "logout"),
]
