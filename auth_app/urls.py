from django.urls import path
from . import views


urlpatterns = [
    path('signUp',views.signUpUser,name='signUp'),
    path("login", views.loginUser, name="login"),
    path('logout',views.logoutUser,name='logout')
]
