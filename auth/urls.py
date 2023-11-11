from django.urls import path
from .import views

app_name ='auth'

urlpatterns = [
    path('login/',views.login_user,name='login_page'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout_user,name='logout')
]