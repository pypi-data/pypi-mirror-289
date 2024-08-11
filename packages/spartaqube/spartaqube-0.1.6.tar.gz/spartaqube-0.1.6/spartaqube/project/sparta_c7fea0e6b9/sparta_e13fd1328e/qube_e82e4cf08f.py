import os,zipfile,pytz
UTC=pytz.utc
from django.conf import settings as conf_settings
def sparta_1fcd7b40ac():
	B='APPDATA'
	if conf_settings.PLATFORMS_NFS:
		A='/var/nfs/notebooks/'
		if not os.path.exists(A):os.makedirs(A)
		return A
	if conf_settings.PLATFORM=='LOCAL_DESKTOP'or conf_settings.IS_LOCAL_PLATFORM:
		if conf_settings.PLATFORM_DEBUG=='DEBUG-CLIENT-2':return os.path.join(os.environ[B],'SpartaQuantNB/CLIENT2')
		return os.path.join(os.environ[B],'SpartaQuantNB')
	if conf_settings.PLATFORM=='LOCAL_CE':return'/app/notebooks/'
def sparta_6df77a0f4a(userId):A=sparta_1fcd7b40ac();B=os.path.join(A,userId);return B
def sparta_8a2f6ebcab(notebookProjectId,userId):A=sparta_6df77a0f4a(userId);B=os.path.join(A,notebookProjectId);return B
def sparta_2d575973e3(notebookProjectId,userId):A=sparta_6df77a0f4a(userId);B=os.path.join(A,notebookProjectId);return os.path.exists(B)
def sparta_8aef8633e0(notebookProjectId,userId,ipynbFileName):A=sparta_6df77a0f4a(userId);B=os.path.join(A,notebookProjectId);return os.path.isfile(os.path.join(B,ipynbFileName))
def sparta_1b4e2e04e8(notebookProjectId,userId):
	C=userId;B=notebookProjectId;D=sparta_8a2f6ebcab(B,C);G=sparta_6df77a0f4a(C);A=f"{G}/zipTmp/"
	if not os.path.exists(A):os.makedirs(A)
	H=f"{A}/{B}.zip";E=zipfile.ZipFile(H,'w',zipfile.ZIP_DEFLATED);I=len(D)+1
	for(J,M,K)in os.walk(D):
		for L in K:F=os.path.join(J,L);E.write(F,F[I:])
	return E
def sparta_e392c17681(notebookProjectId,userId):B=userId;A=notebookProjectId;sparta_1b4e2e04e8(A,B);C=f"{A}.zip";D=sparta_6df77a0f4a(B);E=f"{D}/zipTmp/{A}.zip";F=open(E,'rb');return{'zipName':C,'zipObj':F}