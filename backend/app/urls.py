from django.urls import path
from .views import *

urlpatterns = [
    path('team/', teamApi),
    path('team/<str:id>/', teamApi),

    path('employee/', employeeApi),
    path('employee/<str:id>/', employeeApi),
]
