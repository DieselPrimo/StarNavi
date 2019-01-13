from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255, blank=False, null=True)
    login = models.CharField(max_length=255, unique=True, blank=False, null=True)
    password = models.CharField(max_length=255, blank=False, null=True)
    email = models.EmailField(max_length=70, blank=False, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=255)
    like = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
