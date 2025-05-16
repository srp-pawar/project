from django.db import models

# Create your models here.
class Testimonials(models.Model):
    Name=models.CharField(max_length=20)
    Rating_stars=models.PositiveSmallIntegerField()
    Rating_views=models.TextField()
    User_post=models.CharField(max_length=20)

class Messages_users(models.Model):
    Username=models.CharField(max_length=25)
    Email_id=models.EmailField()
    message_by_user=models.TextField()
    date_time=models.TimeField(auto_now=True)
