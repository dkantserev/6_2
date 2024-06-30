n=int(input())
while(n<1 or n> 100000):
	print('Invalid request')
	n=int((input()))
	

m=list(map(int,input().split(' ')))
newMassive=[]
while (len(m)<n or len(m)>n):
	print("введите n(",n, ") чисел")
	m=list(map(int,input().split(' ')))





def lastToFirst():
	m.insert(0,m.pop(len(m)-1))
	
lastToFirst()

for i in m:
	newMassive.append(i)
print(newMassive)
