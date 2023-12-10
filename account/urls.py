from django.urls import path
from account.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name='home'),
    path('patient-register/', patientRegisterView, name='patient_register'),
    path('patient-login/', patientLogin, name='patient_login'),
    
    path('doctor-register/', doctorRegisterView, name='doctor_register'),
    path('doctor-login/', doctorLogin, name='doctor_login'),
    
    path('logout/', logout, name='logout'),
    path('profile/', Profile, name='profile'),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
