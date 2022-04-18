#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import networkx as nx
import numpy as np

G = nx.DiGraph(
            {1: [2,3,4,9,5],
            2: [1, 3, 5, 6, 14],
            3: [1, 2, 4, 6, 7, 8],
            4: [1, 3, 8, 10, 18],
            5: [1, 2, 6, 10, 15, 19],
            6: [2,3,5,7,10,11],
            7: [3,6, 8,11,12,13],
            8: [3,4,7,9,13,14],
            9: [1,4,8,19],
            10: [4,5,6,11,15],
            11: [6,7,10,12,15,16],
            12: [7,11,13,16,17,18],
            13: [7,8,12,14,18,19],
            14: [2,5,8,9,13,19],
            15: [5,10,11,16,17],
            16: [11,12,15,17],
            17: [12,15,16,18,19],
            18: [4,12,13,17,19],
            19: [5, 9, 13, 14, 17, 18]})

G.nodes[1]['spring']= 'heavy rainfall'
G.nodes[2]['spring']= 'short showers'
G.nodes[3]['spring']= 'sleet'
G.nodes[4]['spring']= 'snowy rain'
G.nodes[5]['spring']= 'warm drizzle'
G.nodes[6]['spring']= 'nippy and humid'
G.nodes[7]['spring']= 'clear and nippy'
G.nodes[8]['spring']= 'hail'
G.nodes[9]['spring']= 'windy and snowy'
G.nodes[10]['spring']= 'warm and humid'
G.nodes[11]['spring'] = 'cloudy and warm'
G.nodes[12]['spring']='sunny and clear'
G.nodes[13]['spring']='cold wafts of mist'
G.nodes[14]['spring']='heavy snowfall'
G.nodes[15]['spring']='hot and dry'
G.nodes[16]['spring']='strong pollen drift'
G.nodes[17]['spring']='pleasantly warm'
G.nodes[18]['spring']='cold and dry'
G.nodes[19]['spring']='light snowfall'

G.nodes[1]['summer']= 'torrential rainfall'
G.nodes[2]['summer']= 'downpour'
G.nodes[3]['summer']= 'cloudy and humid'
G.nodes[4]['summer']= 'warm storm'
G.nodes[5]['summer']= 'warm rain'
G.nodes[6]['summer']= 'short warm showers'
G.nodes[7]['summer']= 'pleasantly warm'
G.nodes[8]['summer']= 'cloudy and windy'
G.nodes[9]['summer']= 'fierce wind'
G.nodes[10]['summer']= 'warm drizzle'
G.nodes[11]['summer'] = 'cloudy and warm'
G.nodes[12]['summer']='hot and dry'
G.nodes[13]['summer']='warm breeze'
G.nodes[14]['summer']='partly cloudy and nippy'
G.nodes[15]['summer']='hot and muggy'
G.nodes[16]['summer']='hot and windy'
G.nodes[17]['summer']='dry heat surges'
G.nodes[18]['summer']='sunny and clear'
G.nodes[19]['summer']='clear and nippy'

G.nodes[1]['autumn']= 'unseasonable warmth'
G.nodes[2]['autumn']= 'pleasantly warm'
G.nodes[3]['autumn']= 'sunny and clear'
G.nodes[4]['autumn']= 'sporadic gusts'
G.nodes[5]['autumn']= 'sunny and nippy'
G.nodes[6]['autumn']= 'sunny and cloudy'
G.nodes[7]['autumn']= 'humid and cloudy'
G.nodes[8]['autumn']= 'cold wafts of mist'
G.nodes[9]['autumn']= 'cold winds'
G.nodes[10]['autumn']= 'drizzle'
G.nodes[11]['autumn'] = 'rain and gusts'
G.nodes[12]['autumn']='rain and fog'
G.nodes[13]['autumn']='thick fog soup'
G.nodes[14]['autumn']='frosty and cloudy'
G.nodes[15]['autumn']='rainy windstorm'
G.nodes[16]['autumn']='heavy downpour'
G.nodes[17]['autumn']='short light showers'
G.nodes[18]['autumn']='windy and clear'
G.nodes[19]['autumn']='cloudy and nippy'

G.nodes[1]['winter']= 'sunny and nippy'
G.nodes[2]['winter']= 'cloudy and nippy'
G.nodes[3]['winter']= 'cold fog wafts'
G.nodes[4]['winter']= 'light drizzle'
G.nodes[5]['winter']= 'cold and clear'
G.nodes[6]['winter']= 'clear and windy'
G.nodes[7]['winter']= 'cold and foggy'
G.nodes[8]['winter']= 'cold rain showers'
G.nodes[9]['winter']= 'heavy rain'
G.nodes[10]['winter']= 'hail'
G.nodes[11]['winter'] = 'snowy rain'
G.nodes[12]['winter']='wet snowfall'
G.nodes[13]['winter']='cold and cloudy'
G.nodes[14]['winter']='cold wind'
G.nodes[15]['winter']='blizzard'
G.nodes[16]['winter']='windy and snowy'
G.nodes[17]['winter']='light snowfall'
G.nodes[18]['winter']='sleet'
G.nodes[19]['winter']='icy and cloudy'

season = str(input('What season?'))
global current_point
current_point = np.random.randint(1,19)
howmanydays = int(input('How many days?'))

def move_hex(current_point, season):
            new_point = np.random.choice(list(G.adj[current_point]))
            current_point = new_point
            current_weather = G.nodes[current_point][season]
            print(current_weather)
            return new_point



def weather_forecast(N,current_point):
    n=0
    while n<N:
        current_point = move_hex(current_point, season)
        n = n+1


weather_forecast(howmanydays,current_point)