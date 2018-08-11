# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

#basic auth to post blog, add blog post model here
#content_type = ContentType.objects.get_for_model()
#permission = Permission.objects.greate(
#    codeanme='can_publish',
#    name='Can Publish Posts',
#    content_type = content_type,
#)


class Profile(models.Model):
    user = models.OneToOneField(User,unique=True, null=False, db_index=True, on_delete=models.DO_NOTHING)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



