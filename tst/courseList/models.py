from django.db import models

# Create your models here.
class course_list(models.Model):
    course_id = models.CharField(max_length=128,primary_key=True)
    course_name = models.CharField(max_length=128)
    t_name = models.CharField(max_length=128)

    