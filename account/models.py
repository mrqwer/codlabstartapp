from django.db import models
# from django.utils import timezone
from django.conf import settings
from .utils import get_random_code
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth=models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    # bio = models.TextField(max_length = 300)
    # country = models.CharField(max_length=100)
    # slug = models.SlugFiled()
    # post = models.Char

    def __str__(self):
        return f'Profile for user {self.user.username}'
