from django.urls import path

from members.views import UserRegisterView

app_name = 'members'

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register')
]