from django import forms
from account.models import *

class doctorRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'form-control',}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password'
  }))
  
  class Meta:
    model = Doctor
    fields = ['first_name', 'last_name', 'image', 'username', 'email', 'password', 'city', 'state', 'pincode']
  
  def clean(self):
    cleaned_data = super(doctorRegistrationForm, self).clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    
    if password != confirm_password:
      raise forms.ValidationError(
        "Password does not match!"
      )
  def __init__(self, *args, **kwargs):
    super(doctorRegistrationForm, self).__init__(*args, **kwargs)
    
    self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last name'
    self.fields['username'].widget.attrs['placeholder'] = 'Enter  Username'

    self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    self.fields['city'].widget.attrs['placeholder'] = 'Enter Your City'
    self.fields['state'].widget.attrs['placeholder'] = 'Enter Your State'
    self.fields['pincode'].widget.attrs['placeholder'] = 'Enter Your Pincode'
    
    
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control item'
 

class patientRegistrationForm(forms.ModelForm):
  password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter Password', 'class':'form-control',}))
  confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
    'placeholder': 'Confirm Password'
  }))
  
  class Meta:
    model = Patient
    fields = ['first_name', 'last_name', 'image', 'username', 'email', 'password', 'city', 'state', 'pincode']
  
  def clean(self):
    cleaned_data = super(patientRegistrationForm, self).clean()
    password = cleaned_data.get('password')
    confirm_password = cleaned_data.get('confirm_password')
    
    if password != confirm_password:
      raise forms.ValidationError(
        "Password does not match!"
      )
  def __init__(self, *args, **kwargs):
    super(patientRegistrationForm, self).__init__(*args, **kwargs)
    
    self.fields['first_name'].widget.attrs['placeholder'] = 'Enter First name'
    self.fields['last_name'].widget.attrs['placeholder'] = 'Enter Last name'
    self.fields['username'].widget.attrs['placeholder'] = 'Enter  Username'

    self.fields['email'].widget.attrs['placeholder'] = 'Enter Email Address'
    self.fields['city'].widget.attrs['placeholder'] = 'Enter Your City'
    self.fields['state'].widget.attrs['placeholder'] = 'Enter Your State'
    self.fields['pincode'].widget.attrs['placeholder'] = 'Enter Your Pincode'
    
    
    for field in self.fields:
      self.fields[field].widget.attrs['class'] = 'form-control item'
 



