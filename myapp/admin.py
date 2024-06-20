from django.contrib import admin
from .models import resumedata

# Register your models here.
@admin.register(resumedata)

class adminform(admin.ModelAdmin):
    list_display=['name','skills','date','genders','locality','city','pin','state','mobile','email',
                'job_city','profile','my_file']
