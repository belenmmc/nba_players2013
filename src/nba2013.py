'''
Created on 2 dic. 2020

@author: belen
'''
#-*- coding: utf-8 -*8
import csv
from matplotlib import pyplot as plt
from collections import namedtuple, Counter

###################################################################################

Player = namedtuple('Player', 'name, position, height, weight, age')

###################################################################################
'1'
###################################################################################

def read_players(file):
    with open(file, 'rt', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        players = [Player(name, position, int(height), int(weight), int(age))
                   for name, position, height, weight, age in reader]
    return players

###################################################################################
'2'
###################################################################################

def filter_by_position(players, position):
    return [player for player in players if player.position == position]


def calculate_names(players):
    names = [(player.name) for player in players]
    return names


def players_by_age(players, age):
    res = [(player.name, player.position, player.height)
           for player in players if age == player.age]
    return res

###################################################################################
'3'
###################################################################################

def mean_height_by_age(players, age = 23):
    heights = [player.height for player in players if age == player.age]
    return sum(heights)/len(heights)

def mean_weight_by_range_age(players, start = 18, end = 40):
    weights = [player.weight for player in players if start <= player.age <= end]
    return sum(weights)/len(weights)

def sum_of_heights_by_position(players, position):
    heights = [player.height for player in players if position == player.position]
    return sum(heights)

###################################################################################
'4'
###################################################################################

def heaviest_by_position(players, position):
    res = [player for player in players if player.position == position]
    res_max = max(res, key = lambda x:x[-2])
    return res_max

###################################################################################
'5'
###################################################################################

def tallest_by_position(players, position, n = 10):
    res = [player for player in players if position == player.position]
    res.sort(key = lambda x:x[2], reverse = True)
    return res[:n]

###################################################################################
'6'
###################################################################################

def dict_by_age(players):
    ages = [player.age for player in players]
    res = {}
    for age in ages:
        res[age] =  [player for player in players if age == player.age][:10]
    return res

def count_positions(players):
    positions = [player.position for player in players]
    res = Counter(positions)
    return res

def count_ages(players):
    ages = [player.age for player in players]
    res = Counter(ages)
    return res

def tallest_by_age(players):
    ages = [player.age for player in players]
    res = {}
    for age in ages:
        res[age] = max((player for player in players if age == player.age), key = lambda x:x[2])
    return res

###################################################################################
'7'
###################################################################################

def pie_positions(players):
    freq = count_positions(players)
    positions = {player.position for player in players}
    sizes = [freq.get(e, 0) for e in positions]
    plt.pie(sizes, labels = positions, autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend()
    plt.show()

def pie_ages(players, ages):
    freq = count_ages(players)
    sizes = [freq.get(e, 0) for e in ages]
    plt.pie(sizes, labels = ages, autopct = '%1.1f%%', shadow = True, startangle = 90)
    plt.legend()
    plt.show()

def bar_positions(players):
    freq = count_positions(players)
    positions = sorted(freq, key = freq.get, reverse = True)
    frequencies = [freq[position] for position in positions]
    plt.bar(positions, frequencies)
    plt.xticks(rotation=80)
    plt.title('Frequency of players by position')
    plt.show()

def bar_ages(players):
    freq = count_ages(players)
    ages = sorted(freq, key = freq.get, reverse = True)
    frequencies = [freq[age] for age in ages]
    plt.bar(ages, frequencies)
    plt.xticks(rotation=80)
    plt.title('Frequency of players by age')
    plt.show()

###################################################################################