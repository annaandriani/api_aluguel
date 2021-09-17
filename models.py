from django.db import models

class Host(models.Model):
    name_host = models.CharField(max_length=30)
    classification = models.FloatField(null=True, blank=True)
    host_addresses = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Checkin(models.Model):
    name_client = models.CharField(max_length=30)
    guests = models.IntegerField(null=True)
    telephone = models.IntegerField(null=True)
    id_reserve = models.CharField(max_length=10)
    id_airbnb = models.CharField(default='xxxxxxx', max_length=6)
    address_reserve = models.CharField(max_length=100)
    daily = models.IntegerField()
    checkin_day = models.DateField()
    checkin_hour = models.TimeField()
    bed_temperature_normal = 'normal'
    bed_temperature_hot = 'hot'
    bed_temperature_choices = [(bed_temperature_normal, 'normal'),
                               (bed_temperature_hot, 'hot')],
    price = models.FloatField(null=True, blank=True)
    payment = models.BooleanField(default=False)
    pet_yes = 'yes'
    pet_no = 'no'
    pet_choices =[(pet_yes, 'yes'),
                  (pet_no, 'no')],
    pet = models.CharField(max_length=2, choices=pet_choices,
    default='no',)



    def __str__(self):
        return self.nome


class Checkout(models.Model):
    checkout = models.DateField()
    name_client = models.CharField(max_length=30)
    address_reserve = models.CharField(max_length=100)
    checkout_hour = models.TimeField()
    concluded_yes = 'yes'
    concluded_no = 'pending'
    concluded_choices = [ (concluded_yes , 'yes'),
                          (concluded_no , 'pending')]

    def __str__(self):
        return self.nome


class Cleaning(models.Model):
    daily = models.IntegerField()
    id_cleaning = models.CharField(max_length=30)
    hour_cleaning = models.TimeField()

    def __str__(self):
        return self.nome



