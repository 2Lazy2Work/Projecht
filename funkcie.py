meno = str
def menu():
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print ("1. Nova hra")
	print ("2. Skoncit")
	print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	volba = int(input())
	if volba == 1:
		nova_hra()
	else:
		exit()

def nova_hra():
	global meno
	print ("Meno postavy?")
	meno = str(input())
	vyber_hry()

def vyber_hry():
	print ("Vyber si hru:")
	print ("1. Maroko")
	print ("2. OKO")
	print ("3. Automat")
	volba = int(input())
	if volba == 1:
		maroko()
	elif volba == 2:
		oko()
	elif volba == 3:
		automat()
