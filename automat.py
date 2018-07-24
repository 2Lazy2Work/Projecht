import random
ITEMS = ["jablko", "hruska", "banan", "hrozno", "clover"]   

prve = None
druhe = None
tretie = None
peniaze = 50
def hrat():
	global prve, druhe, tretie, peniaze
	hrat = otazka()
	while hrat == True and peniaze != 0:
		prve = tocit()
		druhe = tocit()
		tretie = tocit()
		vypis()
		hrat = otazka()

def otazka():
	global peniaze
	odpoved = str(input("Chcete hrat dalej?"))
	if odpoved == "A":
		return True
	elif odpoved == N:
		return False
	else:
		print ("Zla odpoved")

def tocit():
	cislo = random.randint(0,4)
	return ITEMS[cislo]

def vypis():
	global prve, druhe, tretie, peniaze
	if prve == druhe == tretie == "clover":
		win = 200
	elif prve == druhe == tretie:
		win = 10
	elif prve == druhe:
		win = 5
	elif druhe == tretie:
		win = 5
	elif prve == tretie:
		win = 5
	else:
		win = -1
	peniaze += win
	if win > 0:
		print (prve, druhe, tretie,"Vyhral si", win)
	else:
		print (prve, druhe, tretie,"Prehral si")
hrat()