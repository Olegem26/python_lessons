"""
- Изучить что такое функция
(!) Пример функции в lessons/m_2026_04_12/lessons.py
- Обернуть задачу с выводом ромба в функцию, которая:
-- Принимает h
-- Выводит ромб (ничего не возвращает)
- Изучить что такое LEGB в python (области видимости в коде)
"""

# Вот этот код нужно обернуть в функцию
h = int(input('введите число'))
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
