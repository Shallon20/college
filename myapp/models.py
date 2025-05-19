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