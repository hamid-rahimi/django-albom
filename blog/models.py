from django.contrib.auth.models import User
from django.db import models
from django_jalali.db import models as jmaodels


class Article(models.Model):

    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = jmaodels.jDateTimeField(auto_now_add=True)
    is_show = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog/article/')

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(help_text="کمک")
    email = models.EmailField(help_text="ایمیل")

    def __str__(self):
        res = self.first_name + " " + self.last_name
        return res
