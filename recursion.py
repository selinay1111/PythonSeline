def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n - 1)

def palindrome(word: str) -> bool:
    # base case
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1:-1])

# TODO: count the occurrences of a number in a word
# example, count_occurrences("banana", "a") -> 3
def count_occurrences(word: str, letter: str) -> int:
    pass

#TODO: this is a tracing question, try to figure out on pen and paper what the output will be, and validate it after running the code
LIMIT = 1000

def fun2(n):
    if (n <= 0):
        return
    if (n > LIMIT):
        return
    print(n, end=" ")
    fun2(2 * n)
    print(n, end=" ")


# Driver code
# fun2(100)

# TODO: rewrite the fibonacci function without recursion, by using loops
def fibonacci_loops(n: int) -> int:
    pass


if __name__ == '__main__':
    print(palindrome("aabbccbbaa"))