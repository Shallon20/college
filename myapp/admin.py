from django.contrib import admin

from myapp.models import CarouselSlide, NewsEvents, GalleryImage, Testimonial, Faculty, AboutInfo, StaffMember, \
    VisionMission, Stats, WhyChooseUs, Course, DeanProfile, DeanStaff


# Register your models here.
class CarouselSlideAdmin(admin.ModelAdmin):
    list_display = ('title', 'image',)
class NewsEventsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    prepopulated_fields = {'slug': ('title',)}
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('caption', 'image',)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'graduation_year', 'rating',)
class AboutInfoAdmin(admin.ModelAdmin):
    list_display = ('content',)
class WhyChooseUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
class StatsAdmin(admin.ModelAdmin):
    list_display = ('label', 'value',)
class VisionMissionAdmin(admin.ModelAdmin):
    list_display = ('type', 'content',)
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role',)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('faculty', 'title', 'description',)
class DeanProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'email', 'phone', 'office_address',)
class DeanStaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')

admin.site.register(CarouselSlide, CarouselSlideAdmin)
admin.site.register(NewsEvents, NewsEventsAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(AboutInfo, AboutInfoAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(VisionMission, VisionMissionAdmin)
admin.site.register(StaffMember, StaffMemberAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DeanProfile, DeanProfileAdmin)
admin.site.register(DeanStaff, DeanStaffAdmin)