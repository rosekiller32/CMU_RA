# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.utils import timezone
from django.utils.translation import ugettext, ugettext_lazy as _


YES_NO = (
    ('yes', 'Yes'),
    ('no', 'No'),
)

GENDER =(
    ('male', 'Male'),
    ('female', 'Female'),
)

Authorization_Choice =(
    ('us citizen','US Citizen'),
    ('permanent alien','Permanent Alien'),
    ('temporary alien','Temporary Alien'),
    ('refugee','Refugee'),
)

CURRENT_EMPLOYMENT_STATUS_Choice =(
    ('employed full‐time','Employed Full‐time'),
    ('employed part‐time','Employed Part‐time'),
    ('temporary layoff','Temporary Layoff'),
    ('unemployed','Unemployed')
)

UNEMPLOYMENT_COMPENSATION_Choice =(
    ('receiving UC benefits','Receiving UC Benefits'),
    ('exhausted UC benefits','Exhausted UC Benefits'),
    ('not applicable','Not Applicable')
)

I_am_here_today_for_Choice = (
    ('Job Search','Job Search'), 
    ('Use Unemployment Compensation (UC) Phone','Use Unemployment Compensation (UC) Phone'), 
    ('Registration for UC Compliance','Registration for UC Compliance'),
    ('On‐Site Recruitment','On‐Site Recruitment'),
    ('Orientation','Orientation'),
    ('Workshop','Workshop'),
)

Program_Choices = (
    ('JobGateway® Registration','JobGateway® Registration'),
    ('UC – Filing for Benefits or Appeals','UC – Filing for Benefits or Appeals'),
    ('Veterans Services','Veterans Services'),
    ('Calendar of Events','Calendar of Events'),
    ('Labor Market Information','Labor Market Information'),
    ('Resume Assistance','Resume Assistance'),
    ('Job Search Planning/Career Counseling','Job Search Planning/Career Counseling'),
    ('Networking','Networking'),
    ('Interviewing','Interviewing'),
    ('Identifying Skills','Identifying Skills'),
    ('Civil Service/Government Jobs','Civil Service/Government Jobs'),
    ('Job Search Websites','Job Search Websites'),
    ('Supportive Services Information','Supportive Services Information'),
    ('Disability Resources','Disability Resources'),
    ('Tracking My Job Search','Tracking My Job Search'),
    ('Job Search Basics/Show Me the Jobs','Job Search Basics/Show Me the Jobs'),
    ('Starting a Business','Starting a Business'),
    ('Basic Computer Skills (Mouse, Keyboard, etc.)','Basic Computer Skills (Mouse, Keyboard, etc.)'),
    ('Computer Skills (MS Word, Outlook, etc.)','Computer Skills (MS Word, Outlook, etc.)'),
    ('Re‐Entry Resources','Re‐Entry Resources'),
    ('English as a Second Language (ESL)','English as a Second Language (ESL)'),
    ('Basic Reading/Writing/Math Skills','Basic Reading/Writing/Math Skills'),
    ('Obtaining an Occupational Certification or License','Obtaining an Occupational Certification or License'),
    ('Obtaining Your High School Equivalency Diploma','Obtaining Your High School Equivalency Diploma'),

)

Race= (
    ('American Indian/Alaskan Native','American Indian/Alaskan Native'),
    ('Asian','Asian'),
    ('Black/African American','Black/African American'),
    ('Hawaiian Native/other Pacific Islander','Hawaiian Native/other Pacific Islander'),
    ('White','White'), 
    ('Do not Wish to Disclose','Do not Wish to Disclose'),
)

Type_of_Discharge_Choices = (
    ('Honorable','Honorable'),
    ('Dishonorable','Dishonorable'),
    ('Other','Other'),
)


Branch_Of_Service = (
    ('Army','Army'),
    ('Army Reserves','Army Reserves'),
    ('Navy','Navy'),
    ('Navy Reserves','Navy Reserves'),
    ('Air Force','Air Force'),
    ('Air Force Reserves','Air Force Reserves'),
    ('Marines','Marines'), 
    ('Marine Reserves','Marine Reserves'), 
    ('Coast Guard','Coast Guard'),
    ('Coast Guard Reserves','Coast Guard Reserves'), 
    ('National Guard','National Guard'),
)


class Program(models.Model):
    name = models.CharField(max_length=300, choices=Program_Choices)
    def __str__(self):
        return self.name


class PersonalInformation(models.Model):
    created_by = models.ForeignKey(User, unique=True, related_name="PersonalInformations", default="",on_delete=models.PROTECT)
    creation_time = models.DateTimeField(default=timezone.now())
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    social_security_number = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    home_phone = models.CharField(max_length=16)
    cell_phone = models.CharField(max_length=16)
    fax = models.CharField(max_length=16)
    email = models.CharField(max_length=50)
    date_of_birth =  models.DateField()
    authorization_to_work_in_the_us = models.CharField(max_length=50,choices = Authorization_Choice)
    are_you_registered_in_JobGateway = models.CharField(max_length=50,choices = YES_NO)
    gender = models.CharField(max_length=10, choices = GENDER)
    how_did_you_hear_about_us = models.CharField(max_length=20)
    CareerLink_program = MultiSelectField(choices=Program_Choices,default= None)
    education = models.CharField(max_length=20)
    Most_Recent_Employer =  models.CharField(blank=True, max_length=20)
    Most_Recent_Job_Title =  models.CharField(blank=True, max_length=20)
    Most_Recent_Job_Start_Date = models.DateField(blank=True, null=True)
    Most_Recent_Job_End_Date =  models.DateField(blank=True, null=True)
    Wage_per_Hour = models.CharField(max_length=50, blank=True)
    Hours_Per_Week = models.CharField(max_length=50, blank=True)
    is_Hispanic =  models.CharField(max_length=3,choices = YES_NO)
    Race = models.CharField(max_length=50, choices = Race)
    


class MillitaryInformation(models.Model):  
    is_spouse = models.CharField(max_length=3, choices = YES_NO)

class VeteransInformation(models.Model):
    is_millitary_service =  models.CharField(max_length=3, choices = YES_NO)
    Service_relative_disability = models.CharField(max_length=3, choices = YES_NO)
    VA_Compensation = models.CharField(blank=True,max_length=3)
    Entry_Date = models.DateField(blank=True)
    Separation_Date =  models.DateField(blank=True)
    Type_of_Discharge = models.CharField(max_length=50, blank=True, choices = Type_of_Discharge_Choices)
    Milliatary_Badge = models.CharField(max_length=50, blank=True, choices = YES_NO)
    Your_Branch_of_Service = models.CharField(max_length=50, blank=True, choices = Branch_Of_Service)


class Application(models.Model):
    updated_by    = models.ForeignKey(User, related_name="post_updators",on_delete=models.PROTECT)
    update_time   = models.DateTimeField()
    def __unicode__(self):
        return 'post(id=' + str(self.id) + ')'



