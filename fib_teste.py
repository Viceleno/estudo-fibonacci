# [0,1,1,2,3,5,8,13,21,34,55...]

# # recursiva
def vi(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    return vi(n-1)+vi(n-2)
  
# # memorizando
def vi_mem(n, mem = {1:0 , 2:1}):
  if n in mem:
    return mem[n]

  mem[n] = vi_mem(n-1, mem) + vi_mem(n-2, mem)
  return mem[n]

# iterativa
def vi_ite(n):
  n1 = 1
  n2 = 0
  counter = 3
  
  while counter<=n:
    vi_corr = n1 + n2
    n2 = n1
    n1 = vi_corr
    
    counter += 1
    
  return vi_corr



n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
print('Esse é o calculo usando a iteração!')
print(vi_mem(n))
print('Esse é o calculo usando a recursividade pura!')
print(vi(n))
print('Esse é o calculo usando a recursividade com memorização!')
print(vi_ite(n))