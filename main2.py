import colorama
from colorama import Fore, Back, Style

print(type(colorama))
print(dir(colorama))
help(colorama)

# colorama працює так:
# 1. якщо вам потрібно зробити якийсь текст якогось кольору, потрібно записати так:
# print(Fore.(колір тексту великими літерами) + 'сам текст'), ось приклад:
print(Fore.GREEN + 'Hello')

# 2. якщо вам потрібно зробити заливку фону, запишіть так:
# print(Back.(колір фону великими літерами) + 'текст з яким буде фон', ось приклад:
print(Back.BLUE + 'Bohdan')

# 3. якщо вам потрібно зробити текст більше/менше жирним, запишіть так:
# print(Style.(напишіть DIM(менше жирний) або NORMAL або BRIGHT(жирніший)) + 'текст')
# АЛЕ перед цим потрібно забрати всі попередні кольори та фони командою print(Style.RESET_ALL), приклад:
print(Style.RESET_ALL)
print(Style.BRIGHT + 'Summer')
print(Style.NORMAL + 'Summer')
print(Style.DIM + 'Summer')

# майте на увазу colorama може дати колір тексту або фону тільки ось цими кольорами:
# RED, GREEN, YELLOW, BLACK, BLUE, WHITE, MAGENTA(фіолетовий), CYAN(блакитний)

