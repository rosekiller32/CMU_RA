# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple

from CareerLink.models import PersonalInformation, VeteransInformation, MillitaryInformation

from django.contrib.auth.models import User
from CareerLink.models import Program

from django.utils.translation import gettext_lazy as _

from django.utils.safestring import mark_safe


# YES_NO = (
#     ('yes', 'Yes'),
#     ('no', 'No'),
# )

# GENDER =(
#     ('male', 'Male'),
#     ('female', 'Female'),
# )

# Authorization_Choice =(
#     ('us citizen','US Citizen'),
#     ('permanent alien','Permanent Alien'),
#     ('temporary alien','Temporary Alien'),
#     ('refugee','Refugee'),
# )

# CURRENT_EMPLOYMENT_STATUS_Choice =(
#     ('employed full‐time','Employed Full‐time'),
#     ('employed part‐time','Employed Part‐time'),
#     ('temporary layoff','Temporary Layoff'),
#     ('unemployed','Unemployed')
# )

# UNEMPLOYMENT_COMPENSATION_Choice =(
#     ('receiving UC benefits','Receiving UC Benefits'),
#     ('exhausted UC benefits','Exhausted UC Benefits'),
#     ('not applicable','Not Applicable')
# )

# I_am_here_today_for_Choice = (
#     ('Job Search','Job Search'), 
#     ('Use Unemployment Compensation (UC) Phone','Use Unemployment Compensation (UC) Phone'), 
#     ('Registration for UC Compliance','Registration for UC Compliance'),
#     ('On‐Site Recruitment','On‐Site Recruitment'),
#     ('Orientation','Orientation'),
#     ('Workshop','Workshop'),
# )

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

# Race= (
#     ('American Indian/Alaskan Native','American Indian/Alaskan Native'),
#     ('Asian','Asian'),
#     ('Black/African American','Black/African American'),
#     ('Hawaiian Native/other Pacific Islander','Hawaiian Native/other Pacific Islander'),
#     ('White','White'), 
#     ('Do not Wish to Disclose','Do not Wish to Disclose'),
# )

# Type_of_Discharge_Choices = (
#     ('Honorable','Honorable'),
#     ('Dishonorable','Dishonorable'),
#     ('Other','Other'),
# )


# Brach_Of_Service = (
#     ('Army','Army'),
#     ('Army Reserves','Army Reserves'),
#     ('Navy','Navy'),
#     ('Navy Reserves','Navy Reserves'),
#     ('Air Force','Air Force'),
#     ('Air Force Reserves','Air Force Reserves'),
#     ('Marines','Marines'), 
#     ('Marine Reserves','Marine Reserves'), 
#     ('Coast Guard','Coast Guard'),
#     ('Coast Guard Reserves','Coast Guard Reserves'), 
#     ('National Guard','National Guard'),

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.CharField(max_length=50,
                            widget=forms.EmailInput())
    username = forms.CharField(max_length=20)
    password1 = forms.CharField(max_length=200,
                                label='Password',
                                widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=200,
                                label='Confirm password',
                                widget=forms.PasswordInput())

    # Customizes form validation for properties that apply to more
    # than one field.  Overrides the forms.Form.clean function.
    def clean(self):
        # Calls our parent (forms.Form) .clean function, gets a dictionary
        # of cleaned data as a result
        cleaned_data = super(RegistrationForm, self).clean()

        # Confirms that the two password fields match
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords did not match.")

        # We must return the cleaned data we got from our parent.
        return cleaned_data

    # Customizes form validation for the username field.
    def clean_username(self):
        # Confirms that the username is not already present in the
        # User model database.
        username = self.cleaned_data.get('username')
        if User.objects.filter(username__exact=username):
            raise forms.ValidationError("Username is already taken.")

        # We must return the cleaned data we got from the cleaned_data
        # dictionary
        return username


class CreateForm(ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = (
        'created_by',
        'creation_time',
        )
        labels = {
        'education': _('EDUCATION: '),
        'is_Hispanic':_('Considered to be of Hispanic Heritage?'),
        } 
        widgets = {
            # 'date_of_birth' :  extras.SelectDateWidget(years=range(1950, 2019)),
            # 'Most_Recent_Job_Start_Date' :  extras.SelectDateWidget(years=range(1950,2019)),
            # 'Most_Recent_Job_End_Date' : extras.SelectDateWidget(years=range(1950, 2019)),
            'update_time': forms.HiddenInput(),
        }
        attrs={
            'class': 'form-control',
        }


class EditForm(ModelForm):
    class Meta:
        model = PersonalInformation
        exclude = (
            'created_by',
            'creation_time',
        )
        labels = {
            'bio': _('EDUCATION: Highest Grade/Diploma/College or VoTech Classes/Degree completed'),
            'is_Hispanic':_('Considered to be of Hispanic Heritage?'),
        }
        widgets = {
            'update_time': forms.HiddenInput(),
            # 'date_of_birth' :  extras.SelectDateWidget(),
            # 'Most_Recent_Job_Start_Date' :  extras.SelectDateWidget(years=range(1950, 2019)),
            # 'Most_Recent_Job_End_Date' : extras.SelectDateWidget(years=range(1950, 2019)),
        }
        attrs={
            'class': 'form-control',
        }
    


class MillitaryForm(ModelForm):
    class Meta:
        model = MillitaryInformation
        fields = '__all__'
        labels = {
            'is_spouse': _('Are you the Spouse of a veteran as defined above?'),
        }

class EditMillitaryForm(ModelForm):
    class Meta:
        model = MillitaryInformation
        fields = '__all__'
        labels = {
            'is_spouse': _('Are you the Spouse of a veteran as defined above?'),
        }


class VeteransForm(ModelForm):
    class Meta:
        model = VeteransInformation
        fields = '__all__'
        labels = {
            'Entry_Date': _('Entry Date(Anticipated):'),
        }
        widgets = {
            # 'Entry_Date' :  extras.SelectDateWidget(years=range(1950, 2019)),
            # 'Separation_Date' :  extras.SelectDateWidget(years=range(1950, 2019)),
        }

class EditVeteransForm(ModelForm):
    class Meta:
        model = VeteransInformation
        fields = '__all__'
        labels = {
            'Entry_Date': _('Entry Date(Anticipated):'),
        }
        widgets = {
            # 'Entry_Date' :  extras.SelectDateWidget(years=range(1950, 2019)),
        # 'Separation_Date' :  extras.SelectDateWidget(),
        }
    



class ImageUploadForm(forms.Form):
    image = forms.ImageField()
    def clean_picture(self):
        picture = self.cleaned_data['picture']
        if not picture:
            raise forms.ValidationError('You must upload a picture')
        if not picture.content_type or not picture.content_type.startswith('image'):
            raise forms.ValidationError('File type is not image')
        if picture.size > MAX_UPLOAD_SIZE:
            raise forms.ValidationError('File too big (max size is {0} bytes)'.format(MAX_UPLOAD_SIZE))
        return picture

        






