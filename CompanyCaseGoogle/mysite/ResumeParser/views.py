from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "ResumeParser/index.html")

def resumeSubmission(request):
    return render(request, "ResumeParser/submit.html")

def adminReview(request):
    return render(request, "ResumeParser/review.html")
