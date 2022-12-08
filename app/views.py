# DJANGO DECLARATIONS
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import login
from os import listdir, path, remove, system, rename
from django.templatetags.static import static
import pandas as pd
import os
# APP DECLARATIONS
import app.models as am
import app.forms as af
import app.m01_pre_treatment as m01
import app.m02_describe as m02
import app.m03_decide_plots as m03
import app.m05_draw as m05

# DECLARING FONCTIONS
def upload_page(request):
    template = 'upload-page.html'
    context = {}
    return render(request, template, context)

def landing_page(request):
    template = 'blank.html'

    dataset_name = "ds4.xlsx"
    dataset_df = pd.read_excel(
        os.path.join(settings.STATIC_ROOT, 'datasets/' + dataset_name))

    pre_treatment = m01.PreTreatment(
        dataset_df)
    describe = m02.Describe(
        pre_treatment.dataset_df,
        pre_treatment.dataset_columns,
        pre_treatment.random_str)
    decide = m03.DecidePlots(
        describe.dataset_df,
        describe.dataset_columns,
        describe.category_columns,
        describe.date_columns,
        describe.month_columns,
        describe.week_columns,
        describe.random_str)
    draw = m05.DrawPlots(
        decide.dataset_df,
        decide.decided_plots,
        decide.dataset_columns,
        decide.category_columns,
        decide.random_str)

    context = {"plots": draw.plots}
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