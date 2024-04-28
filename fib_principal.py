import threading
import time

def calculate_fib_range(start, end, result_list):
    for i in range(start, end):
        result_list[i] = vi_iterative(i + 1)

def vi_parallel(n, num_threads):
    result_list = [None] * n
    chunk_size = n // num_threads
    threads = []
    
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else n
        
        t = threading.Thread(target=calculate_fib_range, args=(start, end, result_list))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
    
    return result_list[-1]

def vi_iterative(n):
    if n < 2:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Exemplo de uso para n = 4000 com 8 threads
t = int(input('Digite o numero de Threads para o calculo de Fibonacci: \n'))
n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
print(f'Esse é o calculo usando a iteração o numero {n} com {t} Threads!')
 

start_time = time.time()
print(vi_parallel(n - 1, t))
end_time = time.time()

execution_time = end_time - start_time
print("Tempo de execução:", execution_time, "segundos")

# import threading
# import time

# def calculate_fib_range(start, end, result_list):
#     for i in range(start, end):
#         result_list[i] = vi_iterative(i + 1)

# def vi_parallel(n, num_threads):
#     result_list = [None] * n
#     chunk_size = n // num_threads
#     threads = []
    
#     for i in range(num_threads):
#         start = i * chunk_size
#         end = (i + 1) * chunk_size if i < num_threads - 1 else n
        
#         t = threading.Thread(target=calculate_fib_range, args=(start, end, result_list))
#         threads.append(t)
#         t.start()
#         print(f"Thread {i+1} iniciada para calcular índices {start} até {end-1}")

#     for t in threads:
#         t.join()
    
#     return result_list[-1]

# def vi_iterative(n):
#     if n < 2:
#         return n
    
#     a, b = 0, 1
#     for _ in range(2, n + 1):
#         a, b = b, a + b
#     return b

# # Exemplo de uso para n = 4000 com 8 threads
# t = int(input('Digite o numero de Threads para o calculo de Fibonacci: \n'))
# n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
# print(f'Esse é o calculo usando a iteração o numero {n} com {t} Threads!')
 

# start_time = time.time()
# print(vi_parallel(n - 1, t))
# end_time = time.time()

# execution_time = end_time - start_time
# print("Tempo de execução:", execution_time, "segundos")
