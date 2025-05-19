from django.contrib import admin

from myapp.models import CarouselSlide, NewsEvents, GalleryImage, Testimonial, Faculty


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

admin.site.register(CarouselSlide, CarouselSlideAdmin)
admin.site.register(NewsEvents, NewsEventsAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(GalleryImage, GalleryImageAdmin)
admin.site.register(Testimonial, TestimonialAdmin)