from pyexpat import model
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(
        upload_to='images/', 
        blank=True, 
        processors=[ResizeToFill(200,200)], 
        format='JPEG',
        options={'quality':80}
        )
