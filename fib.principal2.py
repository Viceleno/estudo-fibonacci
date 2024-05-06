'''  anotações 
posição    [1,2,3,4,5,6,7,8 ,9 ,10,11,12,13 ,14 ,15 ...]
resultado  [0,1,1,2,3,5,8,13,21,34,55,89,144,233,377...] '''

import threading
import time

# # Função para calcular a sequência de Fibonacci até um determinado índice
# def calculadora_fibonacci(n):
#     # Inicializa os dois primeiros termos da sequência de Fibonacci
#     a, b = 0, 1

#     # Loop para calcular os próximos termos da sequência até o n-ésimo termo
#     for _ in range(n):
#         # Atualiza os valores de a e b para os próximos termos
#         a, b = b, a + b

#     # Retorna o n-ésimo termo da sequência de Fibonacci
#     return a


def calculadora_fibonacci(n):
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

def vi_parallel(n, num_threads):
    threads = []  # Lista para armazenar as threads criadas
    results = []  # Lista para armazenar os resultados finais de cada thread

    # Função para calcular a sequência de Fibonacci em uma thread
    def worker(start, end):
        result = sum(calculadora_fibonacci(i) for i in range(start, end))
        results.append(result)  # Adiciona o resultado à lista de resultados finais

    # Criar e iniciar threads para calcular em paralelo
    for i in range(num_threads):
        start = (n // num_threads) * i + 1  # Início do intervalo para esta thread
        end = (n // num_threads) * (i + 1) if i < num_threads - 1 else n + 1  # Fim do intervalo
        t = threading.Thread(target=worker, args=(start, end))  # Cria a thread
        threads.append(t)  # Adiciona a thread à lista
        t.start()  # Inicia a thread
    
    # Aguarda até que todas as threads terminem
    for t in threads:
        t.join()  # Aguarda a thread atual terminar

    # Retorna a soma dos resultados finais
    return sum(results)  # Retorna a soma dos resultados finais

# Exemplo de uso para n = 4000 com 8 threads
t = int(input('Digite o número de Threads para o cálculo de Fibonacci: \n'))  # Número de threads
n = int(input('Digite um número para o cálculo de Fibonacci: \n'))  # Número para calcular a sequência de Fibonacci
print(f'Este é o cálculo usando a iteração o número {n} com {t} Threads!')  # Exibe a mensagem com os parâmetros escolhidos

start_time = time.time()  # Marca o tempo de início
print(vi_parallel(n, t))  # Chama a função para calcular a sequência de Fibonacci em paralelo
end_time = time.time()  # Marca o tempo de término

execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
