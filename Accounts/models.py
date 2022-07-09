from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username_id = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='photos/', default='photos/download.png')
    follower = models.ManyToManyField("Profile")
    age = models.PositiveIntegerField(null=True)
    # MALE = 'MA'
    # FEMALE = 'FE'
    # OTHER = 'OT'
    # gender_list = [
    #     (MALE, 'Male'),
    #     (FEMALE, 'Female'),
    #     (OTHER, 'Other'),
    # ]
    # gender = models.CharField(max_length=2, choices=gender_list, default='MA')
    # follower = models.IntegerField(default=0)
    # following = models.IntegerField(default=0)
    following = models.ManyToManyField("Profile", related_name='following_me')

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username_id
