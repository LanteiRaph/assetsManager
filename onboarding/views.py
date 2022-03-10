from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
import json


class Home(View):
    def get(self, request):
        return render(request, 'onboarding.html', context={'name': 'Hello World'})


class RegisterUser(View):
    def get(self, request):
        #Render the regisrtration page.
        return render(request, 'registration.html', context={})

    def post(self, request):
        # From user type create the appropriets table
        payload = json.loads(request.body)

        # link the user to the department
        return JsonResponse({'msg': 'success', "payload": payload})

