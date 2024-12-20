from django.contrib import admin
from home.models import Task


# Register the model along with the TaskAdmin class
admin.site.register(Task)
