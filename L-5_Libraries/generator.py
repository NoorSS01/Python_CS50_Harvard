import random
coin=random.choice(["Heads", "Tails"])
print(coin)

cards=["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)
