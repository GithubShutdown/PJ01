# myapp/forms.py
from django.contrib.auth import forms as auth_forms

class LoginForm(auth_forms.AuthenticationForm):
    def __init__(self, *args, **kw):
        super().__init__(*args, **kw)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label


from .models import *
from django import forms

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = SkypeMyNameModel
#         fields = ('user','skype_id' ,'images',)

class UploadForm(forms.ModelForm):
    class Meta:
        model = SkypeMyNameModel
        fields = ('skype_id' ,'images',)

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = FileUpload
#         fields = ('files',)

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('last_name', 'first_name')


# class WeatherForm(forms.Form):
#     data = [
#         ('Tokyo', 'Tokyo'),
#         ('Atami', 'Atami'),
#         ('Nagoya', 'Nagoya'),
#         ('Osaka', 'Osaka'),
#     ]
#     choice = forms.ChoiceField(label='radio', choice=data)

