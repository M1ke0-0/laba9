print("Nomer 1")

def greet(name):
    return "Привет: " + name
print(greet(name))

def square(number):
    return number**2
print(square(number))

def max_of_two(x, y):
    return max(x, y)
print(max_of_two(x, y))


print("Nomer 2")

def describe_person(name, age=30):
    return "Имя: " + name + ", Возраст: " + str(age)
print(describe_person(name, age))


print("Nomer 3")

def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
print(is_prime(number))