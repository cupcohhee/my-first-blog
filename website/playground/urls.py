from django.urls import path
from .import views
#URLConfi
 
urlpatterns = [
    path('hello/', views.say_hello)
]