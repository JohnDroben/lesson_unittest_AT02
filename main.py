def add(a, b):
   return a + b

def subtract(a, b):
   return a - b

def multiply(a, b):
   return a * b

def divide(a, b):
   return a / b

def safe_remainder(a, b): # функция для вычисления остатка от деления
   if b == 0:
      return None
   return a % b

def count_vowels(text): # функция для подсчета гласных
    """Возвращает количество гласных букв (a, e, i, o, u) в строке, независимо от регистра."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text.lower() if char in vowels)



