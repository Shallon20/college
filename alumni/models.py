from django.db import models

# Create your models here.
class Alumni(models.Model):
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='alumni', null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.short_description
    class Meta:
        db_table = "alumni"
        verbose_name_plural = "Alumni"

class AlumniBoard(models.Model):
    image = models.ImageField(upload_to='alumni', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name
    class Meta:
        db_table = "alumni_board"
        verbose_name_plural = "Alumni Board"

class WhyStayConnected(models.Model):
    icon = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "why_stay_connected"
        verbose_name_plural = "Why Stay Connected"

class AlumniMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    graduation_year = models.CharField(max_length=10)
    course_studied = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.graduation_year})"
    class Meta:
        db_table = "alumni_message"
        verbose_name_plural = "Alumni Message"

class AlumniContacts(models.Model):
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.address

    class Meta:
        db_table = "alumni_contacts"
        verbose_name_plural = "Alumni Contacts"