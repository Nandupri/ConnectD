# filepath: c:\Users\varma\ConnectD\polls\admin.py
from django.contrib import admin
from .models import Question

admin.site.register(Question)
