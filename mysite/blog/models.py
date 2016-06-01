from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Session_Table(models.Model):
    Account_session = models.CharField(max_length=50)
    User = models.CharField(max_length=100)
    Session_expiry = models.DateTimeField()
    Last_logged_in = models.DateTimeField()
    Date_created = models.DateTimeField()

    def __str__(self):
        return self.User
