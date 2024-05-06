# import time
# import concurrent.futures

# def vi(n):
#     if n <= 2:
#         return n - 1
#     with concurrent.futures.ThreadPoolExecutor() as executor:
#         future1 = executor.submit(vi, n-1)
#         future2 = executor.submit(vi, n-2)
#         return future1.result() + future2.result()

# # Medindo o tempo de execução
# start_time = time.time()
# print(vi(20))  # Substitua 20 pelo valor de n que você deseja testar
# end_time = time.time()

# print("Tempo de execução: ", end_time - start_time)


def calculadora_fibonacci(n):
    # Inicializa os dois primeiros termos da sequência de Fibonacci
    a, b = 0, 1

    # Loop para calcular os próximos termos da sequência até o n-ésimo termo
    for _ in range(n):
        # Atualiza os valores de a e b para os próximos termos
        a, b = b, a + b

    # Retorna o n-ésimo termo da sequência de Fibonacci
    return a
