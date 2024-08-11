_C='isAuth'
_B='jsonData'
_A='res'
import json
from django.contrib.auth import logout
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from project.sparta_c7fea0e6b9.sparta_7639bac7be import qube_48eea7078d as qube_48eea7078d
from project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 import sparta_2c0db3492a
@csrf_exempt
def sparta_abcb534bb0(request):A=json.loads(request.body);B=json.loads(A[_B]);return qube_48eea7078d.sparta_abcb534bb0(B)
@csrf_exempt
def sparta_3a26a2b07a(request):logout(request);A={_A:1};B=json.dumps(A);return HttpResponse(B)
@csrf_exempt
def sparta_e632cd6259(request):
	if request.user.is_authenticated:A=1
	else:A=0
	B={_A:1,_C:A};C=json.dumps(B);return HttpResponse(C)
def sparta_a3da12f14a(request):
	B=request;from django.contrib.auth import authenticate as F,login;from django.contrib.auth.models import User as C;G=json.loads(B.body);D=json.loads(G[_B]);H=D['email'];I=D['password'];E=0
	try:
		A=C.objects.get(email=H);A=F(B,username=A.username,password=I)
		if A is not None:login(B,A);E=1
	except C.DoesNotExist:pass
	J={_A:1,_C:E};K=json.dumps(J);return HttpResponse(K)