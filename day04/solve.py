path = '.'

total = 0
cards = [1]
i = 1
with open(f'{path}/puzzle') as fp:
    for line in fp.readlines():
        wins, plays = line.strip().split(': ')[1].split(' | ')
        win = { w: 0 for w in filter(lambda a: a.isdigit(), wins.split(' ')) }
        play_sum = 0
        matches = 0

        if i > len(cards):
            cards.append(1)

        for play in plays.split(' '):
            if play in win.keys():
                play_sum = max(play_sum*2, 1)
                matches += 1
        total += play_sum
        for j in range(i, i+matches):
            try:
                cards[j] += cards[i-1]
            except IndexError:
                cards.append(1+cards[i-1])

        i += 1


print(total)
print(sum(cards))