from django.contrib import admin

# Register your models here.
from examiner.models import questionbank,examiner
admin.site.register(questionbank)
admin.site.register(examiner)
