from contextlib import nullcontext
import email
from email.policy import default
from operator import mod
from pyexpat import model
from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password

class Role(models.Model):
    roleName=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(default=datetime.datetime.now())
    is_deleted=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.roleName


class UserProfile(models.Model):
    Name= models.CharField(max_length=50,null=True,)
    password= models.CharField(max_length=100,null=True,)
    email=models.EmailField(blank=True,null=True)
    role=models.ForeignKey("Role",on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.datetime.now())
    is_deleted=models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().full_clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.email


class DebateList(models.Model):
    DebateTopic=models.CharField(max_length=100,null=True,)
    description=models.TextField()
    is_approved=models.BooleanField(default=False)
    created_at=models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc))
    is_deleted=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.DebateTopic



class Debate(models.Model):
    users=models.ManyToManyField("UserProfile")
    # user2=models.ManyToManyField("UserProfile",null=True,blank=True)
    topic=models.ForeignKey("DebateList",on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.datetime.now())
    is_deleted=models.BooleanField(default=False)
    is_tarminated=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.topic.DebateTopic
