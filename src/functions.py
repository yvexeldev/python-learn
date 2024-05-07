def add(a: float, b: float) -> float:
    return a + b

def greet(name: str) -> str:
    return f"Hello, {name}!"

def is_even(number: int) -> bool:
    return number % 2 == 0

def multiply(a: float, b: float) -> float:
    return a * b

def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)

def factorial(number: int) -> int:
    if number == 0:
        return 1
    return number * factorial(number - 1)

def fibonacci(number: int) -> int:
    if number == 0 or number == 1:
        return 1
    return fibonacci(number - 1) + fibonacci(number - 2)

def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def reverse_list(numbers: list[int]) -> list[int]:
    return numbers[::-1]

# Usage of All functions
print(add(1, 2))
print(greet("John"))
print(is_even(10))
print(multiply(2, 3))
print(average([1, 2, 3, 4, 5]))
print(factorial(5))
print(fibonacci(5))
print(is_prime(7))
print(reverse_list([1, 2, 3, 4, 5]))
