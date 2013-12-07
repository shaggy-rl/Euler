from collections import Counter

hands = (line.split() for line in open("./poker.txt"))
index_of_values = {index:value
        for value,index in enumerate('23456789TJQKA')}

def compare(hand):
    cmp = zip(*sorted(((card_kind, index_of_values[count]) for
        count,card_kind in Counter(card[0] for card in hand).items()), reverse=True))
    if len(cmp[0]) == 5:
        flush = len({suite[1] for suite in hand}) == 1
        straight = cmp[1] == tuple(range(cmp[1][0], cmp[1][-1]-1, -1))
        cmp[0] = ((1, (3,2,1)),((3,2,0),5))[straight][flush]

    return cmp

print sum(compare(hand[:5]) > compare(hand[5:]) for hand in hands)
