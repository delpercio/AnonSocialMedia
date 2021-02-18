from django.db import models
from django.utils import timezone
# Create your models here.

POST_CHOICES = ((True, 'Boast'), (False, 'Roast'))

class Posts(models.Model):
    text = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    post_type = models.BooleanField(choices=POST_CHOICES, default= True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.likes - self. dislikes)
