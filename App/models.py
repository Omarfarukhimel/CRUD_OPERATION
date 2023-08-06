from django.db import models


# Create your models here.
class Profile(models.Model):
    Religion = (
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Christian', 'Christian'),
        ('Buddha', 'Buddha')
    )
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others')
    )

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile_pic/', default='default_pic/def.png', null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    age = models.PositiveIntegerField()
    date_of_birth = models.DateField()
    phone_number = models.TextField(max_length=20)
    address = models.TextField(max_length=200, null=True, blank=True)
    gender = models.CharField(max_length=9, choices=Gender)
    religion = models.CharField(max_length=9, choices=Religion)

    def __str__(self):
        return str(self.name)
