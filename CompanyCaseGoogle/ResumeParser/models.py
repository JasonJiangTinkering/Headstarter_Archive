from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resumeadmin = models.BooleanField(default=False)
    def __str__(self) -> str:
        display_name = self.user.first_name + " " + self.user.last_name
        if display_name.strip() == "":
            return self.user.username
        return self.user.first_name + " " + self.user.last_name

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Opening(models.Model):
    name = models.CharField(max_length=30)


from django.core.validators import FileExtensionValidator
class Application(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    apply_for = models.ForeignKey(Opening, on_delete=models.CASCADE)
    resume = models.FileField(upload_to="UploadedResumes", validators=[
        FileExtensionValidator( ['pdf', 'docx'] ),
        ],
        help_text="Please Submit PDF or DOCX file format"
        )
    REQUIRED_FIELDS = [first_name, last_name, email, apply_for, resume]
