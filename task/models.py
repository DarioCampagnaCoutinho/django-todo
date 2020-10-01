from django.db import models
from django.contrib.auth import get_user_model


class Task(models.Model):
    STATUS = (
        ('doing', 'Doing'),
        ('done', 'Done'),
    )
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=265)
    description = models.TextField()
    done = models.CharField(max_length=9, choices=STATUS,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

