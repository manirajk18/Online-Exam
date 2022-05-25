from django.urls import path
from examinee.views import *

urlpatterns=[
    path('new-examinee/',newExaminee),
    path('examinee-signup/',examineeRegistration),
]