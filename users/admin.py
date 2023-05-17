from django.contrib import admin

# Register your models here.
from users.models import (Students,Orders)
admin.site.register(Students)
admin.site.register(Orders)