from collections import defaultdict

def custom_key(card):
    order = "J23456789TQKA" #"AKQJT98765432"
    return [order.index(char) for char in card]

def get_ranks(hands,types):
    ranked = []

    fives = []
    fours = []
    houses = []
    threes = []
    two_pairs = []
    pairs = []
    high_cards = []

    for hand, type in zip(hands,types):
        if type == 7:
            fives.append(hand)
        elif type == 6:
            fours.append(hand)
        elif type == 5:
            houses.append(hand)
        elif type == 4:
            threes.append(hand)
        elif type == 3:
            two_pairs.append(hand)
        elif type == 2:
            pairs.append(hand)
        else:
            high_cards.append(hand)
    
    # print(f"{threes=}")
    # print(f"{sorted(two_pairs)=}")
    ans = []

    if high_cards:
        # print(f"{high_cards=}")
        ans = sorted(high_cards, key=custom_key)
    if pairs:
        # print(f"{pairs=}")
        if ans:
            ans.extend(sorted(pairs, key=custom_key))
        else:
            ans = sorted(pairs, key=custom_key)
    if two_pairs:
        # print(f"{two_pairs=}")
        if ans:
            ans.extend(sorted(two_pairs, key=custom_key))
        else:
            ans = sorted(two_pairs, key=custom_key)
    if threes:
        # print(f"{threes=}")
        if ans:
            ans.extend(sorted(threes, key=custom_key))
        else:
            ans = sorted(threes, key=custom_key)
    if houses:
        if ans:
            ans.extend(sorted(houses, key=custom_key))
        else:
            ans = sorted(houses, key=custom_key)
    if fours:
        if ans:
            ans.extend(sorted(fours, key=custom_key))
        else:
            ans = sorted(fours, key=custom_key)
    if fives:
        if ans:
            ans.extend(sorted(fives, key=custom_key))
        else:
            ans = sorted(fives, key=custom_key)
    
    print(f"{ans=}")

    return ans

def get_type(hand):
    # print(f"{hand=}")
    hand_dict = defaultdict(int)
    type = 1

    for card in hand:
        # print(f"{card=}")
        hand_dict[card] += 1
    
    # print(f"{hand_dict=}") 

    if 5 in hand_dict.values():
        # print(5)
        type = 7
    elif 4 in hand_dict.values():
        # print(4)
        type = 6
    elif 3 in hand_dict.values():
        if 2 in hand_dict.values():
            # print(32)
            type = 5
        else:
            # print(3)
            type = 4
    elif 2 in hand_dict.values():
        count = 0
        for card in hand_dict:
            if hand_dict[card] == 2:
                count += 1
        if count == 2:
            # print(22)
            type = 3
        else:
            # print(2)
            type = 2
    
    # print(f"pre {type=}")

    if "J" in hand:
        if type == 6 or type == 1: # fours or high card
            type += 1
        elif type == 5 or type == 4 or type == 2: #full house, threes or pairs
            type += 2
        elif type == 3: # two pairs
            if hand.count("J") == 2: # two jacks
                type += 3
            else: # one jack
                type += 2

    # print(f"post {type=}")
    return type

with open ("7/input.txt") as f:
    data = f.read().splitlines()

hands = {}
types = []

for d in data:
    hand, bid = d.split()
    hands[hand] = int(bid)

# print(f"{hands=}")

for hand in hands:
    types.append(get_type(hand))

ranks = get_ranks(hands, types)
# print(f"{ranks=}")

winnings = 0

for i, rank in enumerate(ranks):
    # print(f"{i=}, {rank=}, {hands[rank]=}")
    winnings += hands[rank]*(i+1)

print(f"{winnings=}")