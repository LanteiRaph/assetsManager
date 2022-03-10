# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Assignment(models.Model):
    assignment = models.AutoField(primary_key=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, db_column='department', blank=True, null=True)
    equipment = models.ForeignKey('Equipment', models.DO_NOTHING, db_column='equipment', blank=True, null=True)
    is_valid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'assignment'
        unique_together = (('is_valid', 'department', 'equipment'),)


class AttachLec(models.Model):
    attach_lec = models.AutoField(primary_key=True)
    is_valid = models.IntegerField()
    date = models.DateField(blank=True, null=True)
    lecturer = models.ForeignKey('Lecturer', models.DO_NOTHING, db_column='lecturer', blank=True, null=True)
    department = models.ForeignKey('Department', models.DO_NOTHING, db_column='department', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attach_lec'
        unique_together = (('date', 'lecturer', 'department'),)


class Condition(models.Model):
    condition = models.AutoField(primary_key=True)
    equipment = models.ForeignKey('Equipment', models.DO_NOTHING, db_column='equipment', blank=True, null=True)
    request = models.ForeignKey('Request', models.DO_NOTHING, db_column='request', blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ok = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'condition'
        unique_together = (('request', 'date'),)


class Department(models.Model):
    department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'


class Equipment(models.Model):
    equipment = models.AutoField(primary_key=True)
    make = models.ForeignKey('Make', models.DO_NOTHING, db_column='make', blank=True, null=True)
    serial_num = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'equipment'
        unique_together = (('serial_num', 'make'),)


class General(models.Model):
    general = models.AutoField(primary_key=True)
    request = models.ForeignKey('Request', models.DO_NOTHING, db_column='request', blank=True, null=True)
    make = models.ForeignKey('Make', models.DO_NOTHING, db_column='make', blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general'
        unique_together = (('name', 'make'),)


class Image(models.Model):
    image = models.AutoField(primary_key=True)
    src = models.CharField(unique=True, max_length=255, blank=True, null=True)
    equipment = models.ForeignKey(Equipment, models.DO_NOTHING, db_column='equipment', blank=True, null=True)
    general = models.ForeignKey(General, models.DO_NOTHING, db_column='general', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image'


class Lecturer(models.Model):
    lecturer = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lecturer'
        unique_together = (('id', 'name'),)


class Make(models.Model):
    make = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    barcode = models.IntegerField(unique=True, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'make'


class Request(models.Model):
    request = models.AutoField(primary_key=True)
    user = models.IntegerField(blank=True, null=True)
    date_in = models.DateField(blank=True, null=True)
    date_out = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'request'
        unique_together = (('date_out', 'date_in'),)


class State(models.Model):
    state = models.AutoField(primary_key=True)
    taken = models.IntegerField()
    request = models.ForeignKey(Request, models.DO_NOTHING, db_column='request', blank=True, null=True)
    general = models.ForeignKey(General, models.DO_NOTHING, db_column='general', blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'state'
        unique_together = (('date', 'taken'),)


class Student(models.Model):
    student = models.AutoField(primary_key=True)
    school = models.IntegerField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, db_column='department', blank=True, null=True)
    id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    user = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
        unique_together = (('id', 'name'),)
