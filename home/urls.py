from django.urls import path
from home.views import main_home
app_name = 'home'
urlpatterns = [
    path("", main_home, name="main_home")
]
