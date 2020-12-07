from django.contrib import admin

# Import Model from App
from .models import Users

# Register Model for Admin App
admin.site.register(Users)
