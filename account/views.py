from django.shortcuts import render, redirect, get_object_or_404
from account.forms import doctorRegistrationForm, patientRegistrationForm
from account.models import Doctor, Patient
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View

# Create your views here.

def home(request):
  return render(request, 'home.html')

########### Register Patient Account ############
def patientRegisterView(request):
  if request.method == 'POST':
    form = patientRegistrationForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      image = form.cleaned_data['image']
      
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      city = form.cleaned_data['city']
      state = form.cleaned_data['state']
      pincode = form.cleaned_data['pincode']
      # username = email.split('@')[0]
      
      user = Patient.objects.create_user(first_name=first_name, last_name=last_name,  username = username,  email=email,password=password)
      user.image = image
      user.city = city
      user.state = state
      user.pincode = pincode
      
      user.save()

      auth.login(request, user)
      return redirect('profile')
  else:
    form = patientRegistrationForm()
 
  context = {
    'form':form,
  }
  return render(request, 'patient/signup.html', context)

########### Login Patient Account ############
def patientLogin(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']   
    user = auth.authenticate(email=email, password = password)
   
    if user is not None:
      
      if user.is_patient == True:
        auth.login(request, user)
        return redirect('profile')
      else:
        messages.success(request, 'You are not register Patient.')
        return redirect('patient_login')
    else:
      messages.success(request, 'Invalid login credentials')
      return redirect('patient_login')
  return render(request, 'patient/login.html')

########### Register Doctor Account ############
def doctorRegisterView(request):
  if request.method == 'POST':
    form = doctorRegistrationForm(request.POST, request.FILES)
    print(form)
    if form.is_valid():
      print("IMage idiie", form.cleaned_data['image'])
      first_name = form.cleaned_data['first_name']
      last_name = form.cleaned_data['last_name']
      image = form.cleaned_data['image']
      username = form.cleaned_data['username']
      email = form.cleaned_data['email']
      password = form.cleaned_data['password']
      city = form.cleaned_data['city']
      state = form.cleaned_data['state']
      pincode = form.cleaned_data['pincode']
      # username = email.split('@')[0]
      
      print(form.cleaned_data['image'])
      
      user = Doctor.objects.create_user(first_name=first_name, last_name=last_name,  username = username,  email=email,password=password)
      user.image = image
      user.city = city
      user.state = state
      user.pincode = pincode
      
      user.save()

      auth.login(request, user)
      return redirect('profile')
  else:
    form = doctorRegistrationForm()
 
  context = {
    'form':form,
  }
  return render(request, 'doctor/signup.html', context)

########### Login Doctor Account ############
def doctorLogin(request):
  if request.method == 'POST':
    email = request.POST['email']
    password = request.POST['password']   
    user = auth.authenticate(email=email, password = password)
   
    if user is not None:
      
      if user.is_doctor == True:
        auth.login(request, user)
        return redirect('profile')
      else:
        messages.success(request, 'You are not register Doctor.')
        return redirect('doctor_login')
    else:
      messages.success(request, 'Invalid login credentials')
      return redirect('doctor_login')
  return render(request, 'doctor/login.html')



########### logout Teacher Account ############
@login_required(login_url='login')
def logout(request):
  auth.logout(request)
  messages.success(request, 'Your are logged out.')
  return redirect('home')
  
########### Profile  ############
@login_required(login_url='login')
def Profile(request):
  return render(request, 'profile.html')

