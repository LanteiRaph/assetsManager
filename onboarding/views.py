from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from django.views.generic import ListView
import json


from .handlers import staffHandler, studentHandler



class Home(View):
    def get(self, request):
        return render(request, 'onboarding.html', context={'name': 'Hello World'})


class RegisterUser(View):
    def get(self, request):
        return render(request, 'registration.html', context={})

    def post(self, request):
        # From user type create the appropriets table
        payload = json.loads(request.body)

        if payload.get('user_type') == 'student':
            studentHandler(payload)
        else:
            staffHandler(payload)

        # link the user to the department
        return JsonResponse({'msg': 'success', "payload": payload})

