from django.db import models
import datetime
import os
from django.contrib.auth.models import User    # Get User from Django User Management

# Create your models here.
# Define Path (create folder) for File Uploads based on Upload Date
def get_image_path(date, filename):
    return os.path.join('uploads', str(datetime.date.today()), filename)

# Article Model
class Article(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)    # From Django User Management
    image = models.ImageField(default='default.png', blank=True, upload_to=get_image_path)
    # Auto Date and Time when creating an Employee
    last_updated = models.DateTimeField(auto_now=True)
    # Active/Inactive Choice for Featured Article
    ACTIVE_INACTIVE_CHOICES = [
    (True, 'Active'),
    (False, 'Inactive'),
    ]
    featured = models.BooleanField(
        choices=ACTIVE_INACTIVE_CHOICES,
        default=True,
    )
    # Return Artitle Title and Autor
    def __str__(self):
        return str(self.title) + ' - ' + str(self.author)
    # Return Article Body Preview
    def snippet(self):
        return self.body[:50] + '...'    # First 50 chars plus 3 dots at the end
