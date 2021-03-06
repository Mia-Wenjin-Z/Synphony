from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
import datetime
from django.contrib.auth.models import User


class Music(models.Model):

    name = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    lyrics = models.TextField(max_length=255, blank=True)
    liked_user = models.ManyToManyField(User, on_delete=models.CASCADE)

# The goal is to record the liked music of a certain user
# We should implement abstract user, liked_music should be an attribute of it, as we don't know to do that
# For now, we just extend the user here


class Syner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    liked_music = models.ManyToManyField(Music, on_delete=models.CASCADE)


# class Playlist(models.Model):

#     name = models.CharField(max_length=30)
#     music = models.ManyToManyField(Music)
#     created_by = models.ForeignKey(User,on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)

# class Like(models.Model):

#     music = models.ForeignKey(Music,on_delete=models.CASCADE)
#     like_user = models.ForeignKey(User,on_delete=models.CASCADE)

class Participant(models.Model):

    participant_user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, default='participant')
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)


class Studio(models.Model):

    name = models.CharField(max_length=30)
    # participants = models.ManyToManyField(Participant)
    music = models.ManyToManyField(Music, on_delete=models.CASCADE)
    # record whether the studio is active or not
    status = models.BooleanField(default=True)
    # constraint will be set in form.py cannot be larger than 10
    headcount = models.IntegerField(default=10)
    # field_for_sharablelink
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(blank=True)


class Comment(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    commented_on = models.ForeignKey(Studio, on_delete=models.CASCADE)


class History(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    studio = models.ForeignKey(Studio, on_delete=models.CASCADE)
