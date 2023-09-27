# value = 2.9
#
# # # BEGIN (write your solution here)
# converted_value1 = int(value)
# converted_value2 = str(converted_value1)
# print(converted_value2 + ' times')
#
#
# text = 'Never forget what you are, for surely the world will not'
#
# # # BEGIN (write your solution here)
# print(f'''First: {text[0]}
# # Last: {text[len(text)-1]}''')
#
# from random import random
#
# print(round(random()*10, 0))
#
#
# text = 'Never forget what you are, for surely the world will not'
#
# # # BEGIN (write your solution here)
# b = text.find('N')
# c = text.find(',')
# converted_b = str(b)
# converted_c = str(c)
# print(f'''Index of N: {b}
#  Index of ,: {c}''' )
# # # END
#
# text = 'When \t\n you play a \t\n game of thrones you win or you die.'
# print(text)
# # BEGIN (write your solution here)
# print(len(text[5:15].strip()))
#
#
# def greeting_with_return_and_printing():
#     print('Я появлюсь в консоли')
#     return 'Hello, Hexlet!'
#
#
# #И напечатает текст на экран, и вернет значение
# meetings = greeting_with_return_and_printing()
#
# def run():
#     return 5
#     return 10
#
#
# # Что будет выведено на экран?
# print(run())
# def truncate(text, length):
#     result = f"{text[0:length]}..."
#     return result
# tex = 'itworks'
# lengh = 4
# print(truncate(tex, lengh))

# def privet(credit, n = 4):
#     result = f'{credit.replace(credit[:12], n)}'
#     return result
#
# cred = '1234567890091212'
# f = int(input('Введите количество звездочек: '))
# np  = '*' * f
# print(privet(cred, np))

# def get_hidden_card(card_number, stars_count=5):
#     visible_digits_line = card_number[-5:]
#     return f"{'*' * stars_count}{visible_digits_line}"
#
# card_1 = '1234567890901212'
# print(get_hidden_card(card_1))

# def trim_and_repeat(text, offset = 3, repetitions = 2):
#     result = f"{text[:offset] * repetitions}"
#     return result
#
# text_for_repeat = 'python'
# print(trim_and_repeat(text_for_repeat))
#
# def word_multiply(text: str, n: int ) -> str:
#     result: str = text * n
#     return result
#
# text_for_multiply = 'python'
# n_n = 3
# print(word_multiply(text_for_multiply, n_n))

def is_palindrome(word):
    lower_word = word.lower()
    return lower_word == lower_word[::-1]
    return lower_word == ''.join(reversed(lower_word))

def is_not_palindrome(word):
    return not is_palindrome(word)

print(is_not_palindrome('wow'))
