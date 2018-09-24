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
	f = -(abs(math.sin(x1)*math.cos(x2)*math.exp(abs(1-(math.sqrt(x1**2+x2**2)/math.pi)))))

def boltzmanSA(dtE, T):
	return math.exp((-1*dtE)/T) #Rumus Boltzman Probabilitas

def thermodynamic(E, f, x):
	E == f

def searchRandom(rx):
	