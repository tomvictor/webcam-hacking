from django.shortcuts import render


from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from rest_framework import status
from rest_framework.response import Response
from django.core import serializers
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.views import APIView

from django.views import View
# Create your views here.

from django.conf import settings
import sys
import base64
from tomy.salt import saltgen
from .models import Log

class EntryPoint(APIView):
    # queryset = FoodMenu.objects.all()
    permission_classes = [AllowAny]

    def get(self,*args,**kwargs):
        resp = {
            "status" : "0",
            "message" : "get method is not allowed"
        }
        return Response(resp,status=status.HTTP_404_NOT_FOUND)
    
    def post(self, *args, **kwargs):
        _status = 0
        _message = "sucess"
        # print(settings.BASE_DIR)
       

        try:
            _message = "try to retrive post data"
            print(_message)
            data = self.request.data
            _message = "data retrived"
            print(data)
            postdata = data["enc"]
            _message = "parsing data"
            print(_message)
            head,normalized = postdata.split(",")
            print("headder")
            print(head)
            print("encoded data")
            print(normalized)
            _message = "data decoded sucess"
            image_name =  saltgen(5) + ".jpeg"
            full_url = settings.BASE_DIR + "/media/" + image_name
            print(full_url)
            fh = open(full_url, "wb")
            fh.write(base64.b64decode(normalized))
            fh.close()
            _message = "image saved sucess"
            this = Log(image_url=image_name)
            this.save()
            _message = "db updates sucess"
            _status = 1
        except:
            _message = "error occured after : {0}".format(_message)
            print(_message)
        
        resp = {
            "status" : _status,
            "message" : _message
        }
        return Response(resp, status=status.HTTP_200_OK)

