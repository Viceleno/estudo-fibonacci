# posição    [1,2,3,4,5,6,7,8 ,9 ,10,11]
# resultado  [0,1,1,2,3,5,8,13,21,34,55...]

import time

# # recursiva
def recursiva(n):
  if n==1:
    return 0
  elif n==2:
    return 1
  else:
    return recursiva(n-1)+recursiva(n-2)
  
n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
print('Esse é o calculo usando a recurção!')
start_time = time.time()  # Marca o tempo de início
print(recursiva(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução