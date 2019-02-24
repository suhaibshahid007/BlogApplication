from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserLoginForm(forms.Form):
    username =forms.CharField()
    password =forms.CharField(widget=forms.PasswordInput)


class UserRegisterForm(forms.ModelForm):
    email = forms.EmailField(label='Email Address')
    email2 = forms.EmailField(label='Confirm Email')
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User

        fields =[
        'username',
        'email',
        'email2',
        'password',
    ]


    def clean_email2(self):
        email = self.cleaned_data.get("email")
        email2 =self.cleaned_data.get("email2")
        print(email , email2)
        if email != email2:
            raise forms.ValidationError("Email must Match")
        email_qs = User.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("This email is already registered !!! ")




