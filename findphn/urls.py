from django.urls import path
from . import views

urlpatterns = [
    path('',views.findNumber,name='index'),
    path('find-number-api/',views.FindNumberAPI.as_view()),
    path('find-number-in-text-api/',views.FindPhoneNumberInText.as_view()),
]
