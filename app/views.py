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

        return JsonResponse(data=data_dict, safe=False)