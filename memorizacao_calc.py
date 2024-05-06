# posição    [1,2,3,4,5,6,7,8 ,9 ,10,11]
# resultado  [0,1,1,2,3,5,8,13,21,34,55...]

import time

# memorizando
def memorizacao(n, mem = {1:0 , 2:1}):
  if n in mem:
    return mem[n]

  mem[n] = memorizacao(n-1, mem) + memorizacao(n-2, mem)
  return mem[n]

n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
print('Esse é o calculo usando a memorização!')
start_time = time.time()  # Marca o tempo de início
print(memorizacao(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução