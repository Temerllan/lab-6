import math

nums = [2,5]
result = math.prod(nums)
print(result)


def count_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower



def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]



import time
import math

num = int(input())
delay = int(input())

time.sleep(delay / 1000)
print(f"Square root of {num} after {delay} miliseconds is {math.sqrt(num)}")



def all_true(t):
    return all(t)

t = (True, True, True)
print(all_true(t))




1. import os

path = input()

print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
print(os.listdir(path))



2. import os

path = input()

print("Существует:", os.path.exists(path))
print("Чтение разрешено:", os.access(path, os.R_OK))
print("Запись разрешена:", os.access(path, os.W_OK))
print("Исполнение разрешено:", os.access(path, os.X_OK))


3. import os

path = input()

if os.path.exists(path):
    print("Имя файла:", os.path.basename(path))
    print("Каталог:", os.path.dirname(path))
else:
    print("Указанный путь не существует")



4.filename = "example.txt"

with open(filename, 'r', encoding='utf-8') as f:
    print(len(f.readlines()))



5.list_data = ['apple', 'banana', 'cherry']

with open('output.txt', 'w', encoding='utf-8') as f:
    for item in list_data:
        f.write(item + '\n'



6.import string

for letter in string.ascii_uppercase:
    with open(f"{letter}.txt", "w", encoding="utf-8") as f:
        f.write(f"Файл {letter}.txt создан\n")

print("Все 26 файлов успешно созданы!")


7.source = input("Введите имя исходного файла: ")
destination = input("Введите имя файла назначения: ")

with open(source, 'r', encoding='utf-8') as src, open(destination, 'w', encoding='utf-8') as dest:
    dest.write(src.read())

print("Содержимое успешно скопировано!")



8.import os

path = input

if os.path.exists(path):
    if os.access(path, os.W_OK):
        os.remove(path)
        print
    else:
        print
else:
    print



