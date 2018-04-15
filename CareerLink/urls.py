from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^$', views.application, name='home'),
    url(r'^application$', views.application, name='application'),
    # url(r'^applicationForm$', views.applicationForm, name='applicationForm'),
    url(r'^delete$', views.delete, name='delete'),
    url(r'^edit$', views.edit, name='edit'),
    url(r'^create$', views.create, name='create'),
    url(r'^military_form$', views.military_form, name='military_form'),
    url(r'^applicant_certification_statement$', views.applicant_certification_statement, name='applicant_certification_statement'),
    url(r'^release_information$', views.release_information, name='release_information'),
    url(r'^grievance_policy$', views.grievance_policy, name='grievance_policy'),
    url(r'^statement_right$', views.statement_right, name='statement_right'),
    url(r'^failure_to_register$', views.failure_to_register, name='failure_to_register'),
    url(r'^uc_claims$', views.uc_claims, name='uc_claims'),
    url(r'^customerSurvey$', views.customerSurvey, name='customerSurvey'),
    url(r'^millitary$', views.millitary, name='millitary'),
    url(r'^userProfile$', views.userProfile, name='userProfile'),
    url(r'^profile$', views.application, name='profile'),
    url(r'^register$', views.register, name='register'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', auth_views.login, {
        'template_name': 'login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
    url(r'^confirm-registration/(?P<username>[a-zA-Z0-9]+)/(?P<token>[a-z0-9\-]+)$',
        views.confirmRegistration, name='confirm'),
]
