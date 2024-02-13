from django.contrib import admin

# comment all here if new database
from .models import User, Engage_Partners_Table
# Register your models here.

admin.site.register(User)

admin.site.register(Engage_Partners_Table)

# ------------------------------- until here