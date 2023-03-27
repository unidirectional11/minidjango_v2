from django.contrib import admin

# Register your models here.
from jobs.models import Portal
from jobs.models import Person

admin.site.register(Portal)
admin.site.register(Person)
