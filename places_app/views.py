from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from requests import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from .models import ItemLocation,UserP
from .serialization import ItemLocationSerializers
import requests

# Create your views here.


def say_hay(request):
    return HttpResponse('whellcome')


@api_view(['POST'])
def signup(request):
    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email", None)
    phone = request.data.get("phone",None)
    address = request.data.get("address",None)
    user = UserP.objects.create_user(username=username, password=password, email=email, phone=phone, address=address)
    token = Token.object.create(user=user)
    data = {'user_name': user.username, 'token': token}
    return Response(f"new user created. id:{user.id},token {data}")


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def check_token(request):
    return Response(f"this is  a privet response {request.user.username}", 200)


@api_view(['POST'])
def login(request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email", None)
        phone = request.data.get("phone",None)
        address = request.data.get("address",None)


@api_view (['GET'])
def show_list(request):
    list_location = ItemLocation.objects.all()
    item_data = ItemLocationSerializers(list_location, many=True).data
    return Response(item_data)


def search_item(request):
        search_location = request.POST['search_location']
        item_list = ItemLocation.objects.filter(ItemLocation__congtains=search_location)
        return JsonResponse(item_list)


@api_view(['POST'])
def create_ItemLocation(request):
    if request.method == 'POST':
        id_I = request.data.get("id_I")
        item_name = request.data.get("item_name")
        num_pepole = request.data.get("num_pepole")
        owner = request.data.get("owner")
        city = request.data.get("city")
        search_id = ItemLocation.objects.filter(id_I)
        if id_I != search_id:
            location = ItemLocation(id_I=id_I, item_name=item_name, num_pepole=num_pepole, owner=owner, city=city)
            if location.is_valid():
                location.save()
                return ("o.k")
            else:
                return ("Error")