import time
import concurrent.futures

def vi(n):
    if n <= 2:
        return n - 1
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future1 = executor.submit(vi, n-1)
        future2 = executor.submit(vi, n-2)
        return future1.result() + future2.result()

# Medindo o tempo de execução
start_time = time.time()
print(vi(20))  # Substitua 20 pelo valor de n que você deseja testar
end_time = time.time()

print("Tempo de execução: ", end_time - start_time)
