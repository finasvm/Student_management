from django.contrib import admin
from .models import Contact,Course,Staff

# Register your models here.


admin.site.register(Staff)
class Coursedetails(admin.ModelAdmin):
    list_display=('name','description','duration','fee','course_image')
admin.site.register(Course,Coursedetails)
class Customerdetails(admin.ModelAdmin):
    list_display=('name','phno','email')
admin.site.register(Contact,Customerdetails)