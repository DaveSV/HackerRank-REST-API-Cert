#!/bin/python3

import math
import os
import random
import re
import sys

import requests

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#

def getTotalGoals(team, year):
    # Variables para almacenar el total de goles
    total_goals = 0

    # Variables para controlar la paginación
    page = 1
    total_pages = 1

    # Realizar solicitudes GET para obtener los partidos donde el equipo fue el equipo local (team1)
    while page <= total_pages:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={page}"
        response = requests.get(url).json()
        
        # Actualizar el número total de páginas
        total_pages = response['total_pages']
        
        # Analizar los datos de los partidos
        matches = response['data']
        for match in matches:
            total_goals += int(match['team1goals'])
        
        # Pasar a la siguiente página
        page += 1

    # Restablecer las variables para controlar la paginación
    page = 1
    total_pages = 1

    # Realizar solicitudes GET para obtener los partidos donde el equipo fue el equipo visitante (team2)
    while page <= total_pages:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={page}"
        response = requests.get(url).json()
        
        # Actualizar el número total de páginas
        total_pages = response['total_pages']
        
        # Analizar los datos de los partidos
        matches = response['data']
        for match in matches:
            total_goals += int(match['team2goals'])
        
        # Pasar a la siguiente página
        page += 1

    return total_goals

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    team = input()

    year = int(input().strip())

    result = getTotalGoals(team, year)

    fptr.write(str(result) + '\n')

    fptr.close()
