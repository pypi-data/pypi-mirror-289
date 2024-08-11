import json,base64,asyncio,subprocess,uuid,requests,pandas as pd
from subprocess import PIPE
from django.db.models import Q
from datetime import datetime,timedelta
import pytz
UTC=pytz.utc
from project.models_spartaqube import DBConnector,DBConnectorUserShared,PlotDBChart,PlotDBChartShared
from project.models import ShareRights
from project.sparta_c7fea0e6b9.sparta_fe626c7ed8 import qube_ad878641d5 as qube_ad878641d5
from project.sparta_c7fea0e6b9.sparta_fce7d0cfbc import qube_180ac161b4
from project.sparta_c7fea0e6b9.sparta_51d16e4350 import qube_60a0d4ffd7 as qube_60a0d4ffd7
from project.sparta_c7fea0e6b9.sparta_fce7d0cfbc.qube_946a9c1099 import Connector as Connector
def sparta_59afe8ca3a(json_data,user_obj):
	D='key';A=json_data;print('Call autocompelte api');print(A);B=A[D];E=A['api_func'];C=[]
	if E=='tv_symbols':C=sparta_3c81f12289(B)
	return{'res':1,'output':C,D:B}
def sparta_3c81f12289(key_symbol):
	F='</em>';E='<em>';B='symbol_id';G=f"https://symbol-search.tradingview.com/local_search/v3/?text={key_symbol}&hl=1&exchange=&lang=en&search_type=undefined&domain=production&sort_by_country=US";C=requests.get(G)
	try:
		if int(C.status_code)==200:
			H=json.loads(C.text);D=H['symbols']
			for A in D:A[B]=A['symbol'].replace(E,'').replace(F,'');A['title']=A[B];A['subtitle']=A['description'].replace(E,'').replace(F,'');A['value']=A[B]
			return D
		return[]
	except:return[]