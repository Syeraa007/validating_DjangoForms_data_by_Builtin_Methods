from django import forms
from django.core import validators

def validate_name(jelly):
    if jelly[0].lower()=='a':
        raise forms.ValidationError("Name shouldn't starts with A")
    
# def validate_len(value):
#     if len(value)<=5:
#         raise forms.ValidationError("Name should be more than 5 chars")

class Student(forms.Form):
    name=forms.CharField(max_length=100,validators=[validate_name,validators.MinLengthValidator(5)])
    age=forms.IntegerField(help_text='Enter age',label='Age')
    loc=forms.CharField(help_text='Enter location',label='Location')
    email=forms.EmailField(help_text='Enter email',label='Email')
    remail=forms.EmailField(help_text='Enter email',label='Re-Email')
    url=forms.URLField(label='URL',help_text='Enter URL')
    phone=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    botcatch=forms.CharField(label='Bot Catch',help_text='Enter bot catcher',required=False,widget=forms.HiddenInput)
    
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['remail']
        if e!=re:
            raise forms.ValidationError('No match found')
    def clean_botcatch(self):
        bot=self.cleaned_data['botcatch']
        if len(bot)>0:
            raise forms.ValidationError("Can't accept submitted data")