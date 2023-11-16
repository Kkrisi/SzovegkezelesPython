



#I.	Kérjünk be egy szöveget és végezzük el rajta a következő műveleteket, majd minden végeredmény jelenítsünk meg a képernyőn még akkor is, ha ezt a feladat külön nem írja! (konzolos feladat)
#1.	Számoljuk meg hány szóköz van a szövegben! 


def ElsoFeladat(szoveg):
	osszeg = 0
	for betu in szoveg:
		if betu == " ":
			osszeg += 1
	return osszeg













#2.	Írjuk ki a szöveget a képernyőre szóközök nélkül. A továbbiakban ezzel a szöveggel dolgozzunk!
def MasodikFeladat(szoveg):
	return szoveg.replace(" ","")










#3.	Alakítsuk a szöveget kisbetűssé! A továbbiakkal ezzel a szöveggel dolgozzunk!
def HarmadikFeladat(szoveg):
	return szoveg.lower()











#4.	Cseréljük ki az összes ékezetes karaktert ékezet nélkülire ! A továbbiakkal ezzel a szöveggel dolgozzunk!
import unicodedata
def NegyedikFeladat(szoveg):
	return unicodedata.normalize('NFKD', szoveg).encode('ASCII', 'ignore').decode('utf-8', 'ignore')










#5.	Írd ki a szöveget fordítva a képernyőre!
def OtodikFeladat(szoveg):
	i = len(szoveg)-1
	while i >= 0:
		print(szoveg[i],end=" ")
		i -= 1













#6.	Hány magánhangzó van a szövegben? Hány mássalhangzó?
def HatodikFeladat(szoveg):
	maganh = 0
	massalh = 0
	for betu in szoveg:
		if(betu=='A' or betu=='a' or betu=='E' or betu =='e' or betu=='I' or betu=='i' or betu=='O' or betu=='o' or betu=='U' or betu=='u'):
			maganh += 1
		elif not (betu == " " or betu == "."):
			massalh += 1
	return massalh, maganh

































