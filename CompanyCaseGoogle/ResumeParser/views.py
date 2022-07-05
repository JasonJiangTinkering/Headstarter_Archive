from django.shortcuts import render
from ResumeParser.forms import ApplicationForm
# Create your views here.
def index(request):
    return render(request, "ResumeParser/index.html")

def resumeSubmission(request):
    context = {
        "form": ApplicationForm,
    }
    return render(request, "ResumeParser/submit.html", context)

def adminReview(request):
    return render(request, "ResumeParser/review.html")
