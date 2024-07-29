class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

    def __lt__(self, other):
        if self.suit == other.suit:
            return self.rank < other.rank
        return self.suit < other.suit

    def __gt__(self, other):
        if self.suit == other.suit:
            return self.rank > other.rank
        return self.suit > other.suit

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank


def linear_search(cards, target):
    for index, card in enumerate(cards):
        if card == target:
            return index
    return -1


def main():
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

    cards = [Card(suit, rank) for suit in suits for rank in ranks]

    target_card = Card("Hearts", 3)

    index = linear_search(cards, target_card)
    if index != -1:
        print(
            f"Card found at index {index}: {cards[index]}")
    else:
        print("Card not found")


if __name__ == "__main__":
    main()