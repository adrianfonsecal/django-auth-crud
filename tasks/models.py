from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    completedDate = models.DateTimeField(null=True, blank=True)
    isImportant = models.BooleanField(default=False)
    createdByUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title + ' - by ' + self.createdByUser.username


