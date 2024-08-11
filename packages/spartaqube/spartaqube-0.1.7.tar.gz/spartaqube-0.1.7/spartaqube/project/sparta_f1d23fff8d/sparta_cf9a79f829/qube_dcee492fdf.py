_A='jsonData'
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as conf_settings
from project.models import UserProfile
from project.sparta_c7fea0e6b9.sparta_71bb75ea08 import qube_0400a0ab9b as qube_0400a0ab9b
from project.sparta_c7fea0e6b9.sparta_aa98815bd5 import qube_3dd70b4e7a as qube_3dd70b4e7a
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_fb40525a5b
@csrf_exempt
@sparta_fb40525a5b
def sparta_c44903c589(request):
	B=request;I=json.loads(B.body);C=json.loads(I[_A]);A=B.user;D=0;E=UserProfile.objects.filter(user=A)
	if E.count()>0:
		F=E[0]
		if F.has_open_tickets:
			C['userId']=F.user_profile_id;G=qube_3dd70b4e7a.sparta_f9020428e8(A)
			if G['res']==1:D=int(G['nbNotifications'])
	H=qube_0400a0ab9b.sparta_c44903c589(C,A);H['nbNotificationsHelpCenter']=D;J=json.dumps(H);return HttpResponse(J)
@csrf_exempt
@sparta_fb40525a5b
def sparta_822b40b891(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_0400a0ab9b.sparta_99993b96ea(C,A.user);E=json.dumps(D);return HttpResponse(E)