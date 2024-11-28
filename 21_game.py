import random

Card_deck = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]  * 4

wins = 0
loses = 0

def deal(deck_func):
    hands = []
    random.shuffle(deck_func)
    for card in range(2):
        card = deck_func.pop
        if card == 11:
            card = 'A'
        if card == 10:
            card = 'J'
        if card == 10:
            card = 'Q'
        if card == 10:
            card = 'K'
        hands.append(card)
    return hands

def play_more():
    again = input('Нужно добрать карту? (Y/N) : ')
    if again == 'Y':
        game()
    else:
        print('Тут должна была быть ваша реклама, но вы отказались')
        exit()

def sum_score(hand):
    score = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            score += 10
        elif card == 'A':
            if score == >= 11:
                score += 1
            else:
                score += 11
        else:
            score += card
    return score


