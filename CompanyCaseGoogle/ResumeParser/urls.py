from . import views
from django.urls import path

app_name = 'ResumeParser'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit', views.resumeSubmission, name="submit"),
    path('review', views.adminReview, name="review"),
]