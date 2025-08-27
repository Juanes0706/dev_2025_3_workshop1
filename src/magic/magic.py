class Magic:
    """
    Clase con métodos para juegos matemáticos, secuencias especiales y algoritmos numéricos.
    Incluye implementaciones de Fibonacci, números perfectos, triángulo de Pascal etc.
    """

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("n debe ser un número entero no negativo")
        if n == 0:
            return 0
        elif n == 1:
            return 1
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        secuencia = [0, 1]
        while len(secuencia) < n:
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia[:n]

    def es_primo(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def generar_primos(self, n):
        return [i for i in range(2, n + 1) if self.es_primo(i)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma_divisores = 1
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                suma_divisores += i
                if i != n // i:
                    suma_divisores += n // i
        return suma_divisores == n

    def triangulo_pascal(self, filas):
        triangulo = []
        for i in range(filas):
            fila = [1] * (i + 1)
            for j in range(1, i):
                fila[j] = triangulo[i - 1][j - 1] + triangulo[i - 1][j]
            triangulo.append(fila)
        return triangulo

    def factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        resultado = 1
        for i in range(2, n + 1):
            resultado *= i
        return resultado

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a * b) // self.mcd(a, b)

    def suma_digitos(self, n):
        return sum(int(d) for d in str(abs(n)))

    def es_numero_armstrong(self, n):
        digitos = str(n)
        potencia = len(digitos)
        suma = sum(int(d)**potencia for d in digitos)
        return suma == n

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        suma_objetivo = sum(matriz[0])

       
        for fila in matriz:
            if sum(fila) != suma_objetivo:
                return False

       
        for col in range(n):
            if sum(matriz[f][col] for f in range(n)) != suma_objetivo:
                return False

        
        if sum(matriz[i][i] for i in range(n)) != suma_objetivo:
            return False

        
        if sum(matriz[i][n - 1 - i] for i in range(n)) != suma_objetivo:
            return False

        return True
