def rhomb(h):
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
    return rhomb
    
result = rhomb(4)
print(result)



def get_rhomb(h, char = '-'):

    rhomb = ''

    for i in range(h):
        spaces = (h - i) - 1
        stars = (2 * i) + 1
        row = ' ' * spaces + char * stars + '\n'
        rhomb += row
    for i in range((h - 1) - 1, 0 - 1, -1):
        spaces = (h - i) - 1
        stars = (2 * i) + 1
        row = ' ' * spaces + char * stars + '\n'
        rhomb += row

    return rhomb

result = get_rhomb(4, '+',)
print(result)

result = get_rhomb(4)
print(result)
