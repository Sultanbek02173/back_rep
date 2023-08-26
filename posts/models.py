from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ("created",)