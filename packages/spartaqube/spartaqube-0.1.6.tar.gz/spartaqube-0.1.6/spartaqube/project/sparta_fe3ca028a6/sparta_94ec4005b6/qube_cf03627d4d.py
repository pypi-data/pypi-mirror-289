from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_d6cbf19e98
from project.sparta_c7fea0e6b9.sparta_aa98815bd5 import qube_3dd70b4e7a as qube_3dd70b4e7a
from project.models import UserProfile
import project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 as qube_78b017fa56
@sparta_d6cbf19e98
@login_required(redirect_field_name='login')
def sparta_23488d9d71(request):
	E='avatarImg';B=request;A=qube_78b017fa56.sparta_97cb8e2f6f(B);A['menuBar']=-1;F=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(F);A[E]='';C=UserProfile.objects.filter(user=B.user)
	if C.count()>0:
		D=C[0];G=D.avatar
		if G is not None:H=D.avatar.image64;A[E]=H
	A['bInvertIcon']=0;return render(B,'dist/project/helpCenter/helpCenter.html',A)
@sparta_d6cbf19e98
@login_required(redirect_field_name='login')
def sparta_bc55c8734c(request):
	A=request;B=UserProfile.objects.filter(user=A.user)
	if B.count()>0:C=B[0];C.has_open_tickets=False;C.save()
	return sparta_23488d9d71(A)