_G='message'
_F='errorMsg'
_E='date_created'
_D='ticket_id'
_C=True
_B=False
_A='res'
import json,base64,requests,hashlib
from datetime import datetime,timedelta
from dateutil import parser
import pytz
UTC=pytz.utc
from django.conf import settings as conf_settings
from django.contrib.auth.models import User
from django.contrib.humanize.templatetags.humanize import naturalday
from django.forms.models import model_to_dict
from project.models import UserProfile,ticket,ticketMessage
from project.sparta_c7fea0e6b9.sparta_957b17c2d6 import qube_4f323a8bf2 as qube_4f323a8bf2
from project.sparta_c7fea0e6b9.sparta_1feb719204 import qube_84bec09a68 as qube_84bec09a68
from project.sparta_c7fea0e6b9.sparta_fe626c7ed8 import qube_ad878641d5 as qube_ad878641d5
from project.sparta_c7fea0e6b9.sparta_6eb76fb447.qube_863ab3ebef import Email as Email
from project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 import sparta_487e63ac34
ADMIN_EMAIL=conf_settings.ADMIN_EMAIL_TICKET
MAX_TICKETS=conf_settings.MAX_TICKETS
def sparta_0d2a76f082(json_data,user_obj):
	L='typeCase';K='captcha';B=json_data;A=user_obj;M=B[K];F=B['titleCase'];G=B['messageCase'];H=B[L];N=datetime.now()-timedelta(1);C=datetime.now().astimezone(UTC);D=str(str(A.email)+str(C)).encode('utf-8');D=hashlib.md5(D).hexdigest();O=ticket.objects.filter(date_created__gte=N,user=A);I=len(O)
	if I<=MAX_TICKETS:
		E={K:M,'title':F,_G:G,L:H,_D:D,'email':A.email,'first_name':A.first_name,'last_name':A.last_name};E['jsonData']=json.dumps(E);P=requests.post(f"{conf_settings.SPARTAQUBE_WEBSITE}/help-center-new-case",data=json.dumps(E))
		if P.status_code==200:
			try:C=datetime.now().astimezone(UTC);Q=ticket.objects.create(ticket_id=D,type_ticket=H,title=F,date_created=C,user=A);ticketMessage.objects.create(ticket=Q,message=G,user=A,date_created=C);J=UserProfile.objects.get(user=A);J.has_open_tickets=_C;J.save()
			except Exception as R:return{_A:-1,_F:str(R)}
		return{_A:1,'nbTickets':I}
	else:return{_A:-1,_F:'You have reached the maximum tickets limit'}
def sparta_a88952f13b(message,typeCase=0,companyName=None):
	F='Type';C=companyName;B=typeCase;D='BUG'
	if int(B)==0:D='GENERAL'
	E=User.objects.filter(is_staff=_C)
	if E.count()>0:
		G=E[0];A=Email(G.username,[conf_settings.CONTACT_US_EMAIL],'New case opened','New case of type > '+str(D))
		if C is not None:A.addOneRow('Company',C);A.addLineSeparator()
		A.addOneRow('Message',message);A.addLineSeparator()
		if int(B)==0:A.addOneRow(F,'General question')
		else:A.addOneRow(F,'Report Bug')
		A.send()
def sparta_103a991a8b(json_data,user_obj):
	H='arrRes';G='user';E=user_obj;F=json_data['has_user_closed']
	if E.is_staff:
		B=ticket.objects.filter(is_delete=0,has_user_closed=F).order_by('status_ticket');C=[]
		if B.count()>0:
			for D in B:A=sparta_487e63ac34(model_to_dict(D));del A[G];A[_E]=naturalday(parser.parse(str(A[_E])));C.append(A)
		return{_A:1,H:C}
	else:
		B=ticket.objects.filter(user=E,is_delete=0,has_user_closed=F).order_by('-date_created');C=[]
		if B.count()>0:
			for D in B:A=sparta_487e63ac34(model_to_dict(D));del A[G];C.append(A)
		return{_A:1,H:C}
def sparta_1fa23a76dd(json_data,user_obj):
	D=user_obj;I=json_data[_D]
	if D.is_staff:F=ticket.objects.filter(ticket_id=I,is_delete=0)
	else:F=ticket.objects.filter(user=D,ticket_id=I,is_delete=0)
	E=[]
	if F.count()>0:
		G=F[0]
		if not D.is_staff:G.b_show_user_notification=_B;G.save()
		B=ticketMessage.objects.filter(ticket=G)
		if B.count()>0:
			J=B[0].user;C=[]
			for(K,L)in enumerate(B):
				H=L.user;A=sparta_487e63ac34(model_to_dict(L));A[_E]=naturalday(parser.parse(str(A[_E])))
				if D==H:A['me']=1
				else:A['me']=0
				if H==J:
					C.append(A)
					if K==len(B)-1:E.append(C)
				else:
					E.append(C);C=[A]
					if K==len(B)-1:E.append(C)
				J=H
	return{_A:1,'arrMsg':E}
def sparta_4ee1f41180(json_data,user_obj):
	D=json_data;B=user_obj;E=D[_D];F=D[_G]
	if B.is_staff:C=ticket.objects.filter(ticket_id=E)
	else:C=ticket.objects.filter(user=B,ticket_id=E)
	if C.count()>0:
		A=C[0];H=datetime.now().astimezone(UTC);ticketMessage.objects.create(ticket=A,message=F,user=B,date_created=H)
		if A.b_send_email and not B.is_staff:A.b_send_email=_B;A.save();sparta_a88952f13b(F,A.type_ticket,None)
		if B.is_staff:A.status_ticket=2;A.b_send_email=_C;A.has_user_closed=_B;A.b_show_user_notification=_C;A.save();G=UserProfile.objects.get(user=A.user);G.has_open_tickets=_C;G.save()
		else:A.status_ticket=1;A.has_user_closed=_B;A.b_send_email=_B;A.b_show_user_notification=_B;A.save()
		return{_A:1}
	return{_A:-1,_F:'An unexpected error occurred'}
def sparta_e927889dd8(json_data,user_obj):
	B=user_obj;C=json_data[_D]
	if B.is_staff:A=ticket.objects.filter(ticket_id=C)
	else:A=ticket.objects.filter(user=B,ticket_id=C)
	if A.count()>0:D=A[0];D.has_user_closed=_C;D.save()
	return{_A:1}
def sparta_277831e0ac(json_data):
	A=json_data;D=A['userId'];E=A[_D];B=ticket.objects.filter(user_id=D,ticket_id=E)
	if B.count()>0:C=B[0];C.b_show_user_notification=_B;C.save()
	return{_A:1}
def sparta_f9020428e8(user_obj):A=ticket.objects.filter(user=user_obj,b_show_user_notification=_C,has_user_closed=_B);return{_A:1,'nbNotifications':A.count()}