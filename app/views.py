# DJANGO DECLARATIONS
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.templatetags.static import static
from django.template.loader import render_to_string
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

# GENERAL DECLARATIONS
import pandas as pd
import os
from django.http import JsonResponse
import json
from readmrz import MrzDetector, MrzReader
import pytesseract
from datetime import date, datetime
from os import path
from shutil import move

pytesseract.pytesseract.tesseract_cmd = 'C:/Users/user/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'  # your path may be different
# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'  # your path may be different
# APP DECLARATIONS
import app.models as am
import app.forms as af
import app.m00_common as m00

# DECLARING FONCTIONS
def upload_page(request):
    template = 'upload-page.html'
    context = {}
    return render(request, template, context)

def landing_page(request):
    template = 'blank.html'

    context = {}
    return render(request, template, context)


def add_transaction(request):
    template = 'transaction/add-transaction.html'
    context = {}
    return render(request, template, context)


def add_customer(request):
    template = 'customer/add-customer.html'
    context = {}
    return render(request, template, context)


def update_customer(request, pk: int):
    template = 'customer/update-customer.html'
    customer = am.Customer.objects.get(id=pk)
    customer_notes = am.CustomerNotes.objects.filter(
        customer=customer).order_by("-created_at")
    customer_id_file = path.join(
        settings.MEDIA_ROOT, str(customer.id) + ".jpg")
    customer_id_file = customer_id_file.replace("\\", "&C&R&")
    context = {"customer": customer, "customer_id_file": customer_id_file, "customer_notes": customer_notes}
    return render(request, template, context)


def update_transaction(request, pk: int):
    template = 'transaction/update-transaction.html'
    transaction = am.Transaction.objects.get(id=pk)
    transactions_notes = am.TransactionNotes.objects.filter(
        transaction=transaction).order_by("-created_at")
    context = {"transaction": transaction, "transactions_notes": transactions_notes}
    return render(request, template, context)


def customers(request):
    template = 'customer/index.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Client créé avec succès"
    elif success_message == "updated":
        success_message = "Client modifié avec succès"
    else:
        success_message = ""

    customers = am.Customer.objects.all()
    context = {"customers": customers, "success_message": success_message}
    return render(request, template, context)


def transactions(request):
    template = 'transaction/index.html'

    success_message = request.GET.get('success_message')
    if success_message == "creation":
        success_message = "Transaction créée avec succès"
    elif success_message == "updated":
        success_message = "Transaction modifiée avec succès"
    else:
        success_message = ""

    transactions = am.Transaction.objects.all()
    context = {"transactions": transactions, "success_message": success_message}
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

@csrf_exempt
def upload_id_file(request):
    if request.method == 'POST':
        files = request.FILES.getlist("0")

        for f in files:
            fs = FileSystemStorage(path.join(
                settings.MEDIA_ROOT))
            filename = fs.save(request.POST['key'] + ".jpg", f)
        try:
            file_path = os.path.join(
                settings.MEDIA_ROOT, request.POST['key'] + ".jpg")
            if request.POST['key'] == "PASSPORT":
                result = m00.process_id_card(file_path)
            else:
                result = m00.process_passport(file_path)
            data_dict = {"MRZ_found": 1, "id_reading": result, "tmp_file": request.POST['key'] + ".jpg"}
        except Exception as e:
            print(e)
            data_dict = {"MRZ_found": 0, "tmp_file": request.POST['key'] + ".jpg"}

        return JsonResponse(data=data_dict, safe=False)

