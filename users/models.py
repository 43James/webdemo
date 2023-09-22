from django.db import models
from django.contrib.auth.models import User, AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField()
    class Meta:
        ordering = ['-id']

class Profile(models.Model):
    gender = models.CharField(max_length=20, default='', verbose_name='เพศ')
    work_group = models.CharField(max_length=150, verbose_name='กลุ่มงาน')
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)