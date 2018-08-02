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

import base64
from tomy.salt import saltgen

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
        try:
            _message = "try to retrive post data"
            print(_message)
            postdata = self.request.POST.get("enc")
            _message = "data retrived"
            print(postdata)
            try:
                _message = "parsing data"
                print(_message)
                head,normalized = postdata.split(",")
                print("headder")
                print(head)
                print("encoded data")
                print(normalized)
                _message = "data decoded sucess"
                image_name = "../media/"+saltgen(5) + ".jpeg"
                fh = open(image_name, "wb")
                fh.write(normalized.decode('base64'))
                fh.close()
            except:
                _message = "unable to parse data"
        except:
            _message = "unable to pase data"
            print(_message)
        
        resp = {
            "status" : _status,
            "message" : _message
        }
        return Response(resp, status=status.HTTP_200_OK)

