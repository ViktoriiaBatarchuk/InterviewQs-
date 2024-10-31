'''
Number: 151
Task: We have a standard (52 card) deck of cards, with equal share of the cards associated with each of the four
"suits" (e.g. clubs, spades, diamons, and hearts).
Question: If you draw 3 cards from the deck, one a time, what is the probability that you draw
a club, a heart and a diamond in any order?
'''

import math

#In math module there is function math.comb, that calculate number of combinations,
# also known as "binomial coefficients.". Formula: math.comb(n,k) = n!/k!*(n-k)!

#Total number of ways to draw 3 cards out of 52 cards
total_ways_draw_card = math.comb(52,3)

#Number of ways to draw 1 club, 1 heart, and 1 diamond
ways_to_choose_club = 13        #13 clubs in the deck
ways_to_choose_heart = 13       #13 hearts to the deck
ways_to_choose_diamond = 13       #13 hearts to the deck

#Total favourable outcomes
favorable_ways = ways_to_choose_club*ways_to_choose_heart*ways_to_choose_diamond

#The probability to
probability = (favorable_ways/total_ways_draw_card)*100

print(round(probability,2),"%")