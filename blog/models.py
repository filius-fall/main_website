from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_post = models.DateTimeField(default=timezone.now())
    categories = models.TextField(null=True,blank=True)
    tags = models.TextField(null=True,blank=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    banner_image = models.ImageField(upload_to='images/',null=True)
    featured = models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk':self.pk})
        


