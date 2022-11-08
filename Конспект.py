#1. Створіть файл, що містить метод
name = "AskPython"
def add(num1, num2):
        return num1 + num2
#2. Створіть Основний файл для імпорту модуля
import adder
nums = adder.add(5, 10)
print(nums)
#3. Імпорт Тільки Однією Функції
from adder import add

nums = add(5, 10)
print(nums)
#4. Використання Змінних З Нашого Модулю
import adder

nums = adder.add(5, 10)
print(nums)

print(adder.name)
#4. Імпорт, вказавши Ім'я папки
import modules.adder as adder

nums = adder.add(5, 10)
print(nums)

print(adder.name)


from modules import adder

nums = adder.add(5, 10)
print(nums)

print(adder.name)
#5. Додати Шлях до sys.path
import sys
print(sys.path)


import sys
sys.path.append("modules")
import adder

nums = adder.add(5, 10)
print(nums)

print(adder.name)
