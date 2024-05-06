import time

def iterativa(n):
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


n = int(input('Digite um numero para o calculo de Fibonacci: \n'))
print('Esse é o calculo usando iteração!')
start_time = time.time()  # Marca o tempo de início
print(iterativa(n))
end_time = time.time()  # Marca o tempo de término
execution_time = end_time - start_time  # Calcula o tempo total de execução
print("Tempo de execução:", execution_time, "segundos")  # Exibe o tempo de execução