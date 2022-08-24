import requests

def get_data():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    response = requests.get(url)
    superhero = response.json()
    return superhero

def search_hero(hero_list):
    hulk = {}
    captain_america = {}
    thanos = {}
    for hero in hero_list:
        if hero['name'] == 'Hulk':
            hulk = hero
        elif hero['name'] == 'Captain America':
            captain_america = hero
        elif hero['name'] == 'Thanos':
            thanos = hero
    list_hero = (hulk, captain_america, thanos)
    return list_hero

def search_intelligence_hero(heroes):
    if heroes[0]['powerstats']['intelligence'] > heroes[1]['powerstats']['intelligence']:
        if heroes[0]['powerstats']['intelligence'] > heroes[2]['powerstats']['intelligence']:
            print(f'Самый умный {heroes[0]["name"]}')
        else:
            print(f'Самый умный {heroes[2]["name"]}')
    else:
        if heroes[1]['powerstats']['intelligence'] > heroes[2]['powerstats']['intelligence']:
            print(f'Самый умный {heroes[1]["name"]}')
        else:
            print(f'Самый умный {heroes[2]["name"]}')

if __name__ == '__main__':
    search_intelligence_hero(search_hero(get_data()))


