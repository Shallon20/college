from django.contrib import admin

from alumni.models import Alumni, AlumniBoard, WhyStayConnected, AlumniMessage


# Register your models here.
class AlumniAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'title', 'content',)
class AlumniBoardAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role',)
class WhyStayConnectedAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
class AlumniMessageAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'graduation_year', 'email', 'course_studied',)



admin.site.register(Alumni, AlumniAdmin)
admin.site.register(AlumniBoard, AlumniBoardAdmin)
admin.site.register(WhyStayConnected, WhyStayConnectedAdmin)
admin.site.register(AlumniMessage, AlumniMessageAdmin)