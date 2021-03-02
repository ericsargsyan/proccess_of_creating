from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save

def create_profile(sender, instance, created, **kwargs):

    if created:
        Profile.objects.create(user=instance)
        # print("Profile is Created")

post_save.connect(create_profile, sender=User)

# def save_profile(sender,instance,**kwargs):
#     instance.profile.save()
