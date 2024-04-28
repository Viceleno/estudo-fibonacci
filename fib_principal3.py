import threading
import time

# Função recursiva para calcular o termo n da sequência de Fibonacci
def fibo_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo_recursive(n - 1) + fibo_recursive(n - 2)

# Função para calcular a soma da sequência de Fibonacci em paralelo
def parallel_fibonacci(n, num_threads):
    chunk_size = n // num_threads  # Tamanho do intervalo para cada thread
    results = []  # Lista para armazenar os resultados de cada thread

    # Função para calcular a sequência de Fibonacci em uma thread
    def worker(start, end):
        result = sum(fibo_recursive(i) for i in range(start, end))
        results.append(result)

    # Criar e iniciar threads para calcular em paralelo
    threads = []
    for i in range(num_threads):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < num_threads - 1 else n
        t = threading.Thread(target=worker, args=(start, end))
        threads.append(t)
        t.start()

    # Aguarda até que todas as threads terminem
    for t in threads:
        t.join()

    # Retorna o resultado do termo n da sequência de Fibonacci
    return results[0] if results else 0

def main():
    n = int(input("Digite a posição do termo na sequência de Fibonacci: "))
    num_threads = int(input("Digite o número de threads para paralelização: "))

    start_time = time.time()
    result = parallel_fibonacci(n, num_threads)
    end_time = time.time()

    print(f"O {n}º termo da sequência de Fibonacci é: {result}")
    print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()



# n = int(input("Digite um número para calcular a sequência de Fibonacci: "))
# import threading
# import time

# # Função para calcular a sequência de Fibonacci até um determinado índice
# def calculate_fibonacci(n, fib_values):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     elif fib_values[n] is None:
#         fib_values[n] = calculate_fibonacci(n-1, fib_values) + calculate_fibonacci(n-2, fib_values)
#     return fib_values[n]

# # Função para calcular a soma da sequência de Fibonacci em paralelo
# def vi_parallel(n, num_threads):
#     fib_values = [None] * (n + 1)  # Lista para armazenar os valores calculados de Fibonacci
#     fib_values[0] = 0
#     fib_values[1] = 1

#     # Dividir o intervalo de cálculo entre as threads
#     chunk_size = n // num_threads  # Tamanho do intervalo para cada thread
#     threads = []  # Lista para armazenar as threads criadas
#     results = []  # Lista para armazenar os resultados de cada thread
    
#     # Função para calcular a soma da sequência de Fibonacci em uma thread
#     def worker(start, end):
#         result = sum(calculate_fibonacci(i, fib_values) for i in range(start, end))  # Calcula a soma da sequência de Fibonacci no intervalo
#         results.append(result)  # Adiciona o resultado à lista de resultados

#     # Criar e iniciar threads para calcular em paralelo
#     for i in range(num_threads):
#         start = i * chunk_size  # Início do intervalo para esta thread
#         end = (i + 1) * chunk_size if i < num_threads - 1 else n  # Fim do intervalo
#         t = threading.Thread(target=worker, args=(start, end))  # Cria a thread
#         threads.append(t)  # Adiciona a thread à lista
#         t.start()  # Inicia a thread
    
#     # Aguarda até que todas as threads terminem
#     for t in threads:
#         t.join()  # Aguarda a thread atual terminar

#     # Retorna a soma dos resultados
#     return sum(results)  # Retorna a soma dos resultados

# # Exemplo de uso para n = 4000 com 8 threads
# t = int(input('Digite o número de Threads para o cálculo de Fibonacci: \n'))  # Número de threads
# n = int(input('Digite um número para o cálculo de Fibonacci: \n'))  # Número para calcular a sequência de Fibonacci
# print(f'Este é o cálculo usando a iteração o número {n} com {t} Threads!')  # Exibe a mensagem com os parâmetros escolhidos

# start_time = time.time()  # Marca o tempo de início
# print(vi_parallel(n, t))  # Chama a função para calcular a sequência de Fibonacci em paralelo
# end_time = time.time()  # Marca o tempo de término

# execution_time = end_time - start_time  # Calcula o tempo total de execução
# print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
