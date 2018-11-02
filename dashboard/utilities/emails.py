from django.contrib.auth import get_user_model
from django.template.loader import render_to_string

from post_office import mail

# User Model
User = get_user_model()


class BaseEmail:
    template_location = None
    template_name = None
    recipient = None
    subject = None
    sender = None

    def get_sender(self):
        if not self.sender:
            self.sender = User.objects.first()

        return '{} {} <{}>'.format(
            self.sender.first_name,
            self.sender.last_name,
            self.sender.email
        )

    def get_template(self):
        return '{}/{}'.format(self.template_location, self.template_name)

    def get_context_data(self, **kwargs):
        if 'email_obj' not in kwargs:
            kwargs['email_obj'] = self
        return kwargs

    def get_attachments(self, **kwargs):
        return kwargs

    def send(self):
        sender = self.get_sender()
        template = self.get_template()
        context = self.get_context_data()
        attachments = self.get_attachments()

        email = mail.send(
            self.recipient.email,
            sender=sender,
            subject=self.subject,
            html_message=render_to_string(template, context),
            attachments=attachments
        )
        return email
