from rest_framework import serializers
from snippets.models import Checkout, Checkin, Host, Cleaning

pet_yes = 'yes'
pet_no = 'no'
pet_choices = [(pet_yes, 'yes'),
               (pet_no, 'no')],

bed_temperature_normal = 'normal'
bed_temperature_hot = 'hot'
bed_temperature_choices = [(bed_temperature_normal, 'normal'),
                           (bed_temperature_hot, 'hot')],

concluded_yes = 'yes'
concluded_no = 'pending'
concluded_choices = [(concluded_yes, 'yes'),
                     (concluded_no, 'pending')]

class CheckinSerializer(serializers.Serializer):
    telephone = serializers.IntegerField(default=234567890)
    name_client = serializers.CharField(required=False, allow_blank=True, max_length=100)
    id_airbnb = serializers.CharField(required=False, allow_blank=True, max_length=10)
    id_reserve = serializers.CharField(required=False, allow_blank=True, max_length=10)
    address_reserve = serializers.CharField(required=False, allow_blank=True, max_length=100)
    daily = serializers.IntegerField(read_only=False)
    payment =  serializers.BooleanField(required=False)
    checkin_hour = serializers.models.TimeField(default='00:00')
    bed_temperature = serializers.ChoiceField(choices=bed_temperature_choices, default='hot')
    price = serializers.IntegerField(default=1000)
    pet = serializers.ChoiceField(choices=pet_choices, default='yes')
    guests = serializers.IntegerField(default=1)
    checkin_1 =('47999876544', 'Gabriela da Silva', 'ADJ275', 'HMYDPRK5FS', 'Avenida Búzios, 1800 Jurerê InternacIonal. Florianópolis-SC, CEP:8950-100',  '9',  'pending', '14:00','hot', '4125,25', 'yes' , '4')

    def create(self, validated_data):
        return Checkin.objects.create(checkin_1)

    def update(self, instance, validated_data):
        instance.telephone = validated_data.get('telephone', instance.telephone)
        instance.name_client = validated_data.get('name_client', instance.name_client)
        instance.id_airbnb = validated_data.get('id_airbnb', instance.id_airbnb)
        instance.id_reserve = validated_data.get('id_reserve', instance.id_reserve)
        instance.daily = validated_data.get('daily', instance.daily)
        instance.payment = validated_data.get('payment', instance.payment)
        instance.checkin_hour = validated_data.get('checkin_hour', instance.checkin_hour)
        instance.bed_temperature = validated_data.get('bed_temperature', instance.bed_temperature)
        instance.price = validated_data.get('price', instance.price)
        instance.pet = validated_data.get('pet', instance.pet)
        instance.guests = validated_data.get('guests', instance.guests)

        instance.save()
        return instance

class CheckoutSerializer(serializers.Serializer):
    checkout = serializers.DateField()
    name_client = serializers.CharField(required=False, allow_blank=True, max_length=100)
    address_reserve = serializers.CharField(required=False, allow_blank=True, max_length=100)
    checkout_hour = serializers.TimeField(read_only=True)
    concluded = serializers.ChoiceField(choices=concluded_choices, default = 'pending')
    checkout_1 = {'checkout':'16/09/2021','name_client': 'Paulo da Silva', 'address_reserve': 'Avenida Búzios, 1800 Jurerê InternacIonal. Florianópolis-SC, CEP:8950-100','checkout_hour': '16:00', 'concluded':'pending'}
    def create(self, validated_data):
        return Checkout.objects.create(checkout_1)

    def update(self, instance, checkout_1):
        instance.checkout = checkout_1.get('checkout', instance.checkout)
        instance.name_client = checkout_1.get('name_client', instance.name_client)
        instance.checkout_hour = checkout_1.get('checkout_hour', instance.checkout_hour)
        instance.concluded = checkout_1.get('concluded', instance.concluded)
        instance.address_reserve = checkout_1.get('address_reserve', instance.address_reserve)

        instance.save()
        return instance

class HostSerializer(serializers.Serializer):
    name_host = serializers.CharField(read_only=True)
    classification = serializers.CharField(required=False, allow_blank=True, max_length=10)
    host_addresses = serializers.TimeField(read_only=True)
    host_1 = {'name_host': 'Eduarda Cardoso', 'classification': '9.67', 'host_addresses': 'Avenida Búzios, 1800 Jurerê InternacIonal. Florianópolis-SC, CEP:8950-100'}

    def create(self, validated_data):
        return Host.objects.create(host_1)

    def update(self, instance, validated_data):
        instance.name_host = validated_data.get('name_host', instance.name_host)
        instance.classification = validated_data.get('classification', instance.classification)
        instance.host_addresses = validated_data.get('host_addresses', instance.host_addresses)

        instance.save()
        return instance

class CleaningSerializer(serializers.Serializer):
    daily = serializers.IntegerField()
    id_cleaning = serializers.CharField(required=False, max_length=10)
    hour_cleaning = serializers.TimeField()
    cleaning_1 ={'daily':'9', 'id_cleaning':'UGJ678', 'hour_cleaning':'12:00'}

    def create(self, validated_data):
        return Cleaning.objects.create(cleaning_1)

    def update(self, instance, validated_data):
        instance.daily = validated_data.get('daily', instance.daily)
        instance.id_cleaning = validated_data.get('id_cleaning', instance.id_cleaning)
        instance.hour_cleaning = validated_data.get('hour_cleaning', instance.hour_cleaning)

        instance.save()
        return instance
