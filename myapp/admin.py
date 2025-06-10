from django.contrib import admin

from myapp.models import CarouselSlide, NewsEvents, GalleryImage, Testimonial, Faculty, AboutInfo, StaffMember, \
    VisionMission, Stats, WhyChooseUs, Course, DeanProfile, DeanStaff, StudentLeadership, JobsInternshipsAds, Sport, \
    Club, SportImage, ClubImage, HostelApplication, Hostel, HostelImage, DispensaryService, DispensaryContact, \
    DispensaryGallery, CafeteriaService, CafeteriaMenu, CafeteriaImage, CafeteriaMenuPDF, Enrollment, ContactUs, \
    ContactInfo, FAQ, Logo, SocialLinks


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
class StudentLeadershipAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', )
class JobsInternshipsAdsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
class SportImageAdmin(admin.ModelAdmin):
    list_display = ('sport',)
class SportImageInline(admin.TabularInline):
    model = SportImage
    extra = 1
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [SportImageInline]
class ClubImageInline(admin.TabularInline):
    model = ClubImage
    extra = 1
class ClubAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    inlines = [ClubImageInline]
class ClubImageAdmin(admin.ModelAdmin):
    list_display = ('club',)
class HostelImageInline(admin.TabularInline):
    model = HostelImage
    extra = 1
class HostelAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    inlines = [HostelImageInline]
class HostelApplicationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'student_id', 'preferred_type', )
class HostelImageAdmin(admin.ModelAdmin):
    list_display = ('hostel',)
class DispensaryServiceAdmin(admin.ModelAdmin):
    list_display = ('short_description',)
class DispensaryContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'location', 'is_active',)
class DispensaryGalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'caption']
class CafeteriaServiceAdmin(admin.ModelAdmin):
    list_display = ('short_description', 'services',)
class CafeteriaMenuAdmin(admin.ModelAdmin):
    list_display = ('day', 'meal',)
class CafeteriaImageAdmin(admin.ModelAdmin):
    list_display = ('caption',)
class CafeteriaMenuPDFAdmin(admin.ModelAdmin):
    list_display = ('uploaded_at',)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'course')
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject',)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('contact_detail', 'icon',)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer',)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('site_name',)
class SocialLinksAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(CarouselSlide, CarouselSlideAdmin)
admin.site.register(NewsEvents, NewsEventsAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Testimonial, TestimonialAdmin)
admin.site.register(AboutInfo, AboutInfoAdmin)
admin.site.register(WhyChooseUs, WhyChooseUsAdmin)
admin.site.register (Stats, StatsAdmin)
admin.site.register(VisionMission, VisionMissionAdmin)
admin.site.register(StaffMember, StaffMemberAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(DeanProfile, DeanProfileAdmin)
admin.site.register(DeanStaff, DeanStaffAdmin)
admin.site.register(StudentLeadership, StudentLeadershipAdmin)
admin.site.register(Sport, SportAdmin)
admin.site.register(Club, ClubAdmin)
admin.site.register(JobsInternshipsAds, JobsInternshipsAdsAdmin)
admin.site.register(SportImage, SportImageAdmin)
admin.site.register(ClubImage, ClubImageAdmin)
admin.site.register(Hostel, HostelAdmin)
admin.site.register(HostelApplication, HostelApplicationAdmin)
admin.site.register(HostelImage, HostelImageAdmin)
admin.site.register(DispensaryService, DispensaryServiceAdmin)
admin.site.register(DispensaryContact, DispensaryContactAdmin)
admin.site.register(DispensaryGallery, DispensaryGalleryAdmin)
admin.site.register(CafeteriaService, CafeteriaServiceAdmin)
admin.site.register(CafeteriaImage, CafeteriaImageAdmin)
admin.site.register(CafeteriaMenu, CafeteriaMenuAdmin)
admin.site.register(CafeteriaMenuPDF, CafeteriaMenuPDFAdmin)
admin.site.register(Enrollment, EnrollmentAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Logo, LogoAdmin)
admin.site.register(SocialLinks, SocialLinksAdmin)