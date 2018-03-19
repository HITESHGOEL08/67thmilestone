from django import forms
from website.models import Campus_Ambassdors,FestAccomodation
from website.models import UserProfile
from django.contrib.auth.models import User

class Campus_Ambassdor_Form(forms.ModelForm):
    email = forms.EmailField(max_length=100, required=True, help_text="Email",
                             widget=forms.EmailInput(attrs={'class': 'validate', 'input': 'email'}))
    phone = forms.CharField(required=True, help_text="WhatsApp Number",
                            widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text', 'maxlength': '10'}))
    college_name = forms.CharField(max_length=100, required=True, help_text="College Name",
                                   widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    college_address = forms.CharField(max_length=300, required=True, help_text="College Address",
                                      widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    ca_code = forms.CharField(max_length=50, required=True, help_text="Any CA Code?", widget=forms.TextInput(
        attrs={'placeholder': "Enter NO, if you don't have any such code!", 'class': 'validate', 'input': 'text'}))
    reason_ca = forms.CharField(widget=forms.Textarea(attrs={'class': 'materialize-textarea', 'data-length': '500'}),
                                max_length=500, required=True, help_text="Why do you want to be a Campus Ambassador?")
    name = forms.CharField(max_length=100, help_text="Full Name", required=True,
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    slug = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Campus_Ambassdors
        fields = ('name', 'email', 'phone', 'college_name', 'college_address', 'ca_code', 'reason_ca')

class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=100, required=True, help_text="Username",
                                   widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    password = forms.CharField(widget = forms.PasswordInput(),required=True, help_text="Password")
    email = forms.EmailField(max_length=100, required=True, help_text="Email",
                             widget=forms.EmailInput(attrs={'class': 'validate', 'input': 'email'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, help_text="Name",
                               widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    contact = forms.CharField(required=True, help_text="Phone Number",
                            widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text', 'maxlength': '10'}))
    college = forms.CharField(max_length=100, required=True, help_text="College Name",
                           widget=forms.TextInput(attrs={'class': 'validate', 'input': 'text'}))
    gender = forms.ChoiceField(choices = [('0', 'Female'), ('1', 'Male'), ('2', 'Other')],help_text="")
    picture = forms.ImageField(required=False, help_text="", widget=forms.FileInput(attrs={'type': 'file'}))
    # Terms_and_Conditions = forms.BooleanField(required=True, help_text="Terms and Conditions", widget=forms.TextInput(attrs={'class': 'validate', 'type': 'checkbox'}))
    class Meta:
        model = UserProfile
        fields = ('name','contact', 'college', 'gender', 'picture', 'Terms_and_Conditions')

class FestAccomodationForm(forms.ModelForm):
    day1 = forms.BooleanField(required=False, label="4th April 12:00 pm to 5th April 12:00 pm", widget=forms.CheckboxInput())
    day2 = forms.BooleanField(required=False,label="5th April 12:00 pm to 6th April 12:00 pm", widget=forms.CheckboxInput())
    day3 = forms.BooleanField(required=False,label="6th April 12:00 pm to 7th April 12:00 pm", widget=forms.CheckboxInput())
    day4 = forms.BooleanField(required=False,label="7th April 12:00 pm to 8th April 12:00 pm", widget=forms.CheckboxInput())
    date = forms.DateField(label="Expected Check in Date", widget=forms.widgets.DateInput(attrs={'type':'date'}))
    time = forms.TimeField(label="Expected Check in Time", widget=forms.widgets.TimeInput(attrs={'type':'time'}))
    class Meta:
        model = FestAccomodation
        fields = ('day1', 'day2', 'day3', 'day4', 'date', 'time')