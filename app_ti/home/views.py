from django.shortcuts import render
from django.http import HttpResponse

import requests

# Create your views here.


seasons = [
    {
        'number':'1',
        'year':'2008',
        'serie':'Breaking Bad',
            },
    {
        'number':'2',
        'year':'2009',
        'serie':'Breaking Bad',
            },
    {
        'number':'3',
        'year':'2010',
        'serie':'Breaking Bad',
            },
    {
        'number':'4',
        'year':'2011',
        'serie':'Breaking Bad',
            },
    {
        'number':'5',
        'year':'2012 - 2013',
        'serie':'Breaking Bad',
            },
    {
        'number':'1',
        'year':'2015',
        'serie':'Better Call Saul',
            },
    {
        'number':'2',
        'year':'2016',
        'serie':'Better Call Saul',
            },
    {
        'number':'3',
        'year':'2017',  
        'serie':'Better Call Saul',
            },
    {
        'number':'4',
        'year':'2018',        
        'serie':'Better Call Saul',
            },
    {
        'number':'5',
        'year':'2020',
        'serie':'Better Call Saul',
            },
]


#response = requests.get('http://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()

def home(request):
    
    context = {
        'seasons': seasons,
        'title': 'Breaking App - Home'
    }
    return render(request, 'home.html', context)


def season(request, serie, number):
    episodes = requests.get('http://tarea-1-breaking-bad.herokuapp.com/api/episodes').json()

    e_list = []

    for e in episodes:
        if int(e['season']) == number and e['series'] == serie:
            e_list.append(e)

    context = {
        'serie': serie,
        'number': number,
        'e_list': e_list,
        'title': 'Breaking App - Season'
    }
    
    return render(request, 'season.html', context)

def episode(request, episode_id):
    episode = requests.get('http://tarea-1-breaking-bad.herokuapp.com/api/episodes/'+str(episode_id)).json()

    e_info = episode[0]

    print(e_info)

    context = {
        'e_info': e_info,
         'title': 'Breaking App - Episode'
    }
    
    return render(request, 'episode.html', context)


def character(request, char_name):
    li=char_name.split()

    character_raw = requests.get('http://tarea-1-breaking-bad.herokuapp.com/api/characters?name='+'+'.join(li)).json()
    quotes = requests.get('http://tarea-1-breaking-bad.herokuapp.com/api/quote?author='+'+'.join(li)).json()

    character = character_raw[0]
    
    print(quotes)

    context = {
        'character': character,
        'quotes': quotes,
         'title': 'Breaking App - Character'
    }
    
    return render(request, 'character.html', context)



def search_result(request, char_name):
   

    context = {
         'title': 'Breaking App - Search Result'
    }
    
    return render(request, 'search_result.html', context)