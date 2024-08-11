import time
def sparta_8352eb52a7():
	B=0;A=time.time()
	while True:B=A;A=time.time();yield A-B
TicToc=sparta_8352eb52a7()
def sparta_4e0ae5ecac(tempBool=True):
	A=next(TicToc)
	if tempBool:print('Elapsed time: %f seconds.\n'%A);return A
def sparta_97a695d837():sparta_4e0ae5ecac(False)