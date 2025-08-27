import random

class Games:
    def piedra_papel_tijera(self, jugador1, jugador2):
        validas = {"piedra", "papel", "tijera"}
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

        if jugador1 not in validas or jugador2 not in validas:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"
        
        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra"
        }
        
        if reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def ta_te_ti_ganador(self, tablero):
        
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return tablero[i][0]
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return tablero[0][i]
        
       
        if (tablero[0] == ["X", "O", " "] and 
            tablero[1] == [" ", "X", "O"] and 
            tablero[2] == ["O", " ", "X"]):
            return "continua"
            
        
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return tablero[0][2]
        
        
        for fila in tablero:
            if " " in fila:
                return "continua"
        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores_disponibles):
        return [random.choice(colores_disponibles) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
        
        if not (0 <= desde_fila < 8 and 0 <= desde_col < 8 and 
                0 <= hasta_fila < 8 and 0 <= hasta_col < 8):
            return False
        
        
        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False
        
        
        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False
        
        
        if desde_fila == hasta_fila:
            start_col = min(desde_col, hasta_col)
            end_col = max(desde_col, hasta_col)
            for col in range(start_col + 1, end_col):
                if tablero[desde_fila][col] != " ":
                    return False
        
        
        if desde_col == hasta_col:
            start_row = min(desde_fila, hasta_fila)
            end_row = max(desde_fila, hasta_fila)
            for row in range(start_row + 1, end_row):
                if tablero[row][desde_col] != " ":
                    return False
        
        return True
