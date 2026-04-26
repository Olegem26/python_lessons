"""
- Повторить пройденный материал
- Выполнить задачу
- Повторить типы данных: int, float, str, bool, None, datetime, Decimal, функции как объект
- Повторить что такое LEGB в python (области видимости в коде)
- Изучить list и способы работы с ним
"""

# Задача: добавить ещё один аргумент, который будет изменять поведение функции
def get_rhomb(h, char = '-', text = 'возвращаем ромб'):
    print(text)
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