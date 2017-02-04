
from django.db import models
from django.contrib.auth.models import User
from django.db.models import IntegerField, CharField,Model, FileField, FloatField, DateTimeField

class Center(Model):
    center_id = IntegerField(unique=True , blank = False,default=0)
    name = CharField(max_length=30 , blank=True)
    address = CharField(max_length=100 , blank=True)

class Member(Model):
    melli_code = IntegerField(unique=True , blank=False ,)
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank=True , null=True)
    membership_type = CharField(
        max_length=20,
        choices=(
            ("head_manager", "Head Manager"),
            ("legal_expert","Legal Expert"),
            ("center_manager","Center Manager"),
            ("cashier","Cashier"),
            ("auditor","Auditor"),
            ("accountant","Accountant")
        ),
        blank=True
    )



class Customer(Model):
    melli_code = IntegerField(unique=True , blank=False)
    first_name = CharField(max_length=20 , blank=True)
    last_name = CharField(max_length=20 , blank= True)
    center = models.ForeignKey(Center, on_delete=models.CASCADE, blank=True , null=True)

class CustomerAccount(Model):
    owner_melli_code = IntegerField(blank=False)
    account_number = IntegerField(unique=True , blank=False)
    money = IntegerField(blank=False)
    center = models.ForeignKey(Center , on_delete=models.CASCADE , blank=True , null=True)






