from django.urls import path, include
from .views import user_login, user_logout, user_register


app_name='accounts'
urlpatterns = [
    path('login/', user_login, name="login_page"),
    path('logout/', user_logout, name="logout_page"),
    path('register/', user_register, name="register_page"),
]

