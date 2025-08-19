from django.contrib import admin
from .models import Students, Enrollment, Subject, Instructor

# Register your models here.

class EnrollmentAdmin(admin.ModelAdmin):
  list_display = ("subject", "student", "mark")

admin.site.register(Students)
admin.site.register(Instructor)
admin.site.register(Subject)
admin.site.register(Enrollment, EnrollmentAdmin)