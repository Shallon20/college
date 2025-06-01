from django.contrib import admin

from library.models import LibraryIntro, LibraryServices, LibraryStaff, LibraryContacts

# Register your models here.
class LibraryIntroAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_intro',)
class LibraryServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
class LibraryContactsAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email',)
class LibraryStaffAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role',)

admin.site.register(LibraryIntro, LibraryIntroAdmin)
admin.site.register(LibraryServices, LibraryServicesAdmin)
admin.site.register(LibraryStaff, LibraryStaffAdmin)
admin.site.register(LibraryContacts, LibraryContactsAdmin)