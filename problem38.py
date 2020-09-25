def pan(n):
  n=str(n)
  if '1' in n and '2' in n and '3' in n and '4' in n and '5' in n and '6' in n and '9' in n and '7' in n and '8' in n and len(n)==9:
    return True
  else:
    return False
for i in range(9999,1,-1):
  print('i', i)
  s=''
  c=1
  while(True):
    s=s+str(i*c)
    #visualising purpose
    print(s)
    c+=1
    if len(s)==9 or len(s)>9:
      break
  if pan(int(s)):
    print(s)
    break  
