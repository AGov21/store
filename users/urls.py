from django.urls import path
from users.views import user_login, logout, user_register


app_name = 'users'

urlpatterns = [
    path('login/', user_login, name='login'),
    path('register/', user_register, name='register'),
    path('logout/', logout, name='logout'),
]