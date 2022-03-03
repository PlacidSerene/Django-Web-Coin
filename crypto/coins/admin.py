from django.contrib import admin
from .models import User, Payment, Asset
# Register your models here.

admin.site.register(User)
admin.site.register(Payment)
admin.site.register(Asset)