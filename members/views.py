from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('login')
    # LOGIN_REDIRECT_URL = '/'
