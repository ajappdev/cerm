# DJANGO DECLARATIONS
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.templatetags.static import static

# GENERAL DECLARATIONS
import pandas as pd
import os
from django.http import JsonResponse
import json
from readmrz import MrzDetector, MrzReader
import pytesseract
from datetime import date, datetime

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different

# APP DECLARATIONS
import app.models as am
import app.forms as af
import app.m00_common as m00

# DECLARING FONCTIONS
def landing_page(request):
    template = 'blank.html'

    context = {}
    return render(request, template, context)


def add_customer(request):
    template = 'customer/add-customer.html'
    context = {}
    return render(request, template, context)


def update_customer(request, pk: int):
    template = 'customer/update-customer.html'
    customer = am.Customer.objects.get(id=pk)
    context = {"customer": customer}
    return render(request, template, context)


def customers(request):
    template = 'customer/index.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Client créée avec succès"
    elif success_message == "updated":
        success_message = "Client modifié avec succès"
    else:
        success_message = ""

    customers = am.Customer.objects.all()
    context = {"customers": customers, "success_message": success_message}
    return render(request, template, context)


def register(request):
    register_form = af.RegisterForm()
    registration_errors = ""
    if request.method == "POST":
        register_form = af.RegisterForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()

            user_profile = am.UserProfile()
            user_profile.user = user
            user_profile.username = request.POST['username']
            user_profile.save()

            login(request, user)

            return redirect("/")
        else:
            registration_errors = register_form.errors

    template = 'registration/register.html'
    context = {
        "register_form": register_form,
        "registration_errors": registration_errors}
    return render(request, template, context)


def ajax_calls(request):
    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        action = received_json_data['action']

        if action == "upload_identity_files_add_customer":

            file_path = os.path.join(
                settings.STATIC_ROOT, 'uploads/passport.jpg')
            detector = MrzDetector()
            reader = MrzReader()
            image = detector.read(file_path)
            cropped = detector.crop_area(image)
            result = reader.process(cropped)
            result['country'] = next(item for item in m00.COUNTRY_CODES if item["alpha-3"] == result['nationality'])['name']
            result['birth_date'] = datetime.strptime(
                str(result['birth_date']),
                m00.DATE_PASSPORTS).strftime(m00.DATE_SHORT_LOCAL_WITH_SLASH)
            result['expiry_date'] = datetime.strptime(
                str(result['expiry_date']),
                m00.DATE_PASSPORTS).strftime(m00.DATE_SHORT_LOCAL_WITH_SLASH)
            data_dict = {"id_reading": result}

        if action == "delete_customer":
            error = 0
            error_text = ""
            try:
                am.Customer.objects.filter(
                    id=int(received_json_data['customer_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_CUSTOMER, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        if action == "save_customer":
            error = 0
            error_text = ""
            try:
                new_customer = am.Customer()
                new_customer.complete_name = received_json_data['customer_name']
                new_customer.identity_type = received_json_data['customer_type']
                new_customer.identity_number = received_json_data['customer_id']
                new_customer.identity_expire_date = received_json_data['customer_expire']
                new_customer.phone = received_json_data['customer_phone']
                new_customer.email = received_json_data['customer_email']
                new_customer.date_of_birth = received_json_data['customer_birth']
                new_customer.nationality = received_json_data['customer_nationality']
                new_customer.address = received_json_data['customer_address']
                new_customer.sex = received_json_data['customer_sex']
                new_customer.save()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, SAVE_CUSTOMER, 1, " + str(e)
                error = 1
            
            if received_json_data['customer_note'] != "" and error == 0:
                try:
                    new_customer_note = am.CustomerNotes()
                    new_customer_note.note = received_json_data['customer_note']
                    new_customer_note.customer = new_customer
                    new_customer_note.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, SAVE_CUSTOMER_NOTE, 2, " + str(e)
                    error = 1

            data_dict = {"error": error, "error_text": error_text}


        return JsonResponse(data=data_dict, safe=False)