_O='Please send valid data'
_N='dist/project/auth/resetPasswordChange.html'
_M='captcha'
_L='password'
_K='login'
_J='POST'
_I=False
_H='error'
_G='form'
_F='email'
_E='res'
_D='home'
_C='manifest'
_B='errorMsg'
_A=True
import json,hashlib,uuid
from datetime import datetime
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings as conf_settings
from django.urls import reverse
import project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 as qube_78b017fa56
from project.forms import ConnexionForm,RegistrationTestForm,RegistrationBaseForm,RegistrationForm,ResetPasswordForm,ResetPasswordChangeForm
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_d6cbf19e98
from project.sparta_c7fea0e6b9.sparta_7639bac7be import qube_48eea7078d as qube_48eea7078d
from project.sparta_f1d23fff8d.sparta_a76ed2732a import qube_905037d90f as qube_905037d90f
from project.models import LoginLocation,UserProfile
def sparta_c212c11ba6():return{'bHasCompanyEE':-1}
def sparta_03e7139418(request):B=request;A=qube_78b017fa56.sparta_97cb8e2f6f(B);A[_C]=qube_78b017fa56.sparta_7e71d2f59e();A['forbiddenEmail']=conf_settings.FORBIDDEN_EMAIL;return render(B,'dist/project/auth/banned.html',A)
@sparta_d6cbf19e98
def sparta_97a14e397f(request):
	C=request;B='/';A=C.GET.get(_K)
	if A is not None:D=A.split(B);A=B.join(D[1:]);A=A.replace(B,'$@$')
	return sparta_8d2fd5aefd(C,A)
def sparta_e98f397761(request,redirectUrl):return sparta_8d2fd5aefd(request,redirectUrl)
def sparta_8d2fd5aefd(request,redirectUrl):
	E=redirectUrl;A=request;print('Welcome to loginRedirectFunc')
	if A.user.is_authenticated:return redirect(_D)
	G=_I;H='Email or password incorrect'
	if A.method==_J:
		C=ConnexionForm(A.POST)
		if C.is_valid():
			I=C.cleaned_data[_F];J=C.cleaned_data[_L];F=authenticate(username=I,password=J)
			if F:
				if qube_48eea7078d.sparta_f851f0972a(F):return sparta_03e7139418(A)
				login(A,F);K,L=qube_78b017fa56.sparta_18a43f1cec();LoginLocation.objects.create(user=F,hostname=K,ip=L,date_login=datetime.now())
				if E is not None:
					D=E.split('$@$');D=[A for A in D if len(A)>0]
					if len(D)>1:M=D[0];return redirect(reverse(M,args=D[1:]))
					return redirect(E)
				return redirect(_D)
			else:G=_A
		else:G=_A
	C=ConnexionForm();B=qube_78b017fa56.sparta_97cb8e2f6f(A);B.update(qube_78b017fa56.sparta_8f2f0fd22c(A));B[_C]=qube_78b017fa56.sparta_7e71d2f59e();B[_G]=C;B[_H]=G;B['redirectUrl']=E;B[_B]=H;B.update(sparta_c212c11ba6());return render(A,'dist/project/auth/login.html',B)
@sparta_d6cbf19e98
def sparta_5f2799ed80(request):
	A=request
	if A.user.is_authenticated:return redirect(_D)
	E='';D=_I;F=qube_48eea7078d.sparta_1ec02864d3()
	if A.method==_J:
		if F:B=RegistrationForm(A.POST)
		else:B=RegistrationBaseForm(A.POST)
		if B.is_valid():
			I=B.cleaned_data;H=None
			if F:
				H=B.cleaned_data['code']
				if not qube_48eea7078d.sparta_04d6dd260c(H):D=_A;E='Wrong guest code'
			if not D:
				J=A.META['HTTP_HOST'];G=qube_48eea7078d.sparta_abcb534bb0(I,J)
				if int(G[_E])==1:K=G['userObj'];login(A,K);return redirect(_D)
				else:D=_A;E=G[_B]
		else:D=_A;E=B.errors.as_data()
	if F:B=RegistrationForm()
	else:B=RegistrationBaseForm()
	C=qube_78b017fa56.sparta_97cb8e2f6f(A);C.update(qube_78b017fa56.sparta_8f2f0fd22c(A));C[_C]=qube_78b017fa56.sparta_7e71d2f59e();C[_G]=B;C[_H]=D;C[_B]=E;C.update(sparta_c212c11ba6());return render(A,'dist/project/auth/registration.html',C)
