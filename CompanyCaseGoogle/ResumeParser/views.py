from django.shortcuts import redirect, render
from ResumeParser.forms import ApplicationForm
from django.http import HttpResponse
from django.contrib import messages
from ResumeParser.models import Opening
from django.contrib.auth.decorators import login_required 

def admin_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id):
            return HttpResponse('<h1> Not Logged In</h1>"')
        else:
            if (not user.profile.resumeadmin):
                return HttpResponse("<h1> User is not an Admin </h1>")
            return function(request, *args, **kw)
    return wrapper

# Create your views here.
def index(request):
    openings = Opening.objects.all()
    context = {
        "opening" : openings,
    }
    return render(request, "ResumeParser/index.html", context)

def resumeSubmission(request, opening_id):
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
@login_required
def adminReview(request, opening_id):
    return render(request, "ResumeParser/review.html")
