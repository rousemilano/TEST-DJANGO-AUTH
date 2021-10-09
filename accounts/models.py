from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class UserProfile(models.Model):
    profile_picture = models.ImageField(upload_to='user/picture', verbose_name='Picture')
    phone_number = models.CharField(max_length=50, verbose_name='Phone')
    short_description = models.TextField(max_length=200, verbose_name='Description')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User')

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"
    
    def __str__(self):
        return self.user.username

    def __unicode__(self):
        return self.user.username

class AnonymousUser(models.Model):
    ip_address = models.CharField(max_length=52, verbose_name='IP Address')
    created_date = models.DateField(default=datetime.now, verbose_name='Created Date')

    class Meta:
        verbose_name = "Anonymous User"
        verbose_name_plural = "Anonymous Users"
    
    def __str__(self):
        return self.ip_address

    def __unicode__(self):
        return self.ip_address

class Room(models.Model):
    created_date = models.DateField(verbose_name='Created Date')
    anonymousUser = models.ForeignKey(AnonymousUser, on_delete=models.CASCADE, verbose_name='Anonymous User')
    speaker = models.ForeignKey(UserProfile, on_delete=models.CASCADE, verbose_name='Speaker')

    class Meta:
        verbose_name = "Room"
        verbose_name_plural = "Rooms"
    
    def __str__(self):
        return self.speaker.user.username

    def __unicode__(self):
        return self.speaker.user.username
