from urllib.parse import urlparse,urlunparse
from django.contrib.auth.decorators import login_required
from django.conf import settings as conf_settings
from django.shortcuts import render
import project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 as qube_78b017fa56
from project.models import UserProfile
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_d6cbf19e98
from project.sparta_fe3ca028a6.sparta_4adf789d23.qube_70a35f0dc8 import sparta_c212c11ba6
@sparta_d6cbf19e98
@login_required(redirect_field_name='login')
def sparta_e1c5721f20(request,idSection=1):
	B=request;D=UserProfile.objects.get(user=B.user);E=D.avatar
	if E is not None:E=D.avatar.avatar
	C=urlparse(conf_settings.URL_TERMS)
	if not C.scheme:C=urlunparse(C._replace(scheme='http'))
	F={'item':1,'idSection':idSection,'userProfil':D,'avatar':E,'url_terms':C};A=qube_78b017fa56.sparta_97cb8e2f6f(B);A.update(qube_78b017fa56.sparta_7bc7002ac2(B.user));A.update(F);G='';A['accessKey']=G;A.update(sparta_c212c11ba6());return render(B,'dist/project/auth/settings.html',A)