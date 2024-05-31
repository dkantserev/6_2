n=int(input())
while(n<1 or n> 100000):
	print('Invalid request')
	n=int((input()))
m=[]
for i in range(n):
	el=int(input())
	
	while(el==0 or el>10e9):
		print('incorrect number')
		el=int(input())
		
	m.append(el)
	
def xxx (m):
	r=[]
	start=0
	for i in range(int(len(m))-1,int(len(m)/2)-1,-1):
			r.append(m[i])
			for j in range(start,int(len(m)/2)):
				r.append(m[j])
				start += 1
				break
		
	return r
print(xxx(m))
