from django.utils import timezone
from .models import Account, Session, Message, Verification

from rest_framework import status
from rest_framework.decorators import api_view
from django.template import RequestContext
from rest_framework.response import Response
from Globe_Mobile_Admin.serializers import AccountSerializer, SessionSerializer, MessageSerializer, VerificationSerializer 
# Create your views here.


@api_view(['GET', 'POST'])
def AccountList(request):

        if request.method=='GET':
                acc = Account.objects.all()
                serializer1 = AccountSerializer(acc, many=True)
                return Response(serializer1.data)
        
        elif request.method=='POST':
                serializer1 = AccountSerializer(data=request.data)
                if serializer1.is_valid():
                        serializer1.save()
                        return Response(serializer1.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer1.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def SessionList(request):

        if request.method=='GET':
                sess = Session.objects.all()
                serializer2 = SessionSerializer(sess, many=True)
                return Response(serializer2.data)
        
        elif request.method=='POST':
                serializer2 = SessionSerializer(data=request.data)
                if serializer2.is_valid():
                        serializer2.save()
                        return Response(serializer2.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer2.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def MessageList(request):

        if request.method=='GET':
                msg = Message.objects.all()
                serializer3 = MessageSerializer(msg, many=True)
                return Response(serializer3.data)
        
        elif request.method=='POST':
                serializer3 = MessageSerializer(data=request.data)
                if serializer3.is_valid():
                        serializer3.save()
                        return Response(serializer3.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer3.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def VerificationList(request):

        if request.method=='GET':
                ver = Verification.objects.all()
                serializer4 = VerificationSerializer(ver, many=True)
                return Response(serializer4.data)
        
        elif request.method=='POST':
                serializer4 = VerificationSerializer(data=request.data)
                if serializer4.is_valid():
                        serializer4.save()
                        return Response(serializer4.data, status=status.HTTP_201_CREATED)
                else:
                        return Response(serializer4.errors, status=status.HTTP_400_BAD_REQUEST)