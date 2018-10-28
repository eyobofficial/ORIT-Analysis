from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.template.loader import render_to_string


class AuthenticationView(LoginView):

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
