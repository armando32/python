from django.db import models
from django.utils import timezone
# Create your models here.


class Account(models.Model):
	account = models.CharField(verbose_name='Account',max_length=50)
	app_code = models.CharField(verbose_name='App code',max_length=20)
	id_token = models.CharField(verbose_name='Identity token',max_length=50)
	fran_net = models.CharField(verbose_name='Franchise network',max_length=10)
	fran_type = models.CharField(verbose_name='Franchise type',max_length=10)
	date_join = models.DateTimeField(verbose_name='Date joined',default=timezone.now)

class Session(models.Model):
    Account_session = models.CharField(verbose_name='Account session', max_length=50)
    User = models.CharField(verbose_name='User',max_length=50)
    Session_expiry = models.DateTimeField(verbose_name='Session expiry', default=timezone.now()+timezone.timedelta(days=60))
    Last_logged_in = models.DateTimeField(verbose_name='Last logged in', blank=True, null=True)
    Date_created = models.DateTimeField(verbose_name='Date created', default=timezone.now)

    def Log(self):
    	self.Last_logged_in=timezone.now

class Message(models.Model):
    app_code = models.CharField(verbose_name='App code', max_length=50)
    app_sms = models.CharField(verbose_name='App sms message', max_length=20)
    message = models.CharField(verbose_name='Message', max_length=200)
    shortcode = models.IntegerField(verbose_name='Shortcode')
    xdn_type = models.CharField(verbose_name='Xdn usage type', max_length=50)
    date_modified = models.DateTimeField(verbose_name='Date modified', blank=True, null=True)
    date_created = models.DateTimeField(verbose_name='Date created', default=timezone.now)

    def DateModify(self):
    	self.date_modified = timezone.now
    	self.save()

class Verification(models.Model):
	ver_token = models.CharField(verbose_name='Verification token', max_length=50)
	ver = models.CharField(verbose_name='Verification', max_length=10)
	valid = models.DateTimeField(verbose_name='Valid until', default=timezone.now()+timezone.timedelta(minutes=10))
	payload = models.CharField(verbose_name='Payload', max_length=200)
	last_mod = models.DateTimeField(verbose_name='Last Modified', default=timezone.now)