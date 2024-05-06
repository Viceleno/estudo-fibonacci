# posição    [1,2,3,4,5,6,7,8 ,9 ,10,11]
# resultado  [0,1,1,2,3,5,8,13,21,34,55...]

import time

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
    if n == 1:
        return 0
    elif n == 2:
        return 1

    n1 = 0
    n2 = 1
    counter = 3

    while counter <= n:
        n_corrente = n1 + n2
        n1 = n2
        n2 = n_corrente

        counter += 1

    return n_corrente



def calculate_fibonacci(n):
  if n == 1:
    return 0
  elif n == 2:
    return 1

  a, b = 0, 1
  for _ in range(n - 1):
    a, b = b, a + b
  return a



n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
print('Esse é o calculo usando a memorização!')
start_time = time.time()  # Marca o tempo de início
print(vi_mem(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
print('Esse é o calculo usando a recursividade!')
start_time = time.time()  # Marca o tempo de início
print(vi(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
print('Esse é o calculo usando a iteração!')
start_time = time.time()  # Marca o tempo de início
print(vi_ite(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
print('Esse é o calculo usando iteração sucinta!')
start_time = time.time()  # Marca o tempo de início
print(calculate_fibonacci(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução