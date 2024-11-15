"""
2. Research about Caching Mechanism and then, implement a caching mechanism for a function that calculates the square of a number. Instructions:
- Define a function square(n) that calculates the square of an input number n.
- Implement a cache using a dictionary to store previously computed squares.
- Modify the square(n) function to check if the result for the given n is already in the cache:
  - If it is, return the cached result.
  - If it is not, compute the square, store it in the cache, and then return the result.
"""

cache_dict = {}


def square(n: int) -> str:
    if n ** 2 in cache_dict.values():
        return f"Value already in cache: {cache_dict[n]}"
    else:
        cache_dict[n] = n ** 2
        return f"New value added to the cache: {cache_dict[n]}"


list_to_test = [2, 5, 1, 3, 7, 1, 6, 2, 5]
for i in list_to_test:
    print(f"Checking caching mechanism: {square(i)}")

"""
Output:
    Checking caching mechanism: New value added to the cache: 4
    Checking caching mechanism: New value added to the cache: 25
    Checking caching mechanism: New value added to the cache: 1
    Checking caching mechanism: New value added to the cache: 9
    Checking caching mechanism: New value added to the cache: 49
    Checking caching mechanism: Value already in cache: 1
    Checking caching mechanism: New value added to the cache: 36
    Checking caching mechanism: Value already in cache: 4
    Checking caching mechanism: Value already in cache: 25
"""

