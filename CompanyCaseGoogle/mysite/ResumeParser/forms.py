from dataclasses import field
from multiprocessing import AuthenticationError
from django.forms import ModelForm, Textarea
from ResumeParser.models import Application
from django.utils.translation import gettext_lazy as _

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['apply_for', 'resume']
        labels = {
            'apply_for': _("Application Choice"),
            }

