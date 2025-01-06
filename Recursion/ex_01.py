def ex_01(n):
  if n == 1 :
      r1 = 12
  else :
      r1 = n + ex_01(n//2)
  return r1
