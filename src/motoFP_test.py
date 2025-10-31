import motoFP

def test_lee_carreras():
    print("Test de lee_carreras")
    carrera_test = motoFP.lee_carreras("data/mundial_motofp.csv")
    print(carrera_test)
    
def test_maximo_dias_sin_ganar():
    print("Test de maximo_dias_sin_ganar")
    carreras = motoFP.lee_carreras("data/mundial_motofp.csv")
    resultado = motoFP.maximo_dias_sin_ganar(carreras, "Marc Marquez")
    print(f"Maximo dias sin ganar para Marc Marquez: {resultado}")

def test_piloto_mas_podios_por_circuito():
    print("Test de piloto_mas_podios_por_circuito")
    carreras = motoFP.lee_carreras("data/mundial_motofp.csv")
    resultado = motoFP.piloto_mas_podios_por_circuito(carreras)
    print("Piloto con mas podios por circuito:")
    for circuito, piloto in resultado.items():
        print(f"{circuito}: {piloto}")

def test_escuderias_con_solo_un_piloto():
    print("Test de escuderias_con_solo_un_piloto")
    carreras = motoFP.lee_carreras("data/mundial_motofp.csv")
    resultado = motoFP.escuderias_con_solo_un_piloto(carreras)
    print("Escuderias con solo un piloto que ha quedado en el podio:")
    for escuderia in resultado:
        print(escuderia)

def piloto_racha_mas_larga_victorias_consecutivas():
    print("Test de piloto_racha_mas_larga_victorias_consecutivas")
    carreras = motoFP.lee_carreras("data/mundial_motofp.csv")
    resultado = motoFP.piloto_racha_mas_larga_victorias_consecutivas(carreras)
    print(f"Piloto con la racha mas larga de victorias consecutivas: {resultado[0]} con {resultado[1]} victorias")


def ultimos_gandores_por_circuito():
    print("Test de ultimos_gandores_por_circuito")
    carreras = motoFP.lee_carreras("data/mundial_motofp.csv")
    resultado = motoFP.ultimos_gandores_por_circuito(carreras)
    print("Ultimos ganadores por circuito:")
    for circuito, piloto in resultado.items():
        print(f"{circuito}: {piloto}")

if __name__ == "__main__":
    test_lee_carreras()
    test_maximo_dias_sin_ganar()
    test_piloto_mas_podios_por_circuito()
    test_escuderias_con_solo_un_piloto()
    piloto_racha_mas_larga_victorias_consecutivas()
    ultimos_gandores_por_circuito()