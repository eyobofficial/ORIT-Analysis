from django.contrib import messages
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RegistrationForm


User = get_user_model()


class AuthenticationView(LoginView):
    """
    Login a user
    """

    def form_valid(self, form):
        redirect_to = super().form_valid(form)
        user = form.get_user()

        base_path = 'accounts/components/notifications'
        if user.last_login:
            path = f'{base_path}/welcome_back.html'
            message = render_to_string(path, {'user': user})
        else:
            path = f'{base_path}/welcome.html'
            message = render_to_string(path, {'user': user})

        messages.warning(self.request, message)
        return redirect_to


class UserRegisterationView(CreateView):
    """
    Signup a new user
    """
    model = User
    form_class = RegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('dashboard:overview')
    message_path = 'accounts/components/notifications'

    def get_notification(self):
        path = f'{self.message_path}/welcome.html'
        return render_to_string(path, {'user': self.request.user})

    def form_valid(self, form):
        pass
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        messages.warning(self.request, self.get_notification())
        return redirect(self.success_url)
