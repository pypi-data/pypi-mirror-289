import os
from project.sparta_72a4072f41.sparta_a34d606785.qube_418f54c31c import qube_418f54c31c
from project.sparta_72a4072f41.sparta_a34d606785.qube_1dadbaa4f3 import qube_1dadbaa4f3
from project.sparta_72a4072f41.sparta_a34d606785.qube_3f87295b8b import qube_3f87295b8b
from project.sparta_72a4072f41.sparta_a34d606785.qube_8f864c0301 import qube_8f864c0301
class db_connection:
	def __init__(A,dbType=0):A.dbType=dbType;A.dbCon=None
	def get_db_type(A):return A.dbType
	def getConnection(A):
		if A.dbType==0:
			from django.conf import settings as B
			if B.PLATFORM in['SANDBOX','SANDBOX_MYSQL']:return
			A.dbCon=qube_418f54c31c()
		elif A.dbType==1:A.dbCon=qube_1dadbaa4f3()
		elif A.dbType==2:A.dbCon=qube_3f87295b8b()
		elif A.dbType==4:A.dbCon=qube_8f864c0301()
		return A.dbCon