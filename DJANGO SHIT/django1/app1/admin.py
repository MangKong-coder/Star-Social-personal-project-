from django.contrib import admin
from app1.models import User, Webpage, AccessRecord
# Register your models here.

admin.site.register(User)
admin.site.register(Webpage)
admin.site.register(AccessRecord)