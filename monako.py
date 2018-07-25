from random import randint


print("Maroko")
print("Hrá sa s 3 kockami. Každý hráč hádže maximálne 3x,")
print("a to tak, aby získal maroko (dve rovnaké kocky), alebo veľké maroko (tri rovnaké kocky).")
print("Veľké Maroko je vždy viac ako malé, najviac je šestkové.")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
print("                                                          ")
print("prvy hod kockou :")

a = int(randint(1,6))
b = int(randint(1,6))
c = int(randint(1,6))
print("prva kocka :", a, "/druha kocka :", b, "/tretia kocka :", c)

if a == b == c:
	print("Velke Maroko!")
elif a == b:
	print("Maroko!")
elif b == c:
	print("Maroko!")
elif c == a:
	print("Maroko!")
else:
    print("nic")
print("Vyberte si z moznosti:")
print("1 - Znovu hadzat so vsetkymi kockami")
print("2 - Nechat lezat 1 kocku a dohadzovat s dvoma do Maroka")
print("3 - Nechat lezat 2 kocky a dohadzovat s jednou do Maroka")
rozhodnutie = int(input())

if rozhodnutie == 1:
	a = int(randint(1,6))
	b = int(randint(1,6))
	c = int(randint(1,6))
	print("prva kocka :", a, "/druha kocka :", b, "/tretia kocka :", c)
	if a == b == c:
		print("Velke Maroko!")
	elif a == b:
		print("Maroko!")
	elif b == c:
		print("Maroko!")
	elif c == a:
		print("Maroko!")
	else:
		print("nic")

if rozhodnutie == 2:
	print("vyberte kocku ktoru chcete nechat lezat:")
	print("prva kocka = 1")
	print("druha kocka = 2")
	print("tretia kocka = 3")
	kocka = int(input())
	if kocka == 1:
		b = int(randint(1,6))
		c = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)

		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")

	if kocka == 2:
		a = int(randint(1,6))
		c = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")

	if kocka == 3:
		a = int(randint(1,6))
		b = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
if rozhodnutie == 3:
	print("vyberte kocky ktore chcete nechat lezat:")
	print("prva kocka = 1")
	print("druha kocka = 2")
	print("tretia kocka = 3")
	print("kocka1: ")
	kocka = int(input())
	print("kocka2: ")
	kocka2 = int(input())
	if kocka == kocka2:
		print("nemozes vybrat dve rovnake kocky")
	if kocka == 1 and kocka2 == 2 or kocka == 2 and kocka2 == 1:
		c = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)

		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
	if kocka == 2 and kocka2 == 3 or kocka == 3 and kocka2 ==2:
		a = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
	if kocka == 1 and kocka2 == 3 or kocka == 3 and kocka2 ==1:
		b = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
print("Vyberte si z moznosti:")
print("1 - hadzat so vsetkymi kockami")
print("2 - nechat lezat 1 kocku a dohadzovat s dvoma do Maroka")
print("3 - nechat lezat 2 kocky a dohadzovat s jednou do Maroka")
rozhodnutie2 = int(input())

if rozhodnutie2 == 1:
	a = int(randint(1,6))
	b = int(randint(1,6))
	c = int(randint(1,6))
	print("prva kocka :", a, "/druha kocka :", b, "/tretia kocka :", c)
	if a == b == c:
		print("Velke Maroko!")
	elif a == b:
		print("Maroko!")
	elif b == c:
		print("Maroko!")
	elif c == a:
		print("Maroko!")
	else:
		print("nic")

if rozhodnutie2 == 2:
	print("vyberte kocku ktoru chcete nechat lezat:")
	print("prva kocka = 1")
	print("druha kocka = 2")
	print("tretia kocka = 3")
	kocka = int(input())
	if kocka == 1:
		b = int(randint(1,6))
		c = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)

		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")

	if kocka == 2:
		a = int(randint(1,6))
		c = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")

	if kocka == 3:
		a = int(randint(1,6))
		b = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
if rozhodnutie2 == 3:
	print("vyberte kocky ktore chcete nechat lezat:")
	print("prva kocka = 1")
	print("druha kocka = 2")
	print("tretia kocka = 3")
	print("kocka1: ")
	kocka = int(input())
	print("kocka2: ")
	kocka2 = int(input())
	if kocka == kocka2:
		print("nemozes vybrat dve rovnake kocky")
	if kocka == 1 and kocka2 == 2 or kocka == 2 and kocka2 == 1:
		c = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)

		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
	if kocka == 2 and kocka2 == 3 or kocka == 3 and kocka2 ==2:
		b = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")
	if kocka == 1 and kocka2 == 3 or kocka == 3 and kocka2 ==1:
		b = int(randint(1,6))
		print("/prva kocka :", a, "/druha kocka :", b, "/tretia kocka :",c)
		if a == b == c:
			print("Velke Maroko!")
		elif a == b:
			print("Maroko!")
		elif b == c:
			print("Maroko!")
		elif c == a:
			print("Maroko!")
		else:
			print("nic")









	






