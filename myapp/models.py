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
    is_new = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'News & Events'

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
    class Meta:
        verbose_name_plural = 'About Info'
    

class WhyChooseUs(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_class = models.CharField(max_length=50)
    color_class = models.CharField(max_length=50, default='text-primary')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Why Choose Us'

class Stats(models.Model):
    label = models.CharField(max_length=50)
    value = models.CharField(max_length=20)
    color = models.CharField(max_length=50, default='text-primary')

    def __str__(self):
        return f"{self.label}: {self.value}"
    class Meta:
        verbose_name_plural = 'Stats'

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
    class Meta:
        verbose_name_plural = 'Vision & Mission'

class StaffLeadership(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='staff/')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Staff Leadership'

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
    class Meta:
        verbose_name_plural = 'Dean Profile'

class DeanStaff(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='dean/staff/')
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class StudentLeadership(models.Model):
    image = models.ImageField(upload_to='student_leadership/')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Student Leadership'

class JobsInternshipsAds(models.Model):
    title = models.CharField(max_length=100)
    deadline = models.DateField(blank=False)
    description = models.TextField(max_length=300)
    link = models.URLField(blank=False)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Jobs & Internship Ads'

class Sport(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    captain_name = models.CharField(max_length=100, blank=True)
    captain_contact = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class SportImage(models.Model):
    sport = models.ForeignKey(Sport, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='sports/')

    def __str__(self):
        return f"Image for {self.sport.name}"

class Club(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    leader_name = models.CharField(max_length=100)
    leader_contact = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

class ClubImage(models.Model):
    club = models.ForeignKey(Club, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='club_images/')

    def __str__(self):
        return f"Image for {self.club.name} "
class Hostel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    features = models.TextField(help_text="Enter each feature separated by a semicolon (;)")
    price = models.DecimalField(max_digits=8, decimal_places=2, help_text="Monthly price in KES")

    def __str__(self):
        return self.name

class HostelImage(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hostel_images/')

    def __str__(self):
        return f"Image for {self.hostel.name}"

class HostelApplication(models.Model):
    full_name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    preferred_type = models.CharField(max_length=50)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.student_id}"

class DispensaryService(models.Model):
    short_description = models.CharField(max_length=300)
    service_list = models.CharField(blank=True, max_length=500)
    image = models.ImageField(upload_to='dispensary_service/')
    def __str__(self):
        return self.short_description

class DispensaryContact(models.Model):
    is_active = models.BooleanField(default=True)
    contact_note = models.TextField(help_text="Short note e.g., 'We’re Open 24/7'")
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Contact Info ({self.phone})"

class DispensaryGallery(models.Model):
    image = models.ImageField(upload_to='dispensary_service/')
    caption = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.caption or f"Dispensary Image {self.id}"
    class Meta:
        verbose_name_plural = 'Dispensary Gallery'

class CafeteriaService(models.Model):
    short_description = models.TextField(max_length=500, blank=True)
    services  = models.TextField(help_text="Separate features with a semicolon (;)")

    def __str__(self):
        return self.short_description

class CafeteriaImage(models.Model):
    image = models.ImageField(upload_to='cafeteria/')
    caption = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.caption or "Cafeteria Image"

class CafeteriaMenu(models.Model):
    day = models.CharField(max_length=20)
    meal = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.day} - {self.meal}"

class CafeteriaMenuPDF(models.Model):
    file = models.FileField(upload_to='cafeteria_menus/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Menu PDF uploaded on {self.uploaded_at.date()}"

class Enrollment(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=100)
    reason = models.TextField(blank=True)

    def __str__(self):
        return f"{self.full_name} - {self.course}"
class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=100)
    message = models.TextField(blank=False)

    def __str__(self):
        return self.email
    class Meta:
        verbose_name_plural = 'Contact Us'

class ContactInfo(models.Model):
    contact_detail = models.CharField(max_length=100)
    icon = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.contact_detail
    class Meta:
        verbose_name_plural = 'Contact Info'

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True)

    def __str__(self):
       return self.question
    
class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
    site_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.site_name
    
    class Meta:
        db_table = 'logo'
        verbose_name_plural = 'Logo'

class SocialLinks(models.Model):
    name = models.CharField(max_length=50)
    icon_class = models.CharField(max_length=100)
    url = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        db_table = 'social_links'
        verbose_name_plural = 'Social Links'
