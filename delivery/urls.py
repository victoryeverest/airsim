from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('set_pickup_location/', views.set_pickup_location, name='set_pickup_location'),
    path('set_delivery_location/', views.set_delivery_location, name='set_delivery_location'),
    path('track_drone_status/', views.get_drone_status, name='track_drone_status'),
    path('takeoff/', views.takeoff, name='takeoff'),
    path('move/', views.move_to_position, name='move'),
    path('end_mission/', views.end_mission_view, name='end_mission'),
    path('status/', views.get_drone_status, name='status'),
    path('check_conditions/', views.check_conditions, name='check_conditions'),
    path('takeoff/', views.takeoff, name='takeoff'),
    path('fly/', views.drone_control, name='drone_control'),


]
