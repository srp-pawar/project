from django.db import models
from django.contrib.auth.models import User,auth


# Create your models here.
my_choices=(
    ('Easy','Easy'),
    ('Intemediate','Intermediate'),
    ('Hard','Hard')
)
class Forensics_challenges(models.Model):
    Challenge_ID=models.CharField(max_length=8 ,primary_key=True) 
    Challenge_Name=models.CharField(max_length=50)
    Challenge_Discription=models.TextField()
    Challenge_Points=models.IntegerField()
    Challenge_Difficulty=models.CharField(max_length=13,choices=my_choices)
    Challenge_Answer=models.TextField()
    Challenge_File=models.FileField(null=True)
    Challenge_Ratings=models.IntegerField(default=2.5)
    


class Forensics_challenges_solved(models.Model):
    Username=models.CharField(max_length=25)
    Challenge_id=models.CharField(max_length=5)


