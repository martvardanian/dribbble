from django.db import models


class Cards(models.Model):
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"

    image = models.ImageField(upload_to='images/blog/%Y/%m/%d')
    name = models.CharField(max_length=20)
    like = models.IntegerField()
    view = models.IntegerField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
