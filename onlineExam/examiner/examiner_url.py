from django.urls import path
from examiner.views import *

urlpatterns=[
    path('examiner-login/',examinerLogin),
    path('examiner-loginValidate/',examinerLoginValidate),
    path('set-question/',examinerQuestionSet),
    path('save-question/',examinerQuestionSave),
    path('question-view/',examinerQuestionView),
    path('update-question',examinerQuestionUpdate),
    path('updation/',examinerQuestionUpdation),
    path('delete-question',examinerQuestionDelete),
    path('logout/',examinerLogout),
]