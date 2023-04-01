'''
Created on 2 dic. 2020

@author: belen
'''
#-*- coding: utf-8 -*8

from nba2013 import *

###################################################################################

players = read_players('./data/nba2013.csv')

###################################################################################
'1'
###################################################################################

def test_read_players():
    print('Reading', len(read_players('./data/nba2013.csv')), 'registers.')
    print('First three:', read_players('./data/nba2013.csv')[:3])
    print('Last three:', read_players('./data/nba2013.csv')[-3:])

#test_read_players()

###################################################################################
'2'
###################################################################################

def test_filter_by_position():
    guard = filter_by_position(players, 'Guard')
    forward = filter_by_position(players, 'Forward')
    print('Reading', len(guard), 'registers.')
    print('First three:', guard[:3])
    print('Last three:', guard[-3:])
    print('Reading', len(forward), 'registers.')
    print('First three:', forward[:3])
    print('Last three:', forward[-3:])

#test_filter_by_position()


def test_calculate_names():
    names = calculate_names(players)
    print('There were', len(names), 'players in the 2013 NBA season:')
    print('First three registers:', names[:3])
    print('Last three registers:', names[-3:])

#test_calculate_names()


def test_players_by_age():
    parameter1 = players_by_age(players, 35)
    parameter2 = players_by_age(players, 28)
    print('Reading', len(parameter1), 'registers.')
    print('First three:', parameter1[:3])
    print('Last three:', parameter1[-3:])
    print('Reading', len(parameter2), 'registers.')
    print('First three:', parameter2[:3])
    print('Last three:', parameter2[-3:])

#test_players_by_age()

###################################################################################
'3'
###################################################################################

def test_mean_height_by_age():
    mean1 = mean_height_by_age(players, 34)
    mean2 = mean_height_by_age(players)
    print('Mean height of 34-year-old players:', mean1)
    print('Mean height of 23-year-old players:', mean2)
    
#test_mean_height_by_age()

def test_mean_weight_by_range_age():
    mean1 = mean_weight_by_range_age(players)
    mean2 = mean_weight_by_range_age(players, 23, 33)
    print('Mean weight of players between the ages of 18 and 40:', mean1, 'pounds')
    print('Mean weight of players between the ages of 23 and 33:', mean2, 'pounds')

#test_mean_weight_by_range_age()

def test_sum_of_heights_by_position():
    guard = sum_of_heights_by_position(players, 'Guard')
    center = sum_of_heights_by_position(players, 'Center')
    forward = sum_of_heights_by_position(players, 'Forward')
    print("Sum of guards' heights:")
    print(guard)
    print("Sum of centers' heights:")
    print(center)
    print("Sum of forwards' heights:")
    print(forward)
    
#test_sum_of_heights_by_position()

###################################################################################
'4'
###################################################################################

def test_heaviest_by_position():
    guard = heaviest_by_position(players, 'Guard')
    center = heaviest_by_position(players, 'Center')
    forward = heaviest_by_position(players, 'Forward')
    print('Heaviest guard:')
    print(guard)
    print('Heaviest center:')
    print(center)
    print('Heaviest forward:')
    print(forward)
    
#test_heaviest_by_position()

###################################################################################
'5'
###################################################################################

def test_tallest_by_position():
    guards = tallest_by_position(players, 'Guard')
    centers = tallest_by_position(players, 'Center')
    forwards = tallest_by_position(players, 'Forward')
    print('Tallest guards:')
    print(guards)
    print('Tallest centers:')
    print(centers)
    print('Tallest forwards:')
    print(forwards)

#test_tallest_by_position()

###################################################################################
'6'
###################################################################################

def test_dict_by_age():
    print("Dictionary by players' ages:")
    print(dict_by_age(players))

#test_dict_by_age() #IT ONLY SHOWS 10 BECAUSE IT WON'T LOAD OTHERWISE

def test_count_positions():
    print('Number of players by position:')
    print(count_positions(players))

#test_count_positions()

def test_count_ages():
    print('Number of players by age:')
    print(count_ages(players))

#test_count_ages()

def test_tallest_by_age():
    print('Dictionary with the tallest players by age')
    print(tallest_by_age(players))

#test_tallest_by_age()

###################################################################################
'7'
###################################################################################

def test_pie_positions():
    print(pie_positions(players))

#test_pie_positions()

def test_pie_ages():
    print(pie_ages(players, [24, 25, 26]))
    print(pie_ages(players, [26, 27, 28]))

#test_pie_ages()

def test_bar_position():
    print(bar_positions(players))

#test_bar_position()

def test_bar_ages():
    print(bar_ages(players))

#test_bar_ages()

###################################################################################