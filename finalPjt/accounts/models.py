from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    nickname = models.CharField(max_length=40, blank=True)
    image = ProcessedImageField(
        null = True,
        processors = [Thumbnail(200,200)],
        format ="JPEG",
        options = {'qality': 60}
        )
    
class User(AbstractUser):
    # 더 이상 contrib.models.Model의 유저가 아니라 accounts app 에 있는 유저
    followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="followings")
    is_staff = models.BooleanField(default=False)
