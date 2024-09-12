VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    score = 0

    if len(hand) > 5:
        return "Your hand is over 5 cards!"

    for card in hand:
        if card not in VALID_CARDS:
            return "Invalid card!" 
        elif 'Ace' in hand:
            if not isinstance(card, str):
                score += card
            elif isinstance(card, str) and card != "Ace":
                score += 10
            else:
                if score >= 11:
                    score += 1
                elif score <= 10:
                    score += 11
        else:
            if not isinstance(card, str):
                score += card
            else:
                score += 10

        if score > 21:
            return "Bust!"
    
    return score