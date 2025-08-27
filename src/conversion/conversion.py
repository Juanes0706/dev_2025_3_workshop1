class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        """
        Convierte temperatura de Celsius a Fahrenheit.
        """
        return (celsius * 9 / 5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        """
        Convierte temperatura de Fahrenheit a Celsius.
        """
        return (fahrenheit - 32) * 5 / 9

    def metros_a_pies(self, metros):
        """
        Convierte distancia de metros a pies.
        """
        return metros * 3.28084

    def pies_a_metros(self, pies):
        """
        Convierte distancia de pies a metros.
        """
        return pies * 0.3048

    def decimal_a_binario(self, decimal):
        """
        Convierte un número decimal a su representación binaria.
        """
        return bin(decimal)[2:]

    def binario_a_decimal(self, binario):
        """
        Convierte un número binario a decimal.
        """
        return int(binario, 2)

    def decimal_a_romano(self, numero):
        """
        Convierte un número decimal a numeración romana.
        """
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV", "I"
        ]
        romano = ""
        i = 0
        while numero > 0:
            for _ in range(numero // val[i]):
                romano += syms[i]
                numero -= val[i]
            i += 1
        return romano

    def romano_a_decimal(self, romano):
        """
        Convierte un número romano a decimal.
        """
        romanos = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        prev = 0
        for c in reversed(romano):
            valor = romanos[c]
            if valor < prev:
                total -= valor
            else:
                total += valor
                prev = valor
        return total

    def texto_a_morse(self, texto):
        """
        Convierte texto a código Morse.
        """
        morse_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
            'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
            'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
            'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
            'Z': '--..',
            '0': '-----', '1': '.----', '2': '..---', '3': '...--',
            '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.'
        }
        texto = texto.upper()
        return ' '.join(morse_dict.get(char, '') for char in texto if char in morse_dict)

    def morse_a_texto(self, morse):
        """
        Convierte código Morse a texto.
        """
        morse_dict = {
            '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
            '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
            '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
            '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
            '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
            '--..': 'Z',
            '-----': '0', '.----': '1', '..---': '2', '...--': '3',
            '....-': '4', '.....': '5', '-....': '6', '--...': '7',
            '---..': '8', '----.': '9'
        }
        palabras = morse.strip().split(' ')
        return ''.join(morse_dict.get(codigo, '') for codigo in palabras)