from typing import Reversible
from django.db import models

from django.contrib.auth.models import AbstractBaseUser,    BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone



class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff,
        is_active=True,
        is_superuser=is_superuser,
        last_login=now,
        date_joined=now,
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/onboarding/users/%i/" % (self.pk)




class AttachLec(models.Model):
    attach_lec = models.AutoField(primary_key=True)
    is_valid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    lecturer = models.ForeignKey('Lecturer', models.DO_NOTHING, db_column='lecturer', blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, db_column='department', blank=True, null=True)

    class Meta:
        db_table = 'attach_lec'
        unique_together = (('date', 'lecturer', 'department'),)

    def __str__(self)-> str:
        return self.date


class Department(models.Model):
    department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'department'

    def __str__(self)-> str:
        return self.name

class Lecturer(models.Model):
    lecturer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'lecturer'
        unique_together = (('id', 'name'),)

    def __str__(self)-> str:
        return self.name


class Student(models.Model):
    student = models.AutoField(primary_key=True)
    school = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'student'
        unique_together = (('id', 'name'),)

    def __str__(self)-> str:
        return self.name