_K='has_access'
_J='session'
_I='plot_name'
_H='plot_chart_id'
_G=False
_F='login'
_E='plot_db_chart_obj'
_D='bCodeMirror'
_C='menuBar'
_B=None
_A=True
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import project.sparta_72a4072f41.sparta_07d0d78d96.qube_78b017fa56 as qube_78b017fa56
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_d6cbf19e98
from project.sparta_c7fea0e6b9.sparta_51d16e4350 import qube_78411fba20 as qube_78411fba20
@csrf_exempt
@sparta_d6cbf19e98
@login_required(redirect_field_name=_F)
def sparta_eedcd35dd7(request):
	B=request;C=B.GET.get('edit')
	if C is _B:C='-1'
	A=qube_78b017fa56.sparta_97cb8e2f6f(B);A[_C]=7;D=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(D);A[_D]=_A;A['edit_chart_id']=C;return render(B,'dist/project/plot-db/plotDB.html',A)
@csrf_exempt
@sparta_d6cbf19e98
@login_required(redirect_field_name=_F)
def sparta_83e9070b3e(request):
	A=request;C=A.GET.get('id');D=_G
	if C is _B:D=_A
	else:E=qube_78411fba20.sparta_80bc47ad29(C,A.user);D=not E[_K]
	if D:return sparta_eedcd35dd7(A)
	B=qube_78b017fa56.sparta_97cb8e2f6f(A);B[_C]=7;F=qube_78b017fa56.sparta_7bc7002ac2(A.user);B.update(F);B[_D]=_A;B[_H]=C;G=E[_E];B[_I]=G.name;return render(A,'dist/project/plot-db/plotFull.html',B)
@csrf_exempt
@sparta_d6cbf19e98
def sparta_49fa1604a9(request,id,api_token_id=_B):
	A=request
	if id is _B:B=A.GET.get('id')
	else:B=id
	return sparta_0a1d615af8(A,B)
@csrf_exempt
@sparta_d6cbf19e98
def sparta_09d20fd75b(request,widget_id,session_id,api_token_id):return sparta_0a1d615af8(request,widget_id,session_id)
def sparta_0a1d615af8(request,plot_chart_id,session='-1'):
	G='res';E=plot_chart_id;B=request;C=_G
	if E is _B:C=_A
	else:
		D=qube_78411fba20.sparta_6a80745453(E,B.user);H=D[G]
		if H==-1:C=_A
	if C:return sparta_eedcd35dd7(B)
	A=qube_78b017fa56.sparta_97cb8e2f6f(B);A[_C]=7;I=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(I);A[_D]=_A;F=D[_E];A['b_require_password']=0 if D[G]==1 else 1;A[_H]=F.plot_chart_id;A[_I]=F.name;A[_J]=str(session);return render(B,'dist/project/plot-db/widgets.html',A)
@csrf_exempt
@sparta_d6cbf19e98
def sparta_a5c8fd0c9a(request,session_id,api_token_id):B=request;A=qube_78b017fa56.sparta_97cb8e2f6f(B);A[_C]=7;C=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(C);A[_D]=_A;A[_J]=session_id;return render(B,'dist/project/plot-db/plotGUI.html',A)
@csrf_exempt
@sparta_d6cbf19e98
@login_required(redirect_field_name=_F)
def sparta_01ec0b7883(request):
	J=',\n    ';B=request;C=B.GET.get('id');E=_G
	if C is _B:E=_A
	else:F=qube_78411fba20.sparta_80bc47ad29(C,B.user);E=not F[_K]
	if E:return sparta_eedcd35dd7(B)
	K=qube_78411fba20.sparta_7ed6c63186(F[_E]);D='';G=0
	for(H,I)in K.items():
		if G>0:D+=J
		if I==1:D+=f"{H}=input_1"
		else:L=str(J.join([f"input_{A}"for A in range(I)]));D+=f"{H}=[{L}]"
		G+=1
	M=f'Spartaqube().get_widget(\n    "{C}"\n)';N=f'Spartaqube().plot_data(\n    "{C}",\n    {D}\n)';A=qube_78b017fa56.sparta_97cb8e2f6f(B);A[_C]=7;O=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(O);A[_D]=_A;A[_H]=C;P=F[_E];A[_I]=P.name;A['plot_data_cmd']=M;A['plot_data_cmd_inputs']=N;return render(B,'dist/project/plot-db/plotGUISaved.html',A)
@csrf_exempt
@sparta_d6cbf19e98
def sparta_2a13d39550(request,session_id,api_token_id,json_vars_html):B=request;A=qube_78b017fa56.sparta_97cb8e2f6f(B);A[_C]=7;C=qube_78b017fa56.sparta_7bc7002ac2(B.user);A.update(C);A[_D]=_A;A[_J]=session_id;A.update(json.loads(json_vars_html));return render(B,'dist/project/plot-db/plotAPI.html',A)