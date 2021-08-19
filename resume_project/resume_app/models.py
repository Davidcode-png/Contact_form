from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=250)
    title = models.CharField(max_length=200,default='')
    message = models.TextField(default='')

    def __str__(self):
        return self.name
