from django.shortcuts import redirect, render
from ResumeParser.forms import ApplicationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import REDIRECT_FIELD_NAME

from django.conf import settings
login_url = settings.LOGIN_URL

def admin_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url=None
):
    """
    Decorator for views that checks that the user is logged in, redirecting
    to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_authenticated and u.profile.resumeadmin,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


# Create your views here.
def index(request):
    return render(request, "ResumeParser/index.html")

def resumeSubmission(request):
    if request.method == "POST":

        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submission successful')
    context = {
        "form": ApplicationForm,
    }
    return render(request, "ResumeParser/submit.html", context)

@admin_required
def adminReview(request):
    return render(request, "ResumeParser/review.html")
