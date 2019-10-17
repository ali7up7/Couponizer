from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from resterApp import viewsetters

rt = routers.DefaultRouter()
rt.register(r'mealer', viewsetters.ResterViewset)
rt.register(r'couponerClient', viewsetters.CouponerClientViewset)


urlpatterns = [
    path('adminer/', admin.site.urls),
    path('apier/', include(rt.urls))
]