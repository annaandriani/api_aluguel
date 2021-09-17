from snippets.serializers import HostSerializer, CleaningSerializer, CheckinSerializer, CheckoutSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def Host_list(request, format=None):
    if request.method == 'GET':
        host_1 = {'name_host': 'Eduarda Cardoso', 'classification': '9.67', 'host_addresses': 'Avenida Búzios, 1800 Jurerê InternacIonal. Florianópolis-SC, CEP:8950-100'}
        serializer = HostSerializer(host_1)
        return Response(serializer.data)

@api_view(['GET'])
def Cleaning_list(request, format=None):
    if request.method == 'GET':
        cleaning_1 = {'daily': '9', 'id_cleaning':'UGT215', 'hour_cleaning':'12:00'}
        serializer = CleaningSerializer(cleaning_1)
        return Response(serializer.data)


@api_view(['GET'])
def Checkout_list(request, format=None):
    if request.method == 'GET':
        checkout_1 = {'checkout': '16/09/2021', 'name_client': 'Paulo da Silva', 'address_reserve': 'Avenida Búzios, 1800 Jurerê InternacIonal. Florianópolis-SC, CEP:8950-100', 'checkout_hour': '16:00', 'concluded': 'pending'}
        serializer = CheckoutSerializer(checkout_1)
        return Response(serializer.data)

    elif request.method == 'POST':
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def Checkin_list(request, format=None):
    if request.method == 'GET':
        checkin_1 = {'telephone':'47999876544', 'name_client':'Gabriela da Silva', 'id_airbnb':'ADJ275', 'id_reserve':'HMYDPRK5FS','address_reserve':'Avenida Búzios, 1800 Jurerê InternacIonal. Florianópolis-SC, CEP:8950-100','daily':'9','payment':'pending','checkin_hour':'14:00', 'bed_temperature_choices':'hot', 'price': '4125', 'pet':'yes', 'guests':'4', 'checkin_day':'16/09/2021'}
        serializer = CheckinSerializer(checkin_1)
        return Response(serializer.data)





