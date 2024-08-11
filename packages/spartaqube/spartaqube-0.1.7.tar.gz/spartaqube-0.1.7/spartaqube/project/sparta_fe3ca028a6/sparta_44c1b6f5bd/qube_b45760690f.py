from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings as conf_settings
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import hashlib,project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 as qube_78b017fa56
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_d6cbf19e98
@csrf_exempt
def sparta_ddea6cf9bc(request):B=request;A=qube_78b017fa56.sparta_97cb8e2f6f(B);A['menuBar']=8;A['bCodeMirror']=True;C=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(C);return render(B,'dist/project/api/api.html',A)