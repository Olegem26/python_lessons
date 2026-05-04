def paint_rhomb(h):
    for i in range(h):
        spaces = (h - i) - 1
        stars = (2 * i) + 1
        row = ' ' * spaces + '*' * stars
        print(row)
    for i in range((h - 1) - 1, 0 - 1, -1):
        spaces = (h - i) - 1
        stars = (2 * i) + 1
        row = ' ' * spaces + '*' * stars
        print(row)
    # return None

result = paint_rhomb(4)
print(result)

print("//////////////////////////////////////////////////")

def get_rhomb(h):

    rhomb = ''

    for i in range(h):
        spaces = (h - i) - 1
        stars = (2 * i) + 1
        row = ' ' * spaces + '*' * stars + '\n'
        rhomb += row
    for i in range((h - 1) - 1, 0 - 1, -1):
        spaces = (h - i) - 1
        stars = (2 * i) + 1
        row = ' ' * spaces + '*' * stars + '\n'
        rhomb += row

    return rhomb

result = get_rhomb(4)
print(result)