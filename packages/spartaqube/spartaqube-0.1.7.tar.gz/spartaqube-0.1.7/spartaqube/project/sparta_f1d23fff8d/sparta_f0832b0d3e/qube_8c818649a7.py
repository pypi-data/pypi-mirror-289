_A='jsonData'
import json,inspect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as conf_settings
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from project.sparta_c7fea0e6b9.sparta_2de11a8994 import qube_d9a6859be2 as qube_d9a6859be2
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_fb40525a5b
@csrf_exempt
@sparta_fb40525a5b
def sparta_62d6a7aeef(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d9a6859be2.sparta_62d6a7aeef(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_d4960b9ce8(request):
	C='userObj';B=request;D=json.loads(B.body);E=json.loads(D[_A]);F=B.user;A=qube_d9a6859be2.sparta_d4960b9ce8(E,F)
	if A['res']==1:
		if C in list(A.keys()):login(B,A[C]);A.pop(C,None)
	G=json.dumps(A);return HttpResponse(G)
@csrf_exempt
@sparta_fb40525a5b
def sparta_e5c9784b1a(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=A.user;E=qube_d9a6859be2.sparta_e5c9784b1a(C,D);F=json.dumps(E);return HttpResponse(F)
@csrf_exempt
@sparta_fb40525a5b
def sparta_b92faffc77(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d9a6859be2.sparta_b92faffc77(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_610c9e418e(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d9a6859be2.sparta_610c9e418e(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_bc8247b35f(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d9a6859be2.sparta_bc8247b35f(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
def sparta_158b29a93b(request):A=json.loads(request.body);B=json.loads(A[_A]);C=qube_d9a6859be2.token_reset_password_worker(B);D=json.dumps(C);return HttpResponse(D)
@csrf_exempt
@sparta_fb40525a5b
def sparta_1f0cad136c(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d9a6859be2.network_master_reset_password(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
def sparta_7991ff7801(request):A=json.loads(request.body);B=json.loads(A[_A]);C=qube_d9a6859be2.sparta_7991ff7801(B);D=json.dumps(C);return HttpResponse(D)
@csrf_exempt
def sparta_9f6411575d(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d9a6859be2.sparta_9f6411575d(A,C);E=json.dumps(D);return HttpResponse(E)