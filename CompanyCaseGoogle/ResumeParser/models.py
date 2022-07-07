from django.db import models
# Create your models here.
class AdminUser(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    admin = models.BooleanField(default=False)
    REQUIRED_FIELDS = [first_name, last_name, email, admin]

class Opening(models.Model):
    name = models.CharField(max_length=30)

class Application(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    apply_for = models.ForeignKey(Opening, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="UploadedResumes")
    REQUIRED_FIELDS = [first_name, last_name, email, apply_for, resume]
