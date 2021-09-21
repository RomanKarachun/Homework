def generate_squares(n):
    return {x: x**2 for x in range(1, n+1)}
print(generate_squares(5))
