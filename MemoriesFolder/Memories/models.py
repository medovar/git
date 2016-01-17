from django.db import models
from django.contrib.auth.models import User


class Mem(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=150,null=True)
    text = models.TextField()
    pub_date = models.DateTimeField(null=True)
    like_count = models.IntegerField(default=0)

class Comments(models.Model):
    user = models.ForeignKey(User)
    mem = models.ForeignKey(Mem)
    comment = models.TextField()

class Like(models.Model):
    user = models.ForeignKey(User)
    mem = models.ForeignKey(Mem)
    user_st = models.BooleanField(default=True)

