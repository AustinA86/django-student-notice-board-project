from django.db import models
from django.contrib.auth.models import User

# MODULE 2: Simple Model
class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name='liked_notices', blank=True)

    def total_likes(self):
        return self.liked_by.count()

    def __str__(self):
        return self.title
