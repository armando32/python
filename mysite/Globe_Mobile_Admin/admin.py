from django.contrib import admin
from .models import Account,Message,Session,Verification

# Register your models here.
class a(admin.ModelAdmin):
	list_display = ('account','app_code','id_token','fran_net','fran_type','date_join')

admin.site.register(Account,a)


class SessionTable(admin.ModelAdmin):
	list_display=('Account_session', 'User', 'Session_expiry', 'Last_logged_in', 'Date_created')

admin.site.register(Session, SessionTable)


class Msg(admin.ModelAdmin):
	list_display=('app_code', 'app_sms', 'message', 'shortcode', 'xdn_type', 'date_modified', 'date_created')

admin.site.register(Message, Msg)


class Verf(admin.ModelAdmin):
	list_display=('ver_token', 'ver', 'valid', 'payload', 'last_mod')

admin.site.register(Verification, Verf)
