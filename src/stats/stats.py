from collections import Counter
import math

class Stats:
    def promedio(self, numeros):
        """
        Calcula la media aritmética de una lista de números.
        """
        if not numeros:
            return 0
        return sum(numeros) / len(numeros)
    
    def mediana(self, numeros):
        """
        Encuentra el valor mediano de una lista de números.
        """
        if not numeros:
            return 0
        nums = sorted(numeros)
        n = len(nums)
        mid = n // 2
        if n % 2 == 0:
            return (nums[mid - 1] + nums[mid]) / 2
        else:
            return nums[mid]
    
    def moda(self, numeros):
        """
        Encuentra el valor más frecuente en la lista.
        """
        if not numeros:
            return None
        contador = Counter(numeros)
        max_frec = max(contador.values())
        for num in numeros:
            if contador[num] == max_frec:
                return num
    
    def desviacion_estandar(self, numeros):
        """
        Calcula la desviación estándar poblacional.
        """
        if not numeros:
            return 0
        media = self.promedio(numeros)
        var = sum((x - media) ** 2 for x in numeros) / len(numeros)
        return math.sqrt(var)
    
    def varianza(self, numeros):
        """
        Calcula la varianza poblacional.
        """
        if not numeros:
            return 0
        media = self.promedio(numeros)
        return sum((x - media) ** 2 for x in numeros) / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango de la lista.
        """
        if not numeros:
            return 0
        return max(numeros) - min(numeros)
