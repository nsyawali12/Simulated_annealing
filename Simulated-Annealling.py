import math
import random

tester = ("Hello World!")
print (tester)

print ("This is my first A.I Project : Simulated-Annealling")

tempature = 10000 #inisialisai dengan temperatur bebas aku set dengan 10000
T = tempature
c = 0.06 #nilai diambil sesuai saran dari kertas pak sunjana berikan 0.4 - 0.6
n = 100 #range


def findmin(x1, x2):
	return -(math.fabs(math.sin(x1)*math.cos(x2)*math.exp(math.fabs(1-(math.sqrt(math.pow(x1,2)+(math.pow(x2,2)))/math.pi)))))

def boltzmanSA(dtE, T):
	return math.exp((-1*dtE)/T) #Rumus Boltzman Probabilitas

def findDelta(Fbr, Fskrang):
	Fbr - Fskrang

def searchRandom(rx):
	return random.uniform(-10,10) #return random yang baru dengan batasan -10<=x1<=10 dan -10<=x2<20

#rumus evaluasi 
# DeltaE = f(currentstate) - f(newstate)



initial_1 = random.uniform(-10, -10) #initial state 1 
initial_2 = random.uniform(-10, -10)

stateskr_1 = initial_1
stateskr_2 = initial_2

BFS = findmin(stateskr_1, stateskr_2) #mencari state sekarang 

while T > n:
	print ("T= %f" %T)
	stateBr1 = searchRandom(stateskr_1)
	stateBr2 = searchRandom(stateskr_2)

	Fskrang = findmin(stateskr_1, stateskr_2)
	Fbr = findmin(stateBr1, stateBr2)

	print ("X1 Sekarang = %f" %stateskr_1)
	print ("X2 Sekarang = %f" %stateskr_2)

	print ("X1 Baru = %f" %stateBr1)
	print ("x2 Baru = %f" %stateBr2)

	print("F sekarang =" %Fskrang)

	print("F baru = %f" %FBr)

	dtE = Fbr - Fskrang

	print("delta E= %f" %dtE)

	if(Fbr < Fskrang ):
		stateskr_1 = stateBr1
		stateskr_2 = stateBr2
		BFS = findmin(stateBr1, stateBr2)
	else :
		randomNumber = random.uniform(0, 1)
		p = boltzmanSA(dtE, T)
		if (randomNumber < p):
			stateskr_1 = stateBr1
			stateskr_2 = stateBr2

	print("BFS: %f" %BFS)
	print("\n")

	T = T*0.9
	
print("Final: %f" %BFS) #hasil final dari SA

