from django.db import models


class Cards(models.Model):
    image = models.ImageField(upload_to='images/blog/%Y/%m/%d')
    name = models.CharField(max_length=20)
    like = models.IntegerField()
    view = models.IntegerField()
    is_published = models.BooleanField(default=False)
