from django.db import models
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class CarouselSlide(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="carousel/")
    link = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.title

class NewsEvents(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="news/")
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Faculty(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "faculty"
        verbose_name_plural = "Faculties"

class GalleryImage(models.Model):
    caption = models.TextField()
    image = models.ImageField(upload_to="gallery/")

    def __str__(self):
        return self.caption


class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=150)
    graduation_year = models.CharField(max_length=10)
    image = models.ImageField(upload_to='testimonials/')
    quote = models.TextField()
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name

class AboutInfo(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    color_class = models.CharField(max_length=50, default='text-primary')

    def __str__(self):
        return self.title

class Stats(models.Model):
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=20)
    color = models.CharField(max_length=50, default='text-primary')

    def __str__(self):
        return f"{self.label}: {self.value}"

class VisionMission(models.Model):
    type = models.CharField(max_length=50, choices=[
        ('Vision', 'Vision'),
        ('Mission', 'Mission'),
        ('Core Values', 'Core Values'),
        ('Philosophy', 'Philosophy')
    ])
    content = models.TextField()

    def __str__(self):
        return self.type

class StaffMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/')

    def __str__(self):
        return self.name

class Course(models.Model):
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, related_name='courses')
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/')
    fee_structure = models.FileField(upload_to='fee_structures/', blank=True)

    def __str__(self):
        return self.title

class DeanProfile(models.Model):
    short_description =models.TextField(max_length=100, default='')
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dean/')
    title = models.CharField(max_length=100, default="Dean of Students")
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    office_address = models.TextField()
    message_from_dean = models.TextField()

    def __str__(self):
        return self.name

class DeanStaff(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dean/staff/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name