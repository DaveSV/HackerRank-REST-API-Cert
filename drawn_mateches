import requests
import os

def getNumDraws(year):
    num_draws = 0
    page = 1
    total_pages = 1

    while page <= total_pages:
        url = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&page={page}"
        response = requests.get(url).json()
        total_pages = response['total_pages']
        matches = response['data']
        for match in matches:
            team1_goals = int(match['team1goals'])
            team2_goals = int(match['team2goals'])
            if team1_goals == team2_goals:
                num_draws += 1
        page += 1

    return num_draws


if __name__ == '__main__':
    year = int(input().strip())
    result = getNumDraws(year)
    print(result)