def ajax_calls(request):

    if request.method == 'POST':
        received_json_data = json.loads(request.body)
        action = received_json_data['action']

        if action == "filter_customers_list":

            customer_name_or_id = received_json_data['customer_name_or_id']
            customer_nationality = received_json_data['customer_nationality']
            customer_type = received_json_data['customer_type']
            page = received_json_data['page']
    
            customers = am.Customer.objects.filter(
                Q(complete_name__icontains=customer_name_or_id) |
                Q(identity_number__icontains=customer_name_or_id),
                nationality__icontains=customer_nationality
            )

            customers = [
                c for c in customers if customer_type in c.type_customer()]

            customers_list = m00.pagination(page, 1, customers)

            html = render_to_string(
                        template_name="customer/customers-table.html", 
                        context={
                            "customers": customers_list,
                        }
                    )
            data_dict = {"html": html}

        elif action == "get_my_customers":
            initials = received_json_data['initials']
            my_customers = am.Customer.objects.filter(
                Q(complete_name__icontains=initials) |
                Q(identity_number__icontains = initials))[: 15]
            html = render_to_string(
                        template_name="general-widgets/customers-list.html", 
                        context={
                            "my_customers": my_customers,
                        }
                    )
            data_dict = {"html": html}


        elif action == "delete_customer":
            error = 0
            error_text = ""
            try:
                am.Customer.objects.filter(
                    id=int(received_json_data['customer_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_CUSTOMER, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "delete_transaction":
            error = 0
            error_text = ""
            try:
                am.Transaction.objects.filter(
                    id=int(received_json_data['transaction_id'])).delete()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, DELETE_TRANSACTION, 1, " + str(e)
                error = 1
            data_dict = {"error": error, "error_text": error_text}

        elif action == "save_transaction":
            error = 0
            error_text = ""
            
            if received_json_data['transaction_id'] == 0:
                transaction = am.Transaction()
            else:
                transaction = am.Transaction.objects.get(
                    id=int(received_json_data['transaction_id']))
            try:
                transaction.transaction_type = received_json_data['transaction_type']
                transaction.currency = received_json_data['transaction_currency']
                transaction.amount = received_json_data['transaction_amount']
                transaction.rate = received_json_data['transaction_rate']
                transaction.customer = am.Customer.objects.get(id=int(received_json_data['customer_id']))
                transaction.save()
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, SAVE_TRANSACTION, " + str(e)
                error = 1

            if received_json_data['transaction_note'] != "" and error == 0:
                try:
                    new_transacton_note = am.TransactionNotes()
                    new_transacton_note.note = received_json_data['transaction_note']
                    new_transacton_note.transaction = transaction
                    new_transacton_note.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, SAVE_TRANSACTION_NOTE, " + str(e)
                    error = 1

            data_dict = {"error": error, "error_text": error_text}

        elif action == "save_customer":
            error = 0
            error_text = ""
            
            if received_json_data['cus_id'] == 0:
                customer = am.Customer()
            else:
                customer = am.Customer.objects.get(
                    id=int(received_json_data['cus_id']))
            try:
                customer.complete_name = received_json_data['customer_name']
                customer.identity_type = received_json_data['customer_type']
                customer.identity_number = received_json_data['customer_id']
                customer.identity_expire_date = received_json_data['customer_expire']
                customer.phone = received_json_data['customer_phone']
                customer.email = received_json_data['customer_email']
                customer.date_of_birth = received_json_data['customer_birth']
                customer.nationality = received_json_data['customer_nationality']
                customer.address = received_json_data['customer_address']
                customer.sex = received_json_data['customer_sex']
                customer.save()
                print(received_json_data['customer_key'])
                old_file = path.join(
                    settings.MEDIA_ROOT, received_json_data['customer_key'] + ".jpg")
                new_file = path.join(
                    settings.MEDIA_ROOT, str(customer.id) + ".jpg")
                move(old_file, new_file)
            except Exception as e:
                error_text = "EXCEPTION, AJAX_CALLS, SAVE_CUSTOMER, " + str(e)
                error = 1

            if received_json_data['customer_note'] != "" and error == 0:
                try:
                    new_customer_note = am.CustomerNotes()
                    new_customer_note.note = received_json_data['customer_note']
                    new_customer_note.customer = customer
                    new_customer_note.save()
                except Exception as e:
                    error_text = "EXCEPTION, AJAX_CALLS, SAVE_CUSTOMER_NOTE, " + str(e)
                    error = 1

            data_dict = {"error": error, "error_text": error_text}


        return JsonResponse(data=data_dict, safe=False)