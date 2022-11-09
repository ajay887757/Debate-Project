from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
    AbstractUser,
    UserManager as AbstractUserManager,
)

class UserManager(BaseUserManager):
    def create_superuser(self,email, password,**other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email,password,**other_fields)
    
    def create_user(self,email,password,**other_fields):

        user = self.model(email=email,
                          **other_fields)
        user.set_password(password)
        user.save()
        return user

class Role(models.Model):
    roleName=models.CharField(max_length=50,null=True)
    created_at=models.DateTimeField(default=datetime.datetime.now())
    is_deleted=models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.roleName


class UserProfile(AbstractBaseUser, PermissionsMixin):
    Name= models.CharField(max_length=50,null=True,)
    password= models.CharField(max_length=100,null=True,)
    email=models.EmailField(blank=True,null=True,unique=True)
    role=models.ForeignKey("Role",on_delete=models.CASCADE,null=True,blank=True)
    created_at=models.DateTimeField(default=datetime.datetime.now(tz=timezone.utc),blank=True)
    is_deleted=models.BooleanField(default=False,blank=True)

    is_staff = models.BooleanField(default=False,blank=True)
    is_active = models.BooleanField(default=True,blank=True)
    is_superuser=models.BooleanField(default=False,blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]

    objects = UserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super().full_clean()
        super().save(*args, **kwargs)

    # def __str__(self) -> str:
    #     return self.email


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
