"""
1        1
12      21
123    321
1234  4321
1234554321
"""
n=int(input())
for i in range(1,n+1):
  for j in range(1,i+1):
    print(j,end="")
    j+=1
  for k in range(1,(2*n-2*i)+1):
    print(" ",end="")
    k+=1
  temp=i
  for l in range(temp,0,-1):
    print(temp,end="")
    temp-=1
  print()
  i=i+1
