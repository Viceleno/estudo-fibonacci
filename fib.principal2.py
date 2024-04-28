# anotações 
# posição    [1,2,3,4,5,6,7,8 ,9 ,10,11,12,13 ,14 ,15 ...]
# resultado  [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377...]

import threading
import time

# Função para calcular a sequência de Fibonacci até um determinado índice
def calculate_fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Função para calcular a soma da sequência de Fibonacci em paralelo
def vi_parallel(n, num_threads):
    # Dividir o intervalo de cálculo entre as threads
    chunk_size = n // num_threads  # Tamanho do intervalo para cada thread
    threads = []  # Lista para armazenar as threads criadas
    results = []  # Lista para armazenar os resultados de cada thread
    
    # Função para calcular a sequência de Fibonacci em uma thread
    def worker(start, end):
        result = calculate_fibonacci(end) - calculate_fibonacci(start)  # Calcula o número na posição 'end' e subtrai o número na posição 'start'
        results.append(result)  # Adiciona o resultado à lista de resultados

    # Criar e iniciar threads para calcular em paralelo
    for i in range(num_threads):
        start = i * chunk_size  # Início do intervalo para esta thread
        end = (i + 1) * chunk_size if i < num_threads - 1 else n  # Fim do intervalo
        t = threading.Thread(target=worker, args=(start, end))  # Cria a thread
        threads.append(t)  # Adiciona a thread à lista
        t.start()  # Inicia a thread
    
    # Aguarda até que todas as threads terminem
    for t in threads:
        t.join()  # Aguarda a thread atual terminar

    # Retorna a soma dos resultados
    return sum(results)  # Retorna a soma dos resultados

# Exemplo de uso para n = 4000 com 8 threads
t = int(input('Digite o número de Threads para o cálculo de Fibonacci: \n'))  # Número de threads
n = int(input('Digite um número para o cálculo de Fibonacci: \n'))  # Número para calcular a sequência de Fibonacci
print(f'Este é o cálculo usando a iteração o número {n} com {t} Threads!')  # Exibe a mensagem com os parâmetros escolhidos

start_time = time.time()  # Marca o tempo de início
print(vi_parallel(n - 1, t))  # Chama a função para calcular a sequência de Fibonacci em paralelo
end_time = time.time()  # Marca o tempo de término

execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
