from django.db import models
from django.utils import timezone


class verification(models.Model):
    ver_tok = models.CharField(verbose_name='Verification Token',max_length=200)
    ver = models.IntegerField(verbose_name='Verification')
    val_until = models.DateTimeField(verbose_name='Valid Until',default=timezone.now)
    pay = models.CharField(verbose_name='Payload',max_length=200)
    last_mod = models.DateTimeField(verbose_name='Last Modified',default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
