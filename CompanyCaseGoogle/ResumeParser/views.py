from django.shortcuts import render
from ResumeParser.forms import ApplicationForm
from django.http import HttpResponse, HttpResponseRedirect

def admin_required(function):
    def wrapper(request, *args, **kw):
        user=request.user  
        if not (user.id and request.session.get('code_success')):
            return HttpResponseRedirect('/splash/')
        else:
            if (not user.admin):
                return HttpResponse("<h1> User is not an Admin </h1>")
            return function(request, *args, **kw)
    return wrapper

# Create your views here.
def index(request):
    return render(request, "ResumeParser/index.html")

def resumeSubmission(request):
    context = {
        "form": ApplicationForm,
    }
    return render(request, "ResumeParser/submit.html", context)

@admin_required
def adminReview(request):
    return render(request, "ResumeParser/review.html")
