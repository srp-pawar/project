from django.contrib import admin

# Register your models here.
from .models import Forensics_challenges,Forensics_challenges_solved
# Register your models here.
admin.site.register(Forensics_challenges)
admin.site.register(Forensics_challenges_solved)