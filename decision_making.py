def algo(d):
    if (d.card1.v == d.card2.v):
        if (d.card1.v == '9' or d.card1.v == 'T' or d.card1.v =='J' or d.card1.v =='Q' or  d.card1.v =='K' or d.card1.v =='A'):
            return (2, 0)
    if (d.card1.v == 'A' and (d.card2.v == 'T' or d.card2.v == 'J' or d.card2.v == 'Q' or d.card2.v =='K' or d.card2.v == 'A')):
        return (1, 0)
    if (d.card2.v == 'A' and (d.card1.v == 'T' or d.card1.v == 'J' or d.card1.v == 'Q' or d.card1.v =='K' or d.card1.v == 'A')):
        return (1, 0)
    return (0, 3)
        