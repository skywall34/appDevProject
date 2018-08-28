# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



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


class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=False)
    title = models.CharField(max_length=100,blank=False)
    post_type = models.CharField(max_length=100)
    country = models.CharField(max_length=64,blank=False)
    state = models.CharField(max_length=64, blank=True)
    city = models.CharField(max_length=64)
    date = models.DateTimeField(auto_now=True)
    num_of_people = models.IntegerField(blank=False)
    theme = models.CharField(max_length=100,blank=False)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to="img")

    def __str__(self):
        return self.title
