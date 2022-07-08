from . import views
from django.urls import path

app_name = 'ResumeParser'
urlpatterns = [
    path('', views.index, name='index'),
    path('submit/<int:opening_id>', views.resumeSubmission, name="submit"),
    path('review/<int:opening_id>', views.adminReview, name="review"),

]