from email.policy import default
import math
from pickletools import pydict
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from ResumeParser.jsonfield import JSONField
import json
    #always ignore capitloization
    # weight doesnt have to add up to 1 -> we will convert it afterwards
    # TaregtNum_ut_Weight-> Up to a certain weight given big enough numb
    # TargetOcc_uc_Weight-> Up to a certain weight given enough occ
        # look for tool

default_weighting= {
    'Work Experience': [.25, {'Duration of Experience':[r'[0-9]+[+][ years of experience]gm', 1, 'UT', 1]}],
    'Tools': [.30, {
       'react experience' : [ r'[react]gm', 1, 'UC', 1],
        'django experience' :[r'[django]gm', 1, 'UC', 1],
        'tailwind experience' :[r'[tailwind]gm', 1, 'UC', 1],
        }]
    }

def normalize_weighting(py_dict):
    weighting = py_dict
    top_level_sum = 0
    for title, weight in weighting.items():
        low_level_sum = 0
        for redex, tar_weight in weight[1].items():
            low_level_sum += tar_weight[-1]

        for redex, tar_weight in weight[1].items():
            tar_weight[-1] = math.floor((tar_weight[-1] / low_level_sum) * 1000) / 1000
        top_level_sum += float(weight[0])

    for title, weight in weighting.items():
        weighting[title][0] = math.floor((float(weight[0]) / top_level_sum) * 1000) / 1000
normalize_weighting( default_weighting)


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
    description = models.TextField(max_length = 70, default="", blank = True)
    #weight of various substrings
    # weight -> what that weight is made from

    weighting = JSONField(default=json.dumps(default_weighting))

    def save(self, *args, **kwargs):
        super(Opening, self).save(*args, **kwargs)
        self.normalizeWeighting()

    def normalizeWeighting(self):
        normalize_weighting(self.weighting)
    
    def getWeighting(self):
        return(self.weighting)

    def __str__(self) -> str:
        return self.name


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
