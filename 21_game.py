import random
from random import choice

Card_deck = [1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11]  * 4

wins = 0
loses = 0

def deal(deck_func):                            #Выдача начальных карт и определение мастей
    hands = []
    random.shuffle(deck_func)
    for i in range(2):
        card = deck_func.pop()
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

def play_again():                                #Продолжение игры
    Card_deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] * 4
    print('---------------------------------------------------------------------------------------')
    again = input('Начать новую игру? (Y/N) : ')
    print('---------------------------------------------------------------------------------------')
    if again == 'Y':
        game()
    else:
        print('---------------------------------------------------------------------------------------')
        print('Тут должна была быть ваша реклама, но вы отказались')
        print('---------------------------------------------------------------------------------------')
        exit()

def total(hand):                            #Считаю кол-во очков
    cards = 0
    for card in hand:
        if card == 'J' or card == 'Q' or card == 'K':
            cards += 10
        elif card == 'A':
            if cards >= 11:
                cards += 1
            else:
                cards += 11
        else:
            cards += card
    return cards


def hit(hand):                           #Добавляю карты
    card = Card_deck.pop()
    if card == 11:
        card = 'A'
    if card == 10:
        card = 'J'
    if card == 10:
        card = 'Q'
    if card == 10:
        card = 'K'
    hand.append(card)
    return hand


def score(dealer_hand, player_hand):           #Начинаю считать очки в конце раунда и сравнивать у кого больше
    global wins
    global loses
    print('Результаты раунда')
    print('---------------------------------------------------------------------------------------')
    print('У диллера на руке: ' + str(dealer_hand) + ', сумма очков равна: ' + str(total(dealer_hand)))
    print('У Вас на руке: ' + str(player_hand) + 'сумма очков равна: ' + str(total(player_hand)))
    print('---------------------------------------------------------------------------------------')
    if total(player_hand) == 21:
        #print_result(dealer_hand, player_hand)
        print('---------------------------------------------------------------------------------------')
        print('You have 21, you win')
        print('---------------------------------------------------------------------------------------')
        wins += 1
    elif total(dealer_hand) == 21:
        #print_result(dealer_hand, player_hand)
        print('---------------------------------------------------------------------------------------')
        print('Sorry, but you lose, try again')
        print('---------------------------------------------------------------------------------------')
        loses += 1
    elif total(player_hand) < total(dealer_hand):
        #print_result(dealer_hand, player_hand)
        print('---------------------------------------------------------------------------------------')
        print('У вас меньше очков чем у диллера, так что вы проиграли')
        print('---------------------------------------------------------------------------------------')
        loses += 1
    elif total(player_hand) > total(dealer_hand):
        #print_result(dealer_hand, player_hand)
        print('---------------------------------------------------------------------------------------')
        print('У вас хоть и недобор, но очков у вас больше, поздравляю')
        print('---------------------------------------------------------------------------------------')
        wins += 1
    elif total(player_hand) == total(dealer_hand):
        #print_result(dealer_hand, player_hand)
        print('---------------------------------------------------------------------------------------')
        print('У вас поровну, играйте снова')
        print('---------------------------------------------------------------------------------------')

def game():                                 #Финалочка
    global wins
    global loses
    print('---------------------------------------------------------------------------------------')
    print('Начало игры')
    print('---------------------------------------------------------------------------------------')
    dealer_hand = deal(Card_deck)
    player_hand = deal(Card_deck)
    print('---------------------------------------------------------------------------------------')
    print('У раздающего: ' + str(dealer_hand) + 'сумма очков диллера равна ' + str(total(dealer_hand)))
    print('---------------------------------------------------------------------------------------')
    print('---------------------------------------------------------------------------------------')
    print('У вас на руках: ' + str(player_hand) + ' ваша сумма очков составляет ' + str(total(player_hand)))
    print('---------------------------------------------------------------------------------------')

    cont_game = True
    while cont_game:
        choice = input()
        if choice == 'Y':
            hit(player_hand)
            print('---------------------------------------------------------------------------------------')
            print(player_hand)
            print('Сумма очков: ' + str(total(player_hand)))
            print('---------------------------------------------------------------------------------------')
            if total(player_hand) > 21:
                print('---------------------------------------------------------------------------------------')
                print('Перебор!!!')
                print('---------------------------------------------------------------------------------------')
                loses += 1
                play_again()
        elif choice == 'N':
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print('---------------------------------------------------------------------------------------')
                print('Диллер берёт ещё карту')
                print('---------------------------------------------------------------------------------------')
                if total(dealer_hand) > 21:
                    print('---------------------------------------------------------------------------------------')
                    print('У диллера перебор, ' + str(total(dealer_hand)) + ' вы победили! ')
                    print('---------------------------------------------------------------------------------------')
                    wins += 1
                    play_again()
            score(dealer_hand, player_hand)
            play_again()
            cont_game = False

game()