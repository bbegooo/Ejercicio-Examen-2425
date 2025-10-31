from typing import NamedTuple
import datetime
import csv


#NamedTuple obligatoria por el ejercicio

Piloto = NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP = NamedTuple("CarreraFP",[
        ("fecha_hora",datetime), 
        ("circuito",str),                    
        ("pais",str), 
        ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
        ("tiempo",float), 
        ("podio", list[Piloto])])

#Primer ejercicio

def lee_carreras(mundial_motofp: str) -> list[CarreraFP]:
    carreras: list[CarreraFP] = []
    with open (mundial_motofp, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        for line in lector:
            line = line.strip()
            if line:
                parts = line.split(";")
                fecha_hora = datetime.datetime.strptime(parts[0], "%Y-%m-%d %H:%M")
                circuito = parts[1]
                pais = parts[2]
                seco = parts[3].lower() == "true"
                tiempo = float(parts[4])
                podio_parts = parts[5].split(",")
                podio: list[Piloto] = []
                for piloto_str in podio_parts:
                    nombre, escuderia = piloto_str.split("-")
                    podio.append(Piloto(nombre.strip(), escuderia.strip()))
                carrera = CarreraFP(fecha_hora, circuito, pais, seco, tiempo, podio)
                carreras.append(carrera)
    return carreras

#Segundo ejercicio

def maximo_dias_sin_ganar(carreras: list[CarreraFP], nombre_piloto: str) -> int:
    fechas_ganadas: list[datetime.datetime] = []
    for carrera in carreras:
        if carrera.podio and carrera.podio[0].nombre == nombre_piloto:
            fechas_ganadas.append(carrera.fecha_hora)
    if not fechas_ganadas:
        return None
    fechas_ganadas.sort()
    max_dias = 0
    for i in range(1, len(fechas_ganadas)):
        delta = (fechas_ganadas[i] - fechas_ganadas[i-1]).days
        if delta > max_dias:
            max_dias = delta
    return max_dias

#Tercer ejercicio

def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    circuito_piloto_podios: dict[str, dict[str, int]] = {}
    for carrera in carreras:
        circuito = carrera.circuito
        if circuito not in circuito_piloto_podios:
            circuito_piloto_podios[circuito] = {}
        for piloto in carrera.podio:
            if piloto.nombre not in circuito_piloto_podios[circuito]:
                circuito_piloto_podios[circuito][piloto.nombre] = 0
            circuito_piloto_podios[circuito][piloto.nombre] += 1
    resultado: dict[str, str] = {}
    for circuito, piloto_podios in circuito_piloto_podios.items():
        max_podios = 0
        piloto_max = ""
        for piloto, podios in piloto_podios.items():
            if podios > max_podios:
                max_podios = podios
                piloto_max = piloto
        resultado[circuito] = piloto_max
    return resultado


def escuderias_con_solo_un_piloto(carreras: list[CarreraFP]) -> list[str]:
    escuderia_pilotos: dict[str, set[str]] = {}
    for carrera in carreras:
        for piloto in carrera.podio:
            if piloto.escuderia not in escuderia_pilotos:
                escuderia_pilotos[piloto.escuderia] = set()
            escuderia_pilotos[piloto.escuderia].add(piloto.nombre)
    resultado: list[str] = []
    for escuderia, pilotos in escuderia_pilotos.items():
        if len(pilotos) == 1:
            resultado.append(escuderia)
    return resultado


def piloto_racha_mas_larga_victorias_consecutivas(carreras: list[CarreraFP], año: int|None = None) -> tuple[str, int]:
    max_racha = 0
    piloto_max = ""
    rachas: dict[str, int] = {}
    for carrera in carreras:
        if año is not None and carrera.fecha_hora.year != año:
            continue
        ganador = carrera.podio[0].nombre if carrera.podio else None
        for piloto in rachas.keys():
            if piloto == ganador:
                rachas[piloto] += 1
            else:
                rachas[piloto] = 0
        if ganador and ganador not in rachas:
            rachas[ganador] = 1
        if ganador and rachas[ganador] > max_racha:
            max_racha = rachas[ganador]
            piloto_max = ganador
    return (piloto_max, max_racha)

def ultimos_ganadores_por_circuito(carreras:list[CarreraFP], n: int, estado: str) -> dict[str, list[str]]:
    circuito_ganadores: dict[str, list[str]] = {}
    for carrera in sorted(carreras, key=lambda c: c.fecha_hora, reverse=True):
        if (estado == "seco" and not carrera.seco) or (estado == "mojado" and carrera.seco):
            continue
        circuito = carrera.circuito
        ganador = carrera.podio[0].nombre if carrera.podio else None
        if ganador:
            if circuito not in circuito_ganadores:
                circuito_ganadores[circuito] = []
            if len(circuito_ganadores[circuito]) < n:
                circuito_ganadores[circuito].append(ganador)
    return circuito_ganadores