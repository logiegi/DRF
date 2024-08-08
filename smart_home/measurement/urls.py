from django.urls import path
from django.contrib import admin
from .views import SensorView, OneSensorView, SensorChangeView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('api/measurements/', MeasurementView.as_view()),
    path('api/sensors/', SensorView.as_view()),
    path('api/sensors/<pk>/', OneSensorView.as_view()),
    path('api/sensors/update/<pk>/', SensorChangeView.as_view()),
    path('api/measurements/update/', MeasurementView.as_view()),
]
