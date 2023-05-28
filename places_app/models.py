from django.contrib.auth.models import User
from django.db import models


class UserP(models.Model):
    id_U = models.IntegerField(null=False, unique=True, primary_key=True, blank=True)
    phone = models.IntegerField(null=False,blank=True)
    address = models.CharField(null=False, max_length=30, blank=True)
    user = models.OneToOneField(User, null=True, on_delete=models.RESTRICT, related_name='user_name')
    type = models.CharField(choices=[('Privet', 'privet'), ('Public', 'public')], max_length=20)

    class Meta:
        db_table = 'UserP'

    def __str__(self):
        return f'{self.phone, self.address}'


class ItemLocation(models.Model):
    id_I = models.IntegerField(null=False, unique=True, primary_key=True, blank=True)
    item_name = models.CharField(null=False, max_length=50, blank=True)
    num_people = models.IntegerField(null=False, blank=True)
    owner = models.ForeignKey(UserP, null=False, on_delete=models.RESTRICT, blank=True)
    city = models.CharField(null=False,max_length=60, blank=True)

    class Meta:
        db_table = 'ItemLocation'

    def __str__(self):
        return f'{self.item_name, self.num_people,self.city}'


class Renters(models.Model):
    id_User = models.IntegerField(null=True, unique=True, blank=True)
    id_Place = models.IntegerField(null=True, unique=True, blank=True)
    start_date = models.DateTimeField(null=False, blank=True)
    end_date = models.DateTimeField(null=False, blank=True)

    class Meta:
        db_table = 'Renters'

    def __str__(self):
        return f'{self.start_date, self.end_date}'
