from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *

from .models import Screen, Seat
from .serializers import ScreenSerializer, SeatSerializer

import json


class ScreenListView(APIView):

    def get(self, request):

        """ GET -  returns all screens """

        screens = Screen.objects.all()
        screens_serialized = ScreenSerializer(screens, many=True).data
        return Response(screens_serialized)

    def post(self, request):

        """ POST - add new Screen """

        response_dict = {}
        req_body = request.data
        screen_serializer = ScreenSerializer(data=req_body)
        if screen_serializer.is_valid():
            screen = screen_serializer.save()
            response_dict["message"] = "OK"
            response_dict["id"] = screen.id
            return Response(response_dict)
        response_dict["message"] = "FAIL"
        response_dict["errors"] = screen_serializer.errors
        return Response(response_dict, status=HTTP_400_BAD_REQUEST)


class ScreenView(APIView):

    def get(self, request, name):

        """ GET - details of a screen """

        response_dict = {}
        screen = Screen.objects.filter(name=name).first()
        if screen is None:
            response_dict["message"] = "Screen not found"
            return Response(response_dict, status=HTTP_404_NOT_FOUND)
        screen_serialized = ScreenSerializer(screen).data
        return Response(screen_serialized)

class SeatListView(APIView):






