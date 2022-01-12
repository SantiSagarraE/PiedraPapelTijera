def PPT(jugador, computadora):

    if jugador == computadora:
        resultado = "Empate"
    elif jugador == "PIEDRA" and computadora == "PAPEL":
        resultado = "Computadora"
    elif jugador == "PIEDRA" and computadora == "TIJERA":
        resultado = "Jugador"
    elif jugador == "PAPEL" and computadora == "PIEDRA":
        resultado = "Jugador"
    elif jugador == "PAPEL" and computadora == "TIJERA":
        resultado = "Computadora"
    elif jugador == "TIJERA" and computadora == "PIEDRA":
        resultado = "Computadora"
    elif jugador == "TIJERA" and computadora == "PAPEL":
        resultado = "Jugador"

    return resultado