def sparta_3103ff12bb(request):A=request;B=qube_78b017fa56.sparta_97cb8e2f6f(A);B[_C]=qube_78b017fa56.sparta_7e71d2f59e();return render(A,'dist/project/auth/registrationPending.html',B)
def sparta_68c4dd238c(request,token):
	A=request;B=qube_48eea7078d.sparta_67e138ebdf(token)
	if int(B[_E])==1:C=B['user'];login(A,C);return redirect(_D)
	D=qube_78b017fa56.sparta_97cb8e2f6f(A);D[_C]=qube_78b017fa56.sparta_7e71d2f59e();return redirect(_K)
def sparta_fc04e4867e(request):logout(request);return redirect(_K)
def sparta_a22e51d856(request):A={_E:-100,_B:'You are not logged...'};B=json.dumps(A);return HttpResponse(B)
@csrf_exempt
def sparta_1c52609adf(request):
	A=request;E='';F=_I
	if A.method==_J:
		B=ResetPasswordForm(A.POST)
		if B.is_valid():
			H=B.cleaned_data[_F];I=B.cleaned_data[_M];G=qube_48eea7078d.sparta_1c52609adf(H.lower(),I)
			try:
				if int(G[_E])==1:C=qube_78b017fa56.sparta_97cb8e2f6f(A);C.update(qube_78b017fa56.sparta_8f2f0fd22c(A));B=ResetPasswordChangeForm(A.POST);C[_C]=qube_78b017fa56.sparta_7e71d2f59e();C[_G]=B;C[_F]=H;C[_H]=F;C[_B]=E;return render(A,_N,C)
				elif int(G[_E])==-1:E=G[_B];F=_A
			except Exception as J:print('exception ');print(J);E='Could not send reset email, please try again';F=_A
		else:E=_O;F=_A
	else:B=ResetPasswordForm()
	D=qube_78b017fa56.sparta_97cb8e2f6f(A);D.update(qube_78b017fa56.sparta_8f2f0fd22c(A));D[_C]=qube_78b017fa56.sparta_7e71d2f59e();D[_G]=B;D[_H]=F;D[_B]=E;D.update(sparta_c212c11ba6());return render(A,'dist/project/auth/resetPassword.html',D)
@csrf_exempt
def sparta_e3b0d20ba6(request):
	D=request;E='';B=_I
	if D.method==_J:
		C=ResetPasswordChangeForm(D.POST)
		if C.is_valid():
			I=C.cleaned_data['token'];F=C.cleaned_data[_L];J=C.cleaned_data['password_confirmation'];K=C.cleaned_data[_M];G=C.cleaned_data[_F].lower()
			if len(F)<6:E='Your password must be at least 6 characters';B=_A
			if F!=J:E='The two passwords must be identical...';B=_A
			if not B:
				H=qube_48eea7078d.sparta_e3b0d20ba6(K,I,G.lower(),F)
				try:
					if int(H[_E])==1:L=User.objects.get(username=G);login(D,L);return redirect(_D)
					else:E=H[_B];B=_A
				except Exception as M:E='Could not change your password, please try again';B=_A
		else:E=_O;B=_A
	else:return redirect('reset-password')
	A=qube_78b017fa56.sparta_97cb8e2f6f(D);A.update(qube_78b017fa56.sparta_8f2f0fd22c(D));A[_C]=qube_78b017fa56.sparta_7e71d2f59e();A[_G]=C;A[_H]=B;A[_B]=E;A[_F]=G;A.update(sparta_c212c11ba6());return render(D,_N,A)