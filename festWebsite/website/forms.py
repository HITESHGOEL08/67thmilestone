from django import forms
from website.models import Campus_Ambassdors


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
