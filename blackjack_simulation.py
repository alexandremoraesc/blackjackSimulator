#Simulação de BlackJack para Python
from random import randint 
#import numpy as np 

NUMB_OF_DECKS = 6
TOTAL_BET = 100

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * NUMB_OF_DECKS

class Dealer:
    global cards
    def __init__(self, first_card):
        self.cards = [first_card]
        self.sum = first_card

    def dealcard(self, n):
        qnt = 0 

        while qnt < n:
            a = randint(0, len(cards)-1)
            self.cards.append(cards[a])
            self.sum += cards[a]
            qnt += 1
            cards.pop(a)

class Player:
    global cards
    def __init__(self, player_sum, bet):
        self.cards = [player_sum]
        self.sum = player_sum
        self.bet = bet 
        self.retorno = 0
        self.nmbcards = len(self.cards)

    def playerDecision(self, playerSum, dealerSum):
        #decision = input("A casa tem " + str(dealerSum) + " pontos. Você tem " + str(playerSum) + " pontos. O que deseja fazer? Hit(1), Stand(0), Double(2), Split(-1)")
        #print(playerSum, dealerSum)

        if playerSum <=15 and playerSum != 13:
            return 1

        if playerSum == 13:
            return 2

        else:
            return 0
        
        #return int(decision)

    def dealcard(self, n):
        qnt = 0 

        while qnt < n:
            a = randint(0, len(cards)-1)
            self.cards.append(cards[a])
            self.sum += cards[a]
            qnt += 1
            cards.pop(a)

def game(first_dealer_card, player_sum):
    dealer = Dealer(first_dealer_card)
    player = Player(player_sum, 2)
    global cards, TOTAL_BET
    playerWins = False

    dealer.dealcard(1)
    #player.dealcard(2)

    while player.sum <= 21:
        
        if player.sum == 21 and player.nmbcards == 2:
            #print("O jogador fez um blackjack!")
            p = player.sum    
            player.retorno = 1.5*2*player.bet
            #print(player.retorno)   
            TOTAL_BET += player.retorno 
            #print(TOTAL_BET)
            break

        if player.sum == 21:
            #print("O jogador fez 21 pontos!")
            p = player.sum
            player.retorno = 2*player.bet
            #print(player.retorno)
            TOTAL_BET += player.retorno
            #print(TOTAL_BET)
            break

        decision = player.playerDecision(player.sum, dealer.cards[0])

        if decision == 1:
            player.dealcard(1)
            p =  player.sum

        elif decision == 0: 
            p = player.sum
            break

        elif decision == -1:
            pass

        elif decision == 2:
            player.dealcard(1)
            p = player.sum
            player.bet = 2*player.bet
            break 

        else:
            #print("Escolha inválida.")
            decision = player.playerDecision(player.sum, dealer.cards[0])

    if player.sum > 21:
        #print("O jogador estorou com " + str(player.sum) + " pontos. A casa venceu!")
        playerWins = False   
        player.retorno = -player.bet 
        TOTAL_BET += player.retorno
        #print(player.retorno, TOTAL_BET)
        return playerWins

    while dealer.sum < 17:
        dealer.dealcard(1)
        d = dealer.sum
    
    d = dealer.sum
    
    if dealer.sum > 21:
        #print("Dealer estorou com " + str(dealer.sum) + " pontos. O jogador venceu!")
        playerWins = True 
        player.retorno = 2*player.bet
        TOTAL_BET += player.retorno
        #print(player.retorno, TOTAL_BET)
        return playerWins

    if p == d:
        playerWins = False
        #print("O jogo resultou em empate! A casa fez " + str(d) + " pontos e o jogador fez " + str(p) + " pontos.")
        return playerWins


    resultado = comparar(d,p)

    if resultado:
        player.retorno = 2*player.bet
        TOTAL_BET += player.retorno
        #print(player.retorno, TOTAL_BET)
    else:
        player.retorno = -player.bet
        TOTAL_BET += player.retorno
        #print(player.retorno, TOTAL_BET)

    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 * NUMB_OF_DECKS

    return resultado

def comparar(d, p):
    if p > d:
        #print("O jogador ganhou com " + str(p) + " pontos. A casa fez " + str(d) + " pontos.")
        return True
    
    else:
        #print("A casa ganhou com " + str(d) + " pontos. O jogador fez " + str(p) + " pontos.")
        return False

def main():
    global TOTAL_BET
    for dc in range(2,12):
        for ps in range(4,21):
            contador_p = 0
            contador_d = 0
            for i in range(100):
                a = game(dc, ps)
                if a:
                    contador_p += 1
                else:
                    contador_d += 1
            print(dc, ps, contador_p, contador_d, float(contador_p/(contador_d + contador_p)), TOTAL_BET)
            persistencia(dc, ps, contador_p, contador_d, float(contador_p/(contador_d + contador_p)), TOTAL_BET)
        #arr1 = np.array([contador_d, contador_p])
        #arr2 = np.array([FIRST_DEALER_CARD, PLAYER_SUM, TOTAL_BET])
        #analise(arr1, arr2)
            TOTAL_BET = 100

def persistencia(*args):
    with open("blackjackresults.txt", 'a') as writer:
        for arg in args:
            if arg == args[-1]:
                writer.write(str(arg) + "\n")
            else:
                writer.write(str(arg) + ",")


if __name__ == "__main__":
    main()