
import random
import time
#valor ori de pi, que es diferente al estimado 
PI_REAL = 3.14159
def punto_dentro_circulo(x, y):
    return x * x + y * y < 0.5 * 0.5
# monte carlo
def monte_carlo(N):
    dentro = 0
    inicio = time.perf_counter()
    for i in range(N):
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)
        if punto_dentro_circulo(x, y):
            dentro += 1
    tiempo = time.perf_counter() - inicio
    pi_estimado = 4 * (dentro / N)
    error = abs(PI_REAL - pi_estimado)
    return pi_estimado, error, tiempo
#algoritmo de las vegas
def las_vegas(K):
    dentro = 0
    total = 0
    inicio = time.perf_counter()
    while dentro < K:
        x = random.uniform(-0.5, 0.5)
        y = random.uniform(-0.5, 0.5)
        total += 1
        if punto_dentro_circulo(x, y):
            dentro += 1
    tiempo = time.perf_counter() - inicio
    pi_estimado = 4 * (K / total)
    error = abs(PI_REAL - pi_estimado)
    return pi_estimado, error, tiempo, total


print("VALOR DE REFERENCIA DE PI:", PI_REAL)
print("\n*********** MONTE CARLO ***********")
for N in [1000, 10000, 100000, 1000000]:
    pi_est, error, tiempo = monte_carlo(N)
    print(f"N = {N}")
    print(f"Pi estimado: {pi_est:.6f}")
    print(f"Error: {error:.6f}")
    print(f"Tiempo: {tiempo:.6f} segundos")
    print()

print("\n*********** LAS VEGAS ***********")
for K in [1000, 10000, 100000, 1000000]:
    pi_est, error, tiempo, total = las_vegas(K)
    print(f"K = {K}")
    print(f"Puntos generados: {total}")
    print(f"Puntos fuera: {total - K}")
    print(f"Pi estimado: {pi_est:.6f}")
    print(f"Error: {error:.6f}")
    print(f"Tiempo: {tiempo:.6f} segundos")
    print()

# comparamos n y k 
print("\n=== ALGORITMO MONTE CARLO ===")
for N in [1000, 10000, 100000, 1000000]:
    pi_est, error, tiempo = monte_carlo(N)
    print(
        f"N = {N:<8} | "
        f"π est: {pi_est:.6f} | "
        f"Diferencia: {error:.6f} | "
        f"Tiempo: {tiempo * 1000:7.2f} ms"
    )
print("\n=== ALGORITMO LAS VEGAS ===")
for K in [785, 7854, 78540, 785398]:
    pi_est, error, tiempo, total = las_vegas(K)
    print(
        f"K = {K:<6} (N gen: {total:<7}) | "
        f"π est: {pi_est:.6f} | "
        f"Diferencia: {error:.6f} | "
        f"Tiempo: {tiempo * 1000:7.2f} ms"
    )



