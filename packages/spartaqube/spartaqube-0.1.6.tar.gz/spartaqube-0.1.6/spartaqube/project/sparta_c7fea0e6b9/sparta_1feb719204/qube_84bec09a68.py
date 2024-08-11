_A='utf-8'
import os,json,base64,hashlib,random
from cryptography.fernet import Fernet
def sparta_cdad512a68():A='__API_AUTH__';A=A.encode(_A);A=hashlib.md5(A).hexdigest();A=base64.b64encode(A.encode(_A));return A
def sparta_63634151d4(objectToCrypt):A=objectToCrypt;C=sparta_cdad512a68();D=Fernet(C);A=A.encode(_A);B=D.encrypt(A).decode(_A);B=base64.b64encode(B.encode(_A)).decode(_A);return B
def sparta_5a4836e284(apiAuth):A=apiAuth;B=sparta_cdad512a68();C=Fernet(B);A=base64.b64decode(A);return C.decrypt(A).decode(_A)
def sparta_e0ca92ce2f(kCrypt):A='__SQ_AUTH__'+str(kCrypt);A=A.encode(_A);A=hashlib.md5(A).hexdigest();A=base64.b64encode(A.encode(_A));return A
def sparta_3a37abe674(objectToCrypt,kCrypt):A=objectToCrypt;C=sparta_e0ca92ce2f(kCrypt);D=Fernet(C);A=A.encode(_A);B=D.encrypt(A).decode(_A);B=base64.b64encode(B.encode(_A)).decode(_A);return B
def sparta_a4852538b2(objectToDecrypt,kCrypt):A=objectToDecrypt;B=sparta_e0ca92ce2f(kCrypt);C=Fernet(B);A=base64.b64decode(A);return C.decrypt(A).decode(_A)
def sparta_3842e1d7aa(kCrypt):A='__SQ_EMAIL__'+str(kCrypt);A=A.encode(_A);A=hashlib.md5(A).hexdigest();A=base64.b64encode(A.encode(_A));return A
def sparta_c747a1ad2f(objectToCrypt,kCrypt):A=objectToCrypt;C=sparta_3842e1d7aa(kCrypt);D=Fernet(C);A=A.encode(_A);B=D.encrypt(A).decode(_A);B=base64.b64encode(B.encode(_A)).decode(_A);return B
def sparta_879f112f00(objectToDecrypt,kCrypt):A=objectToDecrypt;B=sparta_3842e1d7aa(kCrypt);C=Fernet(B);A=base64.b64decode(A);return C.decrypt(A).decode(_A)
def sparta_4b68650332(kCrypt):A='__SQ_KEY_SSO_CRYPT__'+str(kCrypt);A=A.encode(_A);A=hashlib.md5(A).hexdigest();A=base64.b64encode(A.encode(_A));return A
def sparta_fc0410cf9f(objectToCrypt,kCrypt):A=objectToCrypt;C=sparta_4b68650332(kCrypt);D=Fernet(C);A=A.encode(_A);B=D.encrypt(A).decode(_A);B=base64.b64encode(B.encode(_A)).decode(_A);return B
def sparta_f7127a1463(objectToDecrypt,kCrypt):A=objectToDecrypt;B=sparta_4b68650332(kCrypt);C=Fernet(B);A=base64.b64decode(A);return C.decrypt(A).decode(_A)