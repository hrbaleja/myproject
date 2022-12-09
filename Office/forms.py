from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Office.models import Ourservice,Customer,Topic,Contactu
from captcha.fields import CaptchaField


  

class SignUpForm(UserCreationForm): 
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
  
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields:
                self.fields[field].widget.attrs.update({
                'class': ('form__field form__text') } )       
    class Meta:
      model = User
      fields = "first_name","last_name","username","password1","password2","email" 
    def save(self, commit=True):
        user = super (SignUpForm , self ).save(commit=False)       
        if commit :
            user.save()
        return user




class Customerform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': ('form__field form__text') } )  
   
    class Meta:
        model = Customer
        fields ="__all__"

class Topicform(forms.ModelForm):
    Title = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Enter New Topic',  'class': 'form__field form__text', }))

    class Meta:
        model = Topic
        fields ="__all__"

class Ourserviceform(forms.ModelForm):  
    class Meta:
        model = Ourservice
        fields ="__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': ('form__field form__text') } )  


class Contactuform(forms.ModelForm):  
    class Meta:
        model = Contactu
        fields ="__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': ('form__field form__text') } )  

