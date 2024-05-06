import threading
import time

def calculadora_fibonacci(n):
    """
    Função para calcular o n-ésimo número da sequência de Fibonacci.

    Args:
        n (int): O número da posição na sequência.

    Returns:
        int: O valor da posição n na sequência de Fibonacci.
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1

    n1 = 0
    n2 = 1

    for _ in range(2, n):
        n1, n2 = n2, n1 + n2

    return n2

def calcular_blocos(start, end):
    """
    Função para calcular os números de Fibonacci em um intervalo específico.

    Args:
        start (int): O início do intervalo (inclusive).
        end (int): O final do intervalo (exclusive).

    Returns:
        list: Uma lista dos números de Fibonacci no intervalo especificado.
    """
    resultados = []
    for i in range(start, end):
        resultado = calculadora_fibonacci(i)
        resultados.append(resultado)
    return resultados

def paralelizar(n, num_threads):
    """
    Função para calcular os números de Fibonacci em paralelo usando threads.

    Args:
        n (int): O número da posição na sequência de Fibonacci a ser calculada.
        num_threads (int): O número de threads a serem usadas para paralelizar o cálculo.

    Returns:
        list: Uma lista contendo os números de Fibonacci calculados em paralelo.
    """
    threads = []
    resultados = []

    # Dividir o cálculo em blocos para cada thread
    tamanho_bloco = n // num_threads
    for i in range(num_threads):
        start = i * tamanho_bloco + 1
        end = (i + 1) * tamanho_bloco + 1 if i < num_threads - 1 else n + 1
        t = threading.Thread(target=lambda s=start, e=end: resultados.extend(calcular_blocos(s, e)))
        threads.append(t)
        t.start()

    # Aguardar todas as threads terminarem
    for t in threads:
        t.join()

    return resultados

# Número de threads para paralelizar
num_threads = int(input('Digite o número de Threads para o cálculo de Fibonacci: '))

# Número para calcular a sequência de Fibonacci
n = int(input('Digite um número para o cálculo de Fibonacci: '))

print(f'Este é o cálculo usando a iteração do número {n} com {num_threads} Threads!')

start_time = time.time()  # Marca o tempo de início
resultado = paralelizar(n, num_threads)
end_time = time.time()  # Marca o tempo de término

execution_time = end_time - start_time  # Calcula o tempo total de execução

print("Resultado:", resultado[-1])  # Exibe o último resultado da sequência
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução
