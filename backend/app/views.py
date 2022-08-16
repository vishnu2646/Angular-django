from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from .models import *
from .serialzers import *
# Create your views here.
@csrf_exempt
def teamApi(request, id=0):
    if request.method == 'GET':
        teams = Team.objects.all()
        teams_seializers = TeamSerializer(teams, many=True)
        return JsonResponse(teams_seializers.data, safe=False)
    elif request.method == 'POST':
        team_data = JSONParser().parse(request)
        team_seializer = TeamSerializer(data=team_data)
        if team_seializer.is_valid():
            team_seializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('Failed to add team', safe=False)
    elif request.method == 'PUT':
        team_data = JSONParser().parse(request)
        team = Team.objects.get(teamId = team_data['teamId'])
        team_seializer = TeamSerializer(team, data=team_data)
        if(team_seializer.is_valid()):
            team_seializer.save()
            return JsonResponse("Updated team Successfully", safe=False)
        return JsonResponse("Team Failed to Updated", safe=False)
    elif request.method == 'DELETE':
        team = Team.objects.get(teamId = id)
        team.delete()
        return JsonResponse("Team Deleted successfully", safe=False)

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_seializers = EmployeeSerializer(employees, many=True, context={'request': request} )
        return JsonResponse(employees_seializers.data, safe=False)
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employee_seializer = EmployeeSerializer(data=employee_data)
        if employee_seializer.is_valid():
            employee_seializer.save()
            return JsonResponse('Added successfully', safe=False)
        return JsonResponse('Failed to add employee', safe=False)
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(employeeId = employee_data['employeeId'])
        employee_seializer = EmployeeSerializer(employee, data=employee_data)
        if(employee_seializer.is_valid()):
            employee_seializer.save()
            return JsonResponse("Updated employee Successfully", safe=False)
        return JsonResponse("Employee Failed to Updated", safe=False)
    elif request.method == 'DELETE':
        employee = Employee.objects.get(employeeId = id)
        employee.delete()
        return JsonResponse("Employee Deleted successfully", safe=False)