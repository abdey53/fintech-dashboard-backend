from django.contrib import admin
from .models import User, FinancialRecord

# Register your models here.

admin.site.register(User)
admin.site.register(FinancialRecord)

