from multiprocessing import AuthenticationError
from django.forms import ModelForm, ClearableFileInput
from ResumeParser.models import Application
from django.utils.translation import gettext_lazy as _

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['first_name', 'last_name', 'email', 'apply_for', 'resume']
        labels = {
            'apply_for': _("Application Choice"),
            }
        
        widgets = {
            "resume": ClearableFileInput(attrs={"accept":"pdf,.doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"})
        }

