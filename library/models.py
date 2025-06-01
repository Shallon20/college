from django.db import models

# Create your models here.
class LibraryIntro(models.Model):
    short_intro = models.CharField(max_length=255)
    image = models.ImageField(upload_to="library/", null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "library_intro"
        verbose_name_plural = "Library Intro"

class LibraryServices(models.Model):
    icon = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "library_services"
        verbose_name_plural = "Library Services"

class LibraryStaff(models.Model):
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to="library/", null=True, blank=True)

    def __str__(self):
        return self.full_name
    class Meta:
        db_table = "library_staff"
        verbose_name_plural = "Library Staff"

class LibraryContacts(models.Model):
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    open_hours = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.phone
    class Meta:
        db_table = "library_contacts"
        verbose_name_plural = "Library Contacts"
