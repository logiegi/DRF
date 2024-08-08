# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.forms.models import model_to_dict

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorChangeSerializer, MeasurementSerializer


# @api_view(['GET', 'POST', 'PATCH'])
# def sensor(request):
#     sensors = Sensor.objects.all()
#     ser = SensorSerializer(sensors, many=True)
#     return Response(ser.data)


class SensorView(APIView):
    def get(self, request):
        sensors = Sensor.objects.all()
        ser = SensorSerializer(sensors, many=True)
        return Response(ser.data)

    def post(self, request):
        post_new = Sensor.objects.create(
            name=request.data['name'],
            description=request.data['description']
        )
        return Response({'post': model_to_dict(post_new)})


class SensorChangeView(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorChangeSerializer


class OneSensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementView(APIView):
    def get(self, request):
        sensors = Measurement.objects.all()
        ser = MeasurementSerializer(sensors, many=True)
        return Response(ser.data)
    def post(self, request):
        serializer = MeasurementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




