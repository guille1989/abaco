from django import forms
from django.contrib.auth.forms import UserCreationForm
from guilletest.models import User
from guilletest.models import TextInputs

#Class for users to make registration
class RegistrationForm(UserCreationForm):    
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        # Disable password validation errors
        for field_name in ['password1', 'password2']:
            self.fields[field_name].error_messages = {'password_mismatch': ''}

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

#Class for the text input field with limit of 140 characteres
class MyTextInputForm(forms.ModelForm):
    user_name = forms.CharField(label='', max_length=140, widget=forms.TextInput(attrs={'id': 'userInput'}))
    text = forms.CharField(label='', max_length=140, widget=forms.Textarea(attrs={'id': 'textArea'}))

    class Meta:
        model = TextInputs
        fields = ('text', 'user_name')
