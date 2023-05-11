def blackjack(cards, dealer_card):
    n = len(cards)
    memo = [[-1] * 22 for _ in range(n + 1)]
    
    # dealer's first card
    dealer_first_card = int(dealer_card) if dealer_card.isdigit() else 10
    
    # initialize memo table for base cases
    for i in range(n + 1):
        memo[i][0] = 0
    for j in range(1, 22):
        memo[n][j] = 0
    
    # fill the memo table
    for i in range(n - 1, -1, -1):
        for j in range(21, -1, -1):
            if memo[i][j] != -1:
                memo[i][j] = max(memo[i][j], memo[i+1][j])
                if j + cards[i] <= 21:
                    memo[i][j] = max(memo[i][j], cards[i] + memo[i+1][j+cards[i]])
    
    # calculate the score based on the memo table
    score = memo[0][0]
    for j in range(1, 22):
        if memo[0][j] != 0:
            break
        score = max(score, memo[0][j])
        
    return score

def main():
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    face_cards = ['J', 'Q', 'K', 'A']
    for i in range(len(face_cards)):
        cards[i+9] = face_cards[i]
    
    dealer_card = input('Enter dealer\'s face-up card: ')
    max_score = -1
    for card1 in cards:
        new_cards = list(cards)
        new_cards.remove(card1)
        for card2 in new_cards:
            player_cards = [card1, card2]
            score = blackjack(player_cards, dealer_card)
            if score > max_score:
                max_score = score
    print('Maximum score:', max_score)

if __name__ == '__main__':
    main()

