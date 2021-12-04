import sys
from collections import Counter
from collections import defaultdict

fn = "input.txt"


def check(c, marks):        # Check card for 5 in-a-row (ho
    if not marks:
        return None

    (_, ch1), = Counter(x // 5 for x in marks).most_common(1)   # Check for vertical 5 in-a-row
    (_, ch2), = Counter(x % 5  for x in marks).most_common(1)   # Check for horizontal 5 in-a-row

    if ch1 == 5 or ch2 == 5:        # 5 in-a-row found
        return sum([card for i, card in enumerate(c) if i not in marks])   # Sum unmarked numbers

    return None                     # No 5 in-a-row found


if __name__ == '__main__':

    with open(fn, "r") as data:
        numbers = [int(board) for board in data.readline().strip().split(',')]
        rest = data.read().split("\n\n")
        cards = [[int(board) for board in r.strip().split()] for r in rest]

    marks_per_card = defaultdict(list)
    finished = set()
    scores = []
    for n in numbers:                       # Next number called
        for i, card in enumerate(cards):    # Check cards for called number
            if i in finished:               # Skip previously finished board
                continue
            if n in card:                  # Found number on this board
                marks_per_card[i].append(card.index(n))   # Mark the number
            score = check(card, marks_per_card[i])        # Check if horizontal or vertical 5-in-a-row
            if score:                       # BINGO! found on this card
                scores.append(score * n)    # Score and save
                finished.add(i)             # Add card to finished card list

    print(f'{scores[0]=}, {scores[-1]=}')   # First and Last scores
