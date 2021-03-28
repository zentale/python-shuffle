def shuffle(cards):
    half = int(len(cards) / 2)
    shuffled = []
    for i in range(half):
        shuffled.append(cards[i])
        shuffled.append(cards[i + half])
    return shuffled


def find_original(cards):
    shuffled = shuffle(cards)
    count = 1
    print(f"{count}. shuffle: {shuffled}")
    while shuffled[1] != 1:
        shuffled = shuffle(shuffled)
        count += 1
        print(f"{count}. shuffle: {shuffled}")

    return count


if __name__ == "__main__":
    deck = list(range(52))
    print(f"original order:  {deck}")
    shuffles_until_original = find_original(deck)
    print(f"It took {shuffles_until_original} shuffles to get the original order.")
