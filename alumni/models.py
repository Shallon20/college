from django.db import models

# Create your models here.
class Alumni(models.Model):
    short_description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='alumni', null=True, blank=True)
    title = models.CharField(max_length=30)
    content = models.TextField(blank=True)

    def __str__(self):
        return self.short_description

class AlumniBoard(models.Model):
    image = models.ImageField(upload_to='alumni', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class WhyStayConnected(models.Model):
    icon = models.CharField(max_length=50, null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title

class AlumniMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    graduation_year = models.CharField(max_length=10)
    course_studied = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} ({self.graduation_year})"