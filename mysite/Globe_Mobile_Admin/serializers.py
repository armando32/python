from rest_framework import serializers
from .models import Account, Session, Message, Verification

class AccountSerializer(serializers.ModelSerializer):

	class Meta:
		model = Account
		fields = ('account', 'app_code', 'id_token', 'fran_net', 'fran_type', 'date_join')

class SessionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Session
		fields = ('Account_session', 'User', 'Session_expiry', 'Last_logged_in', 'Date_created')

class MessageSerializer(serializers.ModelSerializer):

	class Meta:
		model = Message
		fields = ('app_code', 'app_sms', 'message', 'shortcode', 'xdn_type', 'date_modified', 'date_created')


class VerificationSerializer(serializers.ModelSerializer):

	class Meta:
		model = Verification
		fields = ('ver_token', 'ver', 'valid', 'payload', 'last_mod')

