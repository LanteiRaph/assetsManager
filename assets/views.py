from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.utils import timezone

import json
from datetime import date, datetime


from .helpers import get_report_sql, raw_query_sql
from .models import Equipment, General, ReturnDetail, RequestDetails, RequestList


# Define the Home page view
@method_decorator(login_required, name="dispatch")
class Home(TemplateView):
    # returns  a complete page with server side data.
    def get(self, request):
        # Before proceesind check if user is regiater in local db
        if request.user.last_login == timezone.now():
            # Get all the equipments
            equipments = Equipment.objects.all().select_related("make")
            # Paginate the eqipments for better user experince
            equipments_pages = Paginator(equipments, 8)
            page_number = request.GET.get("page")
            page_obj = equipments_pages.get_page(page_number)
            # Get All the general ewuipemtns
            generals = General.objects.all().select_related("make")
            # Get all the previous request for the current user
            prev_request = RequestList.objects.all().filter(user=request.user.id)
            # set the value for display
            context = {
                "equipment_pages": page_obj,
                "generals": generals,
                "user": request.user,
                "prev_request": prev_request
            }
            # render the tamplate with the data
            return render(request, "home.html", context=context)
        else:
            # Redirect the user to registration.
            return redirect('/onboarding/register-user/')


@method_decorator(login_required, name="dispatch")
class RequestDetail(TemplateView):

    def get(self, request, requestId):
        # Get details for the request
        requestDetails = raw_query_sql(get_report_sql(), [requestId])
        # Get the the request with its user type(Check is_staff to know deiffrence of student and lecturer)
        request_ = RequestList.objects.all().filter(request=requestId)
        #RequestDetails = RequestDetails.objects.all().select_related('equipment__make').filter(request=requestId)
        # Return the html code
        return render(
            request, "request-details.html", context={"requestDetails": requestDetails, "request": request_})

    def post(self, request):
        # Get the body of the reuest detail
        # Create the Detail
        # Link the detail to the requets
        # Save the record
        # Respond back to the user.
        return JsonResponse({})

    def put(self, request, requestdetailId):
        # Update the id given ID with the given payload
        # Get the record with the id
        # Update the values accodinlgy(Payload)
        # Respnde back to the user.
        return JsonResponse({})


@method_decorator(login_required, name="dispatch")
class Request(TemplateView):
    def get(self, request):
        # Respond back to the user with a page.
        return render(request, "request-list.html", context={})

    def post(self, request):
        # Get data from client
        payload = json.loads(request.body)
        # To make a request we need the current logged in user(Creat request with current user)
        request_ = RequestList(user=request.user, date_out=datetime.now())
        request_.save()
        # step throught the paylaod list and for each create a conditon and link to equipment and request.
        for condition in payload:
            # We need a condition,(Init to empyt unitl requsest is confired by admin)
            requestDetails_ = RequestDetails(date=datetime.now())
            equipment = Equipment.objects.get(pk=int(condition.get("Id")))
            # Attach the condition to the request
            requestDetails_.request = request_
            requestDetails_.equipment = equipment
            requestDetails_.qty = int(condition.get("qty"))
            requestDetails_.save()
        # Respond to the user with a success message
        return JsonResponse({"msg": "Request Succesfull", "request": request_.request})


# A Class that contiles the admin version of this application
# The get function retruns a poputalte page of the dashboard
# The post function returns the data based on the function name provived.
@method_decorator(login_required, name="dispatch")
class Control(TemplateView):
    def get(self, request):
        # Get all the equipments
        requestList = RequestList.objects.all().select_related(
            'user').annotate('request-details')
        # rendeer th data to the page
        return render(request, "dashbaord.html", context={'requestList': requestList})


class Return(TemplateView):
    # Create a new return record and link it th=o all the details of the cureent request
    def post(self, request, requestId):
        # Get the current date
        date = datetime.now()
        # Create the return detail to link to all the requestDetails
        returndetail = ReturnDetail(date_in=date)
        # Save the detail and get the primary key.
        returndetail.save()
        # Get all details for the given requst
        requestDetails = RequestDetails.objects.all().filter(request=requestId)
        # update the records.
        requestDetails.update(return_detail=returndetail)
        # return back to the user
        return JsonResponse({'msg': 'Success, Returned all request Items'})
