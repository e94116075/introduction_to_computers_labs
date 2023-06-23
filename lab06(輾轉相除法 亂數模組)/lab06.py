def gcd(a,b):
  a1=a
  b1=b
  A=max(a,b)
  B=min(a,b)
  c=-1
  if A==0 or B==0:
    print("0¿¿gcd")
    return 0
  while c!=0 and B!=0:
    c=A%B
    if c==0:
      GCD=B
      if B!=1:
        print(a1,"¿",b1,"¿gcd=",GCD)
        return  GCD
      elif B==1:
        print(a,"¿",b,"¿¿")
        return  GCD
    B=B%c
    if B==0:
      GCD=c
      if c!=1:
        print(a1,"¿",b1,"¿gcd=",GCD)
        return GCD
      elif c==1:
        print(a,"¿",b,"¿¿")
    A=c
ans1=gcd(18,32)
ans2=gcd(10,0)
ans3=gcd(19,20)

