from django.shortcuts import render
from ResumeParser.forms import ApplicationForm
from django.http import HttpResponse
from django.contrib import messages
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
