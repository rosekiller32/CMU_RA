# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from datetime import timedelta
# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.utils import timezone
from django.core import serializers
from django.views.decorators.csrf import ensure_csrf_cookie

# Django transaction system so we can use @transaction.atomic
from django.db import transaction

# Imports the Item class
from CareerLink.models import Application, PersonalInformation, MillitaryInformation, VeteransInformation
from CareerLink.forms import RegistrationForm, CreateForm, EditForm
# Used to send mail from within Django
from django.core.mail import send_mail


# Used to generate a one-time-use token to verify a user's email address
from django.contrib.auth.tokens import default_token_generator


@login_required
def military_form(request):
    context={}
    return render(request, 'military_form.html', context)

@login_required
def applicant_certification_statement(request):
    context={}
    return render(request, 'applicant_certification_statement.html', context)

@login_required
def release_information(request):
    context={}
    return render(request, 'release_information.html', context)


@login_required
def grievance_policy(request):
    context={}
    return render(request, 'grievance_policy.html', context)


@login_required
def statement_right(request):
    context={}
    return render(request, 'statement_right.html', context)


@login_required
def failure_to_register(request):
    context={}
    return render(request, 'failure_to_register.html', context)

@login_required
def uc_claims(request):
    context={}
    return render(request, 'uc_claims.html', context)


@login_required
def userProfile(request):
    context={}
    return render(request, 'user.html', context)


@login_required
def application(request):
    context={'ifCreate': False}
    if PersonalInformation.objects.filter(created_by=request.user).exists():
        personalInformation = PersonalInformation.objects.get(created_by=request.user)
        context['Applications']=personalInformation
        context['ifCreate']=True
    return render(request, 'dashboard.html', context)


@login_required
def millitary(request):
    context={}
    context['form'] = MillitaryForm(request.POST)
    context['Veteranform'] = VeteransForm(request.POST)
    return render(request, 'millitaryForm.html', context)

# @login_required
# def applicationForm(request):
#     context={}
#     context['form'] = CreateForm(request.POST)
#     return render(request, 'applicationForm.html', context)


@transaction.atomic
def register(request):
    context = {}

    # Just display the registration form if this is a GET request.
    if request.method == 'GET':
        context['form'] = RegistrationForm()
        return render(request, 'register.html', context)

    # Creates a bound form from the request POST parameters and makes the
    # form available in the request context dictionary.
    form = RegistrationForm(request.POST)
    context['form'] = form

    # Validates the form.
    if not form.is_valid():
        return render(request, 'register.html', context)

    # At this point, the form data is valid.  Register and login the user.
    new_user = User.objects.create_user(username=form.cleaned_data['username'],
                                        password=form.cleaned_data['password1'],
                                        email=form.cleaned_data['email'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'])
    # Mark the user as inactive to prevent login before email confirmation.
    new_user.is_active = False
    new_user.save()

    # Generate a one-time use token and an email message body
    token = default_token_generator.make_token(new_user)

    email_body = """
Please click the link below to verify your email address and
complete the registration of your account:

  http://{host}{path}
""".format(host=request.get_host(),
           path=reverse('confirm', args=(new_user.username, token)))

    send_mail(subject="Verify your email address",
              message=email_body,
              from_email="hchiou@andrew.cmu.edu",
              recipient_list=[new_user.email])

    context['email'] = form.cleaned_data['email']
    return render(request, 'needs-confirmation.html', context)




@transaction.atomic
def confirmRegistration(request, username, token):
    try:
        user = get_object_or_404(User, username=username)
        # Send 404 error if token is invalid
        if not default_token_generator.check_token(user, token):
            raise Http404

        # Otherwise token was valid, activate the user.
        user.is_active = True
        user.save()
        return render(request, 'confirmed.html', {})
    except:
        raise Http404

@login_required
def create(request):
    if request.method == 'GET':
        context = { 'form': CreateForm() }
        return render(request, 'employment_status.html', context)
    entry = PersonalInformation(created_by=request.user, creation_time=timezone.now())
    create_form = CreateForm(request.POST, instance=entry)
    if not create_form.is_valid():
        print ("Not Succeessful")
        context = { 'form': create_form }
        return render(request, 'employment_status.html', context)
   
    # Save the new record
    create_form.save()

    message = 'Entry created'
    edit_form = EditForm(instance=entry)
    context = { 'message': message, 'PersonalInformation': entry, 'form': edit_form, 'ifCreate': False }
    if PersonalInformation.objects.filter(created_by=request.user).exists():
        personalInformation = PersonalInformation.objects.get(created_by=request.user)
        context['ifCreate']=True
    return render(request, 'dashboard.html', context)

@login_required
def customerSurvey(request):
    context = {}
    return render(request, 'customer_survey.html', context)



@login_required
@transaction.atomic
def edit(request):
    try:
        if request.method == 'GET':
            personalInformation = PersonalInformation.objects.get(created_by=request.user)
            form = EditForm(instance=personalInformation)
            context = { 'entry': personalInformation, 'form': form }
            return render(request, 'edit.html', context)
    
        personalInformation = PersonalInformation.objects.select_for_update().get(created_by=request.user)
        # db_update_time = personalInformation.update_time  # Copy timestamp to check after form is bound
        form = EditForm(request.POST, instance=personalInformation)
        if not form.is_valid():
            context = { 'entry': personalInformation, 'form': form }
            return render(request, 'edit.html', context)

        # if db_update_time != form.cleaned_data['update_time']:
        #     personalInformation = personalInformation.objects.get(created_by=request.user)
        #     form = EditForm(instance=personalInformation)
        #     context = {
        #         'message': 'Another user has modified this record.  Re-enter your changes.',
        #         'entry':   personalInformation,
        #         'form':    form,
        #     }
        #     return render(request, 'edit.html', context)

        # Set update info to current time and user, and save it!
        personalInformation.updated_by  = request.user
        form.save()

        # form = EditForm(instance=entry)
        context = {
            'message': 'Entry updated.',
            'entry':   personalInformation,
            'form':    EditForm(instance=personalInformation),
            'ifCreate': False,
        }
        if PersonalInformation.objects.filter(created_by=request.user).exists():
            personalInformation = PersonalInformation.objects.get(created_by=request.user)
            context['ifCreate']=True
        return render(request, 'dashboard.html', context)
    except PersonalInformation.DoesNotExist:
        context = { 'message': 'Record with id={0} does not exist'.format(id) }
        return render(request, 'edit.html', context)

@login_required
def delete(request):
    if request.method != 'POST':
        message = 'Invalid request.  POST method must be used.'
        return render(request, 'dashboard.html', { 'message': message })
    entry = get_object_or_404(PersonalInformation, created_by=request.user)
    entry.delete()
    message = ('Entry for {0}, {1} has been deleted.').format(entry.last_name, entry.first_name)
    return render(request, 'dashboard.html', { 'message': message })