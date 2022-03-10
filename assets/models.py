from typing import Reversible
from django.db import models

from onboarding.models import User, Department

class RequestDetails(models.Model):
    request_detail = models.AutoField(primary_key=True)
    return_detail = models.ForeignKey('ReturnDetail', models.DO_NOTHING,db_column='return_detail', blank=True, null=True )
    equipment = models.ForeignKey('Equipment', models.DO_NOTHING, db_column='equipment', blank=True, null=True)
    request = models.ForeignKey('RequestList', models.DO_NOTHING, db_column='request', blank=True, null=True)
    date = models.DateTimeField()
    qty = models.IntegerField()

    class Meta:
        db_table = 'requestDetail'
        unique_together = (('equipment', 'date'),)

    def __str__(self)-> str:
        return 'condition'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return Reversible('equipment-details', args=[str(self.request_detail)])

class Equipment(models.Model):
    equipment = models.AutoField(primary_key=True)
    make = models.ForeignKey('Make', models.DO_NOTHING, db_column='make')
    serial_num = models.IntegerField()

    class Meta:
        db_table = 'equipment'
        unique_together = (('serial_num', 'make'))
        ordering = ['serial_num']

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return Reversible('equipment-details', args=[str(self.equipment)])

    def __str__(self)-> str:
        return 'equipment'

class Assignment(models.Model):
    assignment = models.AutoField(primary_key=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equipment', blank=True, null=True)
    is_valid = models.IntegerField()

    class Meta:
        db_table = 'assignment'
        unique_together = (('is_valid', 'department', 'equipment'),)


    def __str__(self)-> str:
        return self.is_valid

class General(models.Model):
    general = models.AutoField(primary_key=True)
    request = models.ForeignKey('RequestList', models.DO_NOTHING, db_column='request', blank=True, null=True)
    make = models.ForeignKey('Make', models.DO_NOTHING, db_column='make')
    name = models.CharField(max_length=255)

    class Meta:
        db_table = 'general'
        unique_together = (('name', 'make'),)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return Reversible('equipment-details', args=[str(self.equipment)])

    def __str__(self) -> str:
        return self.name


class Make(models.Model):
    make = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    barcode = models.IntegerField(unique=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'make'

    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return Reversible('equipment-details', args=[str(self.equipment)])

    def __str__(self) -> str:
        return self.name


class RequestList(models.Model):
    request = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, models.DO_NOTHING, db_column='user', blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'request'
        unique_together = (('date_out', 'date_in'),)
        ordering = ['-date_out']

    def __str__(self) -> str:
        return 'request'

    def get_absolute_url(self):
        return Reversible('request-details', args=[str(self.request)])


class State(models.Model):
    state = models.AutoField(primary_key=True)
    taken = models.IntegerField()
    request = models.ForeignKey(RequestList, models.DO_NOTHING, db_column='request', blank=True, null=True)
    general = models.ForeignKey(General, models.DO_NOTHING, db_column='general', blank=True, null=True)
    date = models.DateField(unique=True)

    class Meta:
        db_table = 'state'
        unique_together = (('date', 'taken'))

    def __str__(self) -> str:
        return self.date

class Image(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    src = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)

    def __str__(self) -> str:
        return 'Image'

class Situation(models.Model):
    situation = models.AutoField(primary_key=True)
    date = models.DateTimeField(unique=True)
    description = models.TextField(max_length=255)
    equipment = models.ForeignKey('Equipment', models.DO_NOTHING, db_column = 'equipment', blank=True, null=True)

    def __str__(self) -> str:
        return self.description
    class Meta:
        db_table = 'situation'


class ReturnDetail(models.Model):
    return_detail = models.AutoField(primary_key=True)
    date_in = models.DateTimeField()

    class Meta:
        db_table = 'returnDetail'
