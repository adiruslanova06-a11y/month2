from colorama import Fore, Back, Style, init
# Эта библиотека нужна для оформления вывода (цвета, стили текста) в терминале
print(Fore.RED + "Это красный текст")
print(Fore.GREEN + "Это зелёный текст")
print(Fore.BLUE + "Это синий текст")


nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print(i, j)
