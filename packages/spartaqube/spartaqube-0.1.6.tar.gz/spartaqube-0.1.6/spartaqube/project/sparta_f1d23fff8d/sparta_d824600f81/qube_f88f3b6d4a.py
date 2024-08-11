_I='error.txt'
_H='zipName'
_G='utf-8'
_F='attachment; filename={0}'
_E='appId'
_D='Content-Disposition'
_C='res'
_B='projectPath'
_A='jsonData'
import json,base64
from django.http import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
from project.sparta_c7fea0e6b9.sparta_e13fd1328e import qube_d0427d5d49 as qube_d0427d5d49
from project.sparta_c7fea0e6b9.sparta_e13fd1328e import qube_4a0e53f76f as qube_4a0e53f76f
from project.sparta_c7fea0e6b9.sparta_957b17c2d6 import qube_4f323a8bf2 as qube_4f323a8bf2
from project.sparta_c7fea0e6b9.sparta_7639bac7be.qube_48eea7078d import sparta_fb40525a5b
@csrf_exempt
@sparta_fb40525a5b
def sparta_178fe9aea2(request):
	D='files[]';A=request;E=A.POST.dict();B=A.FILES
	if D in B:C=qube_d0427d5d49.sparta_db26ae4ab5(E,A.user,B[D])
	else:C={_C:1}
	F=json.dumps(C);return HttpResponse(F)
@csrf_exempt
@sparta_fb40525a5b
def sparta_a1996e3bf1(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_97ea889f42(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_161dbff04e(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_35686bccd3(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_45f49071de(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_bcf6a5318e(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_674656e4db(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_4a0e53f76f.sparta_09f5faca6f(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_6e9a1cd074(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_2f893cb1a1(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_5fb29740a8(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_2175dd8ea5(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_d19c97f24f(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_4cadf9fe10(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_c304eed2ef(request):A=request;B=json.loads(A.body);C=json.loads(B[_A]);D=qube_d0427d5d49.sparta_59d57c2929(C,A.user);E=json.dumps(D);return HttpResponse(E)
@csrf_exempt
@sparta_fb40525a5b
def sparta_4ceff982f1(request):
	F='filePath';E='fileName';A=request;B=A.GET[E];G=A.GET[F];H=A.GET[_B];I=A.GET[_E];J={E:B,F:G,_E:I,_B:base64.b64decode(H).decode(_G)};C=qube_d0427d5d49.sparta_790473ad83(J,A.user)
	if C[_C]==1:
		try:
			with open(C['fullPath'],'rb')as K:D=HttpResponse(K.read(),content_type='application/force-download');D[_D]='attachment; filename='+str(B);return D
		except Exception as L:pass
	raise Http404
@csrf_exempt
@sparta_fb40525a5b
def sparta_590210b308(request):
	E='folderName';C=request;F=C.GET[_B];D=C.GET[E];G={_B:base64.b64decode(F).decode(_G),E:D};B=qube_d0427d5d49.sparta_fc96e7a3a5(G,C.user);print(_C);print(B)
	if B[_C]==1:H=B['zip'];I=B[_H];A=HttpResponse();A.write(H.getvalue());A[_D]=_F.format(f"{I}.zip")
	else:A=HttpResponse();J=f"Could not download the folder {D}, please try again";K=_I;A.write(J);A[_D]=_F.format(K)
	return A
@csrf_exempt
@sparta_fb40525a5b
def sparta_a0a71d224c(request):
	B=request;D=B.GET[_E];E=B.GET[_B];F={_E:D,_B:base64.b64decode(E).decode(_G)};C=qube_d0427d5d49.sparta_f8f6176c13(F,B.user)
	if C[_C]==1:G=C['zip'];H=C[_H];A=HttpResponse();A.write(G.getvalue());A[_D]=_F.format(f"{H}.zip")
	else:A=HttpResponse();I='Could not download the application, please try again';J=_I;A.write(I);A[_D]=_F.format(J)
	return A