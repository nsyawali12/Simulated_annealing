import random
import math


tester = ("Hello World!")
print (tester)

feel = ("Tugas 1 Artificial Intelligence : Simulated-Annealling")
print (feel)

tempature = 10000 #inisialisai dengan temperatur bebas aku set dengan 10000
T = tempature
tMin = -19.2085 #nilai diambil sesuai saran dari Dosen
T1 = 1 #nilai T minimal
nTd = 0.9999 #nilai dingin yang ditentukan


def findmin(x1, x2):
	return -(math.fabs(math.sin(x1)*math.cos(x2)*math.exp(math.fabs(1-(math.sqrt(math.pow(x1,2)+(math.pow(x2,2)))/math.pi)))))

def boltzmanSA(dtE, T):
	return math.exp((-1*dtE)/T) #Rumus Boltzman Probabilitas

def findDelta(Fbr, Fskrang):
	Fbr - Fskrang

def searchRandom():
	return random.uniform(-10,10) #return random yang baru dengan batasan -10<=x1<=10 dan -10<=x2<20

def probabilitas(sol, final, T):
	return 2.71828**(-(final-sol))/T

# Main Program #		

x1 = searchRandom()
x2 = searchRandom()
sol = findmin(x1, x2)

while (T > T1):
	xbr1 = searchRandom()
	xbr2 = searchRandom()
	final = findmin(xbr1, xbr2)
	if (sol > final):
		sol = final
		print("Hasil final : ", sol)
	elif (probabilitas(sol,final,T)>random.random()):
		x1 = xbr1
		x2 = xbr2

	T *= nTd